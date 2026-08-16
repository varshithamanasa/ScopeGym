# Build and verification

From the repository root:

```bash
python3 paper/scripts/analyze_results.py
python3 paper/scripts/make_figures.py
```

The analysis script refuses to continue unless it finds 120 runs, 12 balanced
cells, zero model/parse errors, and exact reconciliation between event count
and per-run action counts.

## Manuscript

The manuscript is built with a standard TeX Live installation:

```bash
cd paper
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

`IEEEtran.cls` is included in `paper/` so the build does not depend on the
class being installed system-wide.

Font packages: the manuscript uses `times` for Times text with the default
math fonts. `newtxtext`/`newtxmath` are deliberately not used, because they are
absent from a TeX Live basic installation; `mathptmx` is also avoided, because
it requests the `rsfs` script fonts that a basic installation does not ship,
which makes `\times` fail to typeset.

## Verification

```bash
pdfinfo main.pdf | grep '^Pages:'                 # must be <= 6
pdffonts main.pdf                                 # every font must be embedded
pdftotext main.pdf - | grep -niE '<author names>' # must return nothing
grep -c 'Overfull' main.log                       # must be 0
grep -ci 'undefined' main.log                     # must be 0
```

The double-blind submission PDF is copied from `paper/main.pdf` only after
page-count, page-size, font-embedding, citation, anonymity, and visual checks
pass.
