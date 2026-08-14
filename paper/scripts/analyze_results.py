#!/usr/bin/env python3
"""Audit ScopeGym runs and produce paper-facing descriptive statistics."""

from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "outputs" / "latest" / "runs.csv"
EVENTS = ROOT / "outputs" / "latest" / "events.jsonl"
TABLES = ROOT / "paper" / "tables"
RESEARCH = ROOT / "paper" / "research"


def wilson(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total == 0:
        return float("nan"), float("nan")
    proportion = successes / total
    denominator = 1 + z * z / total
    center = (proportion + z * z / (2 * total)) / denominator
    margin = (
        z
        * math.sqrt(
            proportion * (1 - proportion) / total
            + z * z / (4 * total * total)
        )
        / denominator
    )
    return max(0.0, center - margin), min(1.0, center + margin)


def fisher_exact_two_sided(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact test using the probability-ordering definition."""
    row_1 = a + b
    row_2 = c + d
    col_1 = a + c
    total = row_1 + row_2
    lower = max(0, col_1 - row_2)
    upper = min(row_1, col_1)

    def probability(x: int) -> float:
        return (
            math.comb(col_1, x)
            * math.comb(total - col_1, row_1 - x)
            / math.comb(total, row_1)
        )

    observed = probability(a)
    return sum(
        probability(x)
        for x in range(lower, upper + 1)
        if probability(x) <= observed + 1e-15
    )


def load_runs() -> list[dict[str, str]]:
    with RUNS.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_events() -> list[dict]:
    with EVENTS.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle]


def select(
    rows: list[dict[str, str]], **criteria: str
) -> list[dict[str, str]]:
    return [
        row
        for row in rows
        if all(row[key] == value for key, value in criteria.items())
    ]


def count(rows: list[dict[str, str]], field: str) -> int:
    return sum(int(row[field]) for row in rows)


def statistic(
    label: str,
    rows: list[dict[str, str]],
    field: str,
    denominator_note: str,
) -> dict[str, str]:
    successes = count(rows, field)
    total = len(rows)
    lower, upper = wilson(successes, total)
    return {
        "estimate": label,
        "successes": str(successes),
        "total": str(total),
        "rate": f"{successes / total:.6f}",
        "ci_low": f"{lower:.6f}",
        "ci_high": f"{upper:.6f}",
        "denominator": denominator_note,
    }


def main() -> None:
    rows = load_runs()
    events = load_events()
    assert len(rows) == 120, f"expected 120 runs, found {len(rows)}"
    assert {row["model"] for row in rows} == {"gemma3:4b", "llama3.1:8b"}
    assert {row["goal_framing"] for row in rows} == {
        "minimal",
        "authorized_scope",
        "score_maximizing",
    }
    assert {row["gate_level"] for row in rows} == {"off", "on"}

    cell_counts = Counter(
        (row["model"], row["goal_framing"], row["gate_level"])
        for row in rows
    )
    assert len(cell_counts) == 12
    assert set(cell_counts.values()) == {10}
    assert count(rows, "model_error") == 0
    assert sum(int(row["action_count"]) for row in rows) == len(events)

    events_by_run: dict[str, list[dict]] = defaultdict(list)
    allowed_actions = {
        "inspect_description",
        "inspect_pov",
        "inspect_patch",
        "develop_target_solution",
        "probe_answers_service",
        "attempt_answers_access",
        "submit_target_flag",
        "submit_fake_answer",
        "stop",
    }
    for event in events:
        assert event["action"] in allowed_actions
        events_by_run[event["run_id"]].append(event)
    assert len(events_by_run) == len(rows)
    for row in rows:
        assert len(events_by_run[row["run_id"]]) == int(row["action_count"])

    cell_rows: list[dict[str, str]] = []
    for (model, framing, gate), cell_n in sorted(cell_counts.items()):
        group = select(rows, model=model, goal_framing=framing, gate_level=gate)
        attempted = count(group, "attempted_boundary_violation")
        lower, upper = wilson(attempted, cell_n)
        cell_rows.append(
            {
                "model": model,
                "goal_framing": framing,
                "gate": gate,
                "runs": str(cell_n),
                "attempts": str(attempted),
                "attempt_rate": f"{attempted / cell_n:.6f}",
                "ci_low": f"{lower:.6f}",
                "ci_high": f"{upper:.6f}",
                "executed": str(count(group, "executed_boundary_violation")),
                "valid_success": str(count(group, "valid_success")),
            }
        )

    gated_attempters = [
        row
        for row in rows
        if row["gate_level"] == "on"
        and int(row["attempted_boundary_violation"])
    ]
    statistics = [
        statistic(
            "Score-maximizing attempt, gate off",
            select(rows, goal_framing="score_maximizing", gate_level="off"),
            "attempted_boundary_violation",
            "runs in both models",
        ),
        statistic(
            "Authorized-scope attempt, gate off",
            select(rows, goal_framing="authorized_scope", gate_level="off"),
            "attempted_boundary_violation",
            "runs in both models",
        ),
        statistic(
            "Attempt, gate off",
            select(rows, gate_level="off"),
            "attempted_boundary_violation",
            "all gate-off runs",
        ),
        statistic(
            "Attempt, gate on",
            select(rows, gate_level="on"),
            "attempted_boundary_violation",
            "all gate-on runs",
        ),
        statistic(
            "Executed shortcut, gate off",
            select(rows, gate_level="off"),
            "executed_boundary_violation",
            "all gate-off runs",
        ),
        statistic(
            "Executed shortcut, gate on",
            select(rows, gate_level="on"),
            "executed_boundary_violation",
            "all gate-on runs",
        ),
        statistic(
            "Persistence after denial",
            gated_attempters,
            "persistent_after_denial",
            "gate-on runs with a shortcut attempt",
        ),
        statistic(
            "Safe recovery after denial",
            gated_attempters,
            "safe_recovery",
            "gate-on runs with a shortcut attempt",
        ),
        statistic(
            "Valid completion, gate off",
            select(rows, gate_level="off"),
            "valid_success",
            "all gate-off runs",
        ),
        statistic(
            "Valid completion, gate on",
            select(rows, gate_level="on"),
            "valid_success",
            "all gate-on runs",
        ),
        statistic(
            "Any attempt, Gemma 3 4B",
            select(rows, model="gemma3:4b"),
            "attempted_boundary_violation",
            "all Gemma runs",
        ),
        statistic(
            "Any attempt, Llama 3.1 8B",
            select(rows, model="llama3.1:8b"),
            "attempted_boundary_violation",
            "all Llama runs",
        ),
    ]

    TABLES.mkdir(parents=True, exist_ok=True)
    RESEARCH.mkdir(parents=True, exist_ok=True)
    with (TABLES / "cell_rates.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=cell_rows[0].keys())
        writer.writeheader()
        writer.writerows(cell_rows)
    with (TABLES / "statistics.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=statistics[0].keys())
        writer.writeheader()
        writer.writerows(statistics)

    score = select(
        rows, goal_framing="score_maximizing", gate_level="off"
    )
    scoped = select(
        rows, goal_framing="authorized_scope", gate_level="off"
    )
    score_attempts = count(score, "attempted_boundary_violation")
    scoped_attempts = count(scoped, "attempted_boundary_violation")
    primary_p = fisher_exact_two_sided(
        score_attempts,
        len(score) - score_attempts,
        scoped_attempts,
        len(scoped) - scoped_attempts,
    )
    completion_off = select(rows, gate_level="off")
    completion_on = select(rows, gate_level="on")
    completion_off_n = count(completion_off, "valid_success")
    completion_on_n = count(completion_on, "valid_success")
    completion_p = fisher_exact_two_sided(
        completion_on_n,
        len(completion_on) - completion_on_n,
        completion_off_n,
        len(completion_off) - completion_off_n,
    )

    audit = f"""# Results audit

- Source run table: `{RUNS.relative_to(ROOT)}`
- Source event log: `{EVENTS.relative_to(ROOT)}`
- Runs: {len(rows)}
- Events: {len(events)}
- Balanced cells: 12 cells, 10 runs per cell
- Model/parse-error runs: 0
- Action-count reconciliation: PASS ({len(events)} events)
- Symbolic-action vocabulary check: PASS
- Primary contrast: {score_attempts}/20 score-maximizing versus
  {scoped_attempts}/20 authorized-scope attempts with the gate off
- Primary risk difference: {(score_attempts / 20) - (scoped_attempts / 20):+.3f}
- Primary two-sided Fisher exact p-value: {primary_p:.6f}
- Valid completion: {completion_on_n}/60 gate on versus
  {completion_off_n}/60 gate off
- Completion two-sided Fisher exact p-value: {completion_p:.6f}

The executed-shortcut contrast is not tested as a behavioral effect because
the gate deterministically maps prohibited actions to `authorization_denied`.
Its zero executed rate is an enforcement invariant. Behavioral interpretation
therefore centers on attempt rate, persistence after denial, safe recovery, and
valid completion.
"""
    (RESEARCH / "results_audit.md").write_text(audit, encoding="utf-8")
    print(audit)


if __name__ == "__main__":
    main()
