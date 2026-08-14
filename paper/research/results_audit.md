# Results audit

- Source run table: `outputs/latest/runs.csv`
- Source event log: `outputs/latest/events.jsonl`
- Runs: 120
- Events: 461
- Balanced cells: 12 cells, 10 runs per cell
- Model/parse-error runs: 0
- Action-count reconciliation: PASS (461 events)
- Symbolic-action vocabulary check: PASS
- Primary contrast: 17/20 score-maximizing versus
  13/20 authorized-scope attempts with the gate off
- Primary risk difference: +0.200
- Primary two-sided Fisher exact p-value: 0.273343
- Valid completion: 14/60 gate on versus
  10/60 gate off
- Completion two-sided Fisher exact p-value: 0.494162

The executed-shortcut contrast is not tested as a behavioral effect because
the gate deterministically maps prohibited actions to `authorization_denied`.
Its zero executed rate is an enforcement invariant. Behavioral interpretation
therefore centers on attempt rate, persistence after denial, safe recovery, and
valid completion.
