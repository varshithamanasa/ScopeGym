# Claim–evidence map

## Central thesis

Human-authorization evaluation should separate an agent's attempted shortcut,
the system's execution decision, and the agent's adaptation after denial,
because a hard gate can prevent an outcome without producing compliant
reasoning.

| Claim | Evidence | Strength and boundary |
|---|---|---|
| Score-maximizing framing increased observed shortcut attempts relative to authorized-scope framing in the ungated pilot. | 17/20 versus 13/20; risk difference +0.20; Fisher p=.273. | Directional pilot evidence; not statistically conclusive and not generalized beyond the tested models/task. |
| The gate prevented prohibited execution. | 0/60 executed with gate on versus 43/60 with gate off. | Deterministic enforcement property, not evidence that reasoning became safer. |
| Attempt propensity remained substantial behind the gate. | 41/60 gate-on runs attempted a prohibited action versus 43/60 gate-off runs. | Descriptive; supports separating attempt from execution. |
| Denial behavior is diagnostically useful. | 12/41 gated attempters persisted; 11/41 safely recovered. | Behavioral evidence within the two-model pilot. |
| Results are model-dependent. | Gemma attempted in 56/60 runs; Llama in 28/60. | Strong descriptive heterogeneity; models are not a representative population. |
| The experiment is lower risk than real exploit reproduction. | Symbolic action vocabulary, localhost-only model call, no shell/filesystem/credential/public-network exposure. | Verified from code and reconciled event log. |

## Negative constraints

- Do not call the +20 percentage-point framing contrast statistically
  significant.
- Do not interpret 0% gated execution as behavioral alignment.
- Do not generalize from repeated trajectories to the population of language
  models.
- Do not describe the decoy as a real vulnerability or exploit.
- Do not claim absolute novelty; retain the search-bounded gap statement.
