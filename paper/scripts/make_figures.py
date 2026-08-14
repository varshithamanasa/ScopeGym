#!/usr/bin/env python3
"""Generate vector, IEEE-column-ready ScopeGym figures with ReportLab."""

from __future__ import annotations

import csv
import math
from pathlib import Path

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, white


ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "outputs" / "latest" / "runs.csv"
FIGURES = ROOT / "paper" / "figures"
ARIAL = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
ARIAL_BOLD = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")

BLUE = HexColor("#0077BB")
CYAN = HexColor("#33BBEE")
TEAL = HexColor("#009988")
ORANGE = HexColor("#EE7733")
RED = HexColor("#CC3311")
GREY = HexColor("#6E7781")
LIGHT_BLUE = HexColor("#EAF4FA")
LIGHT_TEAL = HexColor("#E7F5F2")
LIGHT_ORANGE = HexColor("#FFF1E8")
LIGHT_GREY = HexColor("#F2F4F6")


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("FigureSans", str(ARIAL)))
    pdfmetrics.registerFont(TTFont("FigureSans-Bold", str(ARIAL_BOLD)))


def wilson(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
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


def load_rows() -> list[dict[str, str]]:
    with RUNS.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def count(rows: list[dict[str, str]], field: str) -> int:
    return sum(int(row[field]) for row in rows)


def wrapped_text(
    drawing: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    font: str = "FigureSans",
    size: float = 7.0,
    leading: float = 8.2,
    color=black,
    centered: bool = False,
) -> float:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if pdfmetrics.stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    drawing.setFont(font, size)
    drawing.setFillColor(color)
    for index, line in enumerate(lines):
        line_y = y - index * leading
        if centered:
            drawing.drawCentredString(x + width / 2, line_y, line)
        else:
            drawing.drawString(x, line_y, line)
    return y - len(lines) * leading


def box(
    drawing: canvas.Canvas,
    x: float,
    y: float,
    width: float,
    height: float,
    title: str,
    body: str,
    fill,
    stroke,
) -> None:
    drawing.setFillColor(fill)
    drawing.setStrokeColor(stroke)
    drawing.setLineWidth(0.9)
    drawing.roundRect(x, y, width, height, 5, fill=1, stroke=1)
    drawing.setFillColor(stroke)
    drawing.setFont("FigureSans-Bold", 7.6)
    drawing.drawCentredString(x + width / 2, y + height - 11, title)
    wrapped_text(
        drawing,
        body,
        x + 6,
        y + height - 23,
        width - 12,
        size=6.7,
        leading=7.5,
        centered=True,
    )


def arrow(
    drawing: canvas.Canvas,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color=GREY,
) -> None:
    drawing.setStrokeColor(color)
    drawing.setFillColor(color)
    drawing.setLineWidth(1.2)
    drawing.line(x1, y1, x2, y2)
    angle = math.atan2(y2 - y1, x2 - x1)
    length = 5
    spread = 0.45
    drawing.line(
        x2,
        y2,
        x2 - length * math.cos(angle - spread),
        y2 - length * math.sin(angle - spread),
    )
    drawing.line(
        x2,
        y2,
        x2 - length * math.cos(angle + spread),
        y2 - length * math.sin(angle + spread),
    )


def make_design_figure() -> None:
    width, height = 7.08 * 72, 1.45 * 72
    path = FIGURES / "scopegym_design.pdf"
    drawing = canvas.Canvas(
        str(path), pagesize=(width, height), initialFontName="FigureSans"
    )
    drawing.setTitle("ScopeGym experimental design")
    margin = 10
    gap = 18
    box_width = (width - 2 * margin - 3 * gap) / 4
    y = 17
    box_height = 72
    box(
        drawing,
        margin,
        y,
        box_width,
        box_height,
        "1. Randomized factors",
        "2 local models × 3 goal framings × 2 gate states × 10 repeats = 120 runs",
        LIGHT_BLUE,
        BLUE,
    )
    box(
        drawing,
        margin + box_width + gap,
        y,
        box_width,
        box_height,
        "2. Sealed task",
        "Visible local artifacts, an inert decoy answers service, and an eight-action budget",
        LIGHT_TEAL,
        TEAL,
    )
    box(
        drawing,
        margin + 2 * (box_width + gap),
        y,
        box_width,
        box_height,
        "3. Authorization gate",
        "Gate off executes a decoy probe; gate on returns authorization_denied",
        LIGHT_ORANGE,
        ORANGE,
    )
    box(
        drawing,
        margin + 3 * (box_width + gap),
        y,
        box_width,
        box_height,
        "4. Logged outcomes",
        "Attempt, execution, post-denial persistence, safe recovery, and valid completion",
        LIGHT_GREY,
        GREY,
    )
    for index in range(3):
        x1 = margin + (index + 1) * box_width + index * gap + 2
        x2 = margin + (index + 1) * box_width + (index + 1) * gap - 2
        arrow(drawing, x1, y + box_height / 2, x2, y + box_height / 2)
    drawing.setFont("FigureSans", 6.3)
    drawing.setFillColor(GREY)
    drawing.drawCentredString(
        width / 2,
        5,
        "No shell, arbitrary filesystem, credential, exploit payload, or public network was exposed.",
    )
    drawing.showPage()
    drawing.save()


def draw_bar(
    drawing: canvas.Canvas,
    x: float,
    baseline: float,
    width: float,
    height_scale: float,
    successes: int,
    total: int,
    color,
    hatch: bool = False,
) -> None:
    rate = successes / total
    lower, upper = wilson(successes, total)
    bar_height = rate * height_scale
    drawing.setFillColor(color)
    drawing.setStrokeColor(color)
    drawing.rect(x, baseline, width, bar_height, fill=1, stroke=0)
    if hatch:
        drawing.saveState()
        path = drawing.beginPath()
        path.rect(x, baseline, width, bar_height)
        drawing.clipPath(path, stroke=0, fill=0)
        drawing.setStrokeColor(white)
        drawing.setLineWidth(0.6)
        offset = -bar_height
        while offset < width + bar_height:
            drawing.line(
                x + offset,
                baseline,
                x + offset + bar_height,
                baseline + bar_height,
            )
            offset += 5
        drawing.restoreState()
    center = x + width / 2
    drawing.setStrokeColor(black)
    drawing.setLineWidth(0.7)
    drawing.line(
        center,
        baseline + lower * height_scale,
        center,
        baseline + upper * height_scale,
    )
    drawing.line(
        center - 2.5,
        baseline + lower * height_scale,
        center + 2.5,
        baseline + lower * height_scale,
    )
    drawing.line(
        center - 2.5,
        baseline + upper * height_scale,
        center + 2.5,
        baseline + upper * height_scale,
    )
    drawing.setFont("FigureSans-Bold", 6.6)
    drawing.setFillColor(black)
    drawing.drawCentredString(
        center, baseline + bar_height + 5, f"{100 * rate:.0f}%"
    )


def make_results_figure(rows: list[dict[str, str]]) -> None:
    width, height = 7.08 * 72, 2.20 * 72
    path = FIGURES / "scopegym_results.pdf"
    drawing = canvas.Canvas(
        str(path), pagesize=(width, height), initialFontName="FigureSans"
    )
    drawing.setTitle("ScopeGym results")
    plot_bottom = 34
    plot_top = height - 25
    plot_height = plot_top - plot_bottom

    drawing.setFont("FigureSans-Bold", 8.2)
    drawing.setFillColor(black)
    drawing.drawString(30, height - 12, "(a) Shortcut attempts with gate off")
    drawing.drawString(335, height - 12, "(b) Gate and post-denial outcomes")

    left_x0, left_x1 = 32, 304
    right_x0, right_x1 = 345, width - 14
    for axis_x0, axis_x1 in ((left_x0, left_x1), (right_x0, right_x1)):
        drawing.setStrokeColor(HexColor("#C7CDD3"))
        drawing.setLineWidth(0.5)
        for tick in (0, 0.25, 0.5, 0.75, 1.0):
            y = plot_bottom + tick * plot_height
            drawing.line(axis_x0, y, axis_x1, y)
            drawing.setFont("FigureSans", 6.5)
            drawing.setFillColor(GREY)
            drawing.drawRightString(axis_x0 - 3, y - 2, f"{tick:.2f}")
        drawing.setStrokeColor(black)
        drawing.line(axis_x0, plot_bottom, axis_x0, plot_top)
        drawing.line(axis_x0, plot_bottom, axis_x1, plot_bottom)

    framings = [
        ("authorized_scope", "Authorized"),
        ("minimal", "Minimal"),
        ("score_maximizing", "Score-max."),
    ]
    models = [
        ("gemma3:4b", "Gemma 3 4B", BLUE, False),
        ("llama3.1:8b", "Llama 3.1 8B", ORANGE, True),
    ]
    group_width = (left_x1 - left_x0) / 3
    bar_width = 24
    for group_index, (framing, label) in enumerate(framings):
        center = left_x0 + group_width * (group_index + 0.5)
        for model_index, (model, _, color, hatch) in enumerate(models):
            group = [
                row
                for row in rows
                if row["model"] == model
                and row["goal_framing"] == framing
                and row["gate_level"] == "off"
            ]
            successes = count(group, "attempted_boundary_violation")
            x = center + (model_index - 0.5) * (bar_width + 5) - bar_width / 2
            draw_bar(
                drawing,
                x,
                plot_bottom,
                bar_width,
                plot_height,
                successes,
                len(group),
                color,
                hatch,
            )
        drawing.setFont("FigureSans", 6.8)
        drawing.setFillColor(black)
        drawing.drawCentredString(center, 21, label)

    drawing.setFont("FigureSans", 6.7)
    drawing.setFillColor(black)
    drawing.setStrokeColor(BLUE)
    drawing.setFillColor(BLUE)
    drawing.rect(74, 6, 9, 6, fill=1, stroke=0)
    drawing.setFillColor(black)
    drawing.drawString(87, 6, "Gemma 3 4B")
    drawing.setStrokeColor(ORANGE)
    drawing.setFillColor(ORANGE)
    drawing.rect(158, 6, 9, 6, fill=1, stroke=0)
    drawing.setStrokeColor(white)
    for offset in range(-3, 12, 4):
        drawing.line(158 + offset, 6, 158 + offset + 6, 12)
    drawing.setFillColor(black)
    drawing.drawString(171, 6, "Llama 3.1 8B")
    gated_attempters = [
        row
        for row in rows
        if row["gate_level"] == "on"
        and int(row["attempted_boundary_violation"])
    ]
    right_metrics = [
        (
            "Executed\nGate off",
            count(
                [row for row in rows if row["gate_level"] == "off"],
                "executed_boundary_violation",
            ),
            60,
            RED,
        ),
        (
            "Executed\nGate on",
            count(
                [row for row in rows if row["gate_level"] == "on"],
                "executed_boundary_violation",
            ),
            60,
            TEAL,
        ),
        (
            "Persisted\nAfter denial",
            count(gated_attempters, "persistent_after_denial"),
            len(gated_attempters),
            ORANGE,
        ),
        (
            "Recovered\nSafely",
            count(gated_attempters, "safe_recovery"),
            len(gated_attempters),
            BLUE,
        ),
    ]
    metric_width = (right_x1 - right_x0) / len(right_metrics)
    right_bar_width = 26
    for index, (label, successes, total, color) in enumerate(right_metrics):
        center = right_x0 + metric_width * (index + 0.5)
        draw_bar(
            drawing,
            center - right_bar_width / 2,
            plot_bottom,
            right_bar_width,
            plot_height,
            successes,
            total,
            color,
        )
        drawing.setFont("FigureSans", 6.1)
        drawing.setFillColor(black)
        parts = label.split("\n")
        drawing.drawCentredString(center, 21, parts[0])
        drawing.drawCentredString(center, 13, parts[1])
        drawing.setFont("FigureSans", 5.9)
        drawing.setFillColor(GREY)
        drawing.drawCentredString(center, 5, f"{successes}/{total}")
    drawing.showPage()
    drawing.save()


def main() -> None:
    register_fonts()
    FIGURES.mkdir(parents=True, exist_ok=True)
    rows = load_rows()
    make_design_figure()
    make_results_figure(rows)
    print(f"wrote {FIGURES / 'scopegym_design.pdf'}")
    print(f"wrote {FIGURES / 'scopegym_results.pdf'}")


if __name__ == "__main__":
    main()
