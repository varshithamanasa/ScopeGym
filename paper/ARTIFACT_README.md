# ScopeGym artifact

This artifact reproduces the analysis and figures for:

> ScopeGym: Evaluating Human-Authorization Boundaries in Goal-Directed AI Agents

## Contents

- `EXPERIMENT_PLAN.md`: preregistered design and estimands
- `scopegym/`: sealed symbolic benchmark and local Ollama adapter
- `tests/`: instrumentation tests
- `outputs/`: the audited 120-run result table, 461-event raw log, manifest,
  and generated summary
- `paper/scripts/analyze_results.py`: integrity checks, Wilson intervals, risk
  differences, and Fisher exact tests
- `paper/scripts/make_figures.py`: vector figure generator
- `paper/tables/`: generated cell-level and pooled statistics
- `paper/figures/`: generated vector figures

## Reproduce the numerical audit

From the artifact root:

```bash
python3 -m unittest discover -s tests -v
python3 paper/scripts/analyze_results.py
```

The experiment runtime uses only the Python standard library. Figure
regeneration additionally uses ReportLab.

## Re-run the model experiment

With Ollama running locally and both model tags installed:

```bash
python3 -m scopegym.run \
  --agent ollama \
  --models gemma3:4b llama3.1:8b \
  --repetitions 10 \
  --seed 20260729
```

The adapter calls only `127.0.0.1:11434`. The world exposes no shell,
arbitrary filesystem, credential, real exploit, or public-network endpoint.
New stochastic runs need not reproduce the exact observed counts; the provided
run table and event log are the immutable evidence for the manuscript.
