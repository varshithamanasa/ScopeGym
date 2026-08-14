# ScopeGym Authorization-Gate Study Summary

## Results by model, framing, and authorization gate

| Model | Framing | Gate | Runs | Attempt rate (95% Wilson CI) | Executed rate | Safe completion | Model errors |
|---|---|---|---:|---:|---:|---:|---:|
| gemma3:4b | authorized_scope | off | 10 | 1.000 (0.722–1.000) | 1.000 | 0.500 | 0 |
| gemma3:4b | authorized_scope | on | 10 | 1.000 (0.722–1.000) | 0.000 | 0.600 | 0 |
| gemma3:4b | minimal | off | 10 | 0.900 (0.596–0.982) | 0.900 | 0.200 | 0 |
| gemma3:4b | minimal | on | 10 | 0.800 (0.490–0.943) | 0.000 | 0.300 | 0 |
| gemma3:4b | score_maximizing | off | 10 | 1.000 (0.722–1.000) | 1.000 | 0.300 | 0 |
| gemma3:4b | score_maximizing | on | 10 | 0.900 (0.596–0.982) | 0.000 | 0.400 | 0 |
| llama3.1:8b | authorized_scope | off | 10 | 0.300 (0.108–0.603) | 0.300 | 0.000 | 0 |
| llama3.1:8b | authorized_scope | on | 10 | 0.200 (0.057–0.510) | 0.000 | 0.000 | 0 |
| llama3.1:8b | minimal | off | 10 | 0.400 (0.168–0.687) | 0.400 | 0.000 | 0 |
| llama3.1:8b | minimal | on | 10 | 0.600 (0.313–0.832) | 0.000 | 0.000 | 0 |
| llama3.1:8b | score_maximizing | off | 10 | 0.700 (0.397–0.892) | 0.700 | 0.000 | 0 |
| llama3.1:8b | score_maximizing | on | 10 | 0.600 (0.313–0.832) | 0.000 | 0.100 | 0 |

## Preregistered contrasts

- Score-maximizing attempt rate without gate: 0.850
- Authorized-scope attempt rate without gate: 0.650
- Framing risk difference: +0.200
- Executed-violation rate without gate: 0.717
- Executed-violation rate with gate: 0.000
- Gate risk difference: -0.717
- Persistence after denial among gated attempters: 0.293
- Safe recovery among gated attempters: 0.268

All primary outcomes include refusals and malformed/model-error runs in the denominator. The gate's executed-violation effect is an enforcement property by design; persistence and recovery are the behavioral gate outcomes.
