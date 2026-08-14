# Build and verification

From the repository root:

```bash
/Users/varshithamanjunath/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 paper/scripts/analyze_results.py
/Users/varshithamanjunath/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 paper/scripts/make_figures.py
tools/tectonic/tectonic -X compile paper/main.tex --outdir paper/build
```

The analysis script refuses to continue unless it finds 120 runs, 12 balanced
cells, zero model/parse errors, and exact reconciliation between event count
and per-run action counts.

The Tectonic 0.16.9 macOS ARM binary was downloaded from the official GitHub
release. Its archive SHA-256 was verified as:

`edb67c61aba768289f6da441c9e6f523cfaff4f8b2a5708523ef29c543f8e88e`

The verified conference/preprint PDF is copied from `paper/build/main.pdf` to
`paper/ScopeGym_conference_preprint.pdf` only after page-size, page-count,
font-embedding, citation, and visual checks pass.
