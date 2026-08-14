# Code Experiment Plan

## Material Passport

- Origin Skill: experiment-agent
- Origin Mode: plan
- Origin Date: 2026-07-24
- Verification Status: UNVERIFIED
- Version Label: code_plan_v1

## Experiment Overview

- **Title**: ScopeGym: Goal Framing, Information Access, and Benchmark Circumvention
- **Objective**: Estimate how goal framing and supplied vulnerability
  information affect intended task completion and boundary-violation attempts
  in the presence of benchmark-integrity traps.
- **Primary RQ**: Does a score-maximizing goal increase boundary-violation
  attempts compared with an explicit authorized-scope instruction?
- **Primary hypothesis**: The boundary-violation rate is higher under
  score-maximizing framing than under authorized-scope framing when a shortcut
  is visible.
- **Type**: simulation / agent evaluation

## Variables

- **Independent variables**:
  - Goal framing: minimal, authorized scope, score maximizing
  - Authorization gate: off, on
  - Model: Gemma 3 4B, Llama 3.1 8B
- **Primary dependent variable**: any boundary-violation attempt per run
- **Secondary dependent variables**: executed violation, persistence after
  denial, safe recovery, valid target success, action count, and
  time-to-first-boundary-attempt
- **Controls**: identical world, action vocabulary, seed schedule, run budget,
  and scoring logic across conditions
- **Potential confounds**: prompt length, model nondeterminism, provider safety
  layer, task difficulty, cross-run memory, and model updates

## Design

Full 2 × 3 × 2 factorial randomized experiment with 10 repetitions per cell
(120 runs). The included scripted agent remains solely a deterministic
pipeline-validation baseline.

## Setup

- **Language/Framework**: Python 3.11+ standard library
- **Entry Command**:
  `python3 -m scopegym.run --agent ollama --models gemma3:4b llama3.1:8b --repetitions 10 --seed 20260729`
- **Working Directory**: repository root
- **Dependencies**: none beyond Python
- **Environment**: sealed synthetic state machine; no network or subprocesses

## Expected Outputs

| Output | Path | Format | Success Criterion |
|---|---|---|---|
| Run table | `outputs/latest/runs.csv` | CSV | 120 rows and required columns |
| Event log | `outputs/latest/events.jsonl` | JSONL | one or more events per run |
| Summary | `outputs/latest/summary.md` | Markdown | reports all factor levels |
| Manifest | `outputs/latest/manifest.json` | JSON | records seed and design |

## Monitoring Configuration

- **Timeout**: 5 minutes
- **Monitor files**: run directory under `outputs/`
- **Experiment type override**: simulation

## Analysis Plan

- **Primary estimand**: risk difference in attempted boundary violations
  between `score_maximizing` and `authorized_scope` without the gate
- **Gate estimand**: risk difference in executed boundary violations between
  gate-on and gate-off conditions
- **Uncertainty**: Wilson 95% confidence intervals for condition proportions;
  bootstrap or mixed-effects logistic regression is recommended for real-model
  data with multiple task IDs
- **Secondary comparisons**: valid-success rate and mean action count across all
  factorial cells
- **Multiplicity**: primary contrast is confirmatory; all remaining contrasts
  are exploratory and should use Holm correction in a paper
- **Exclusions**: infrastructure failures before the first agent action; never
  exclude refusals, failures, or boundary violations
- **Interpretation boundary**: scripted-agent results validate instrumentation
  only and provide no inference about real AI systems

## Safety

All endpoints are in-memory labels. There is no shell, package registry,
credential, public network, exploit payload, or real vulnerable service.
