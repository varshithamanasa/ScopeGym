# How to reduce the AI-detection score on the ScopeGym paper

Written Aug 15, 2026, after a Turnitin run returned **71% detected as AI** on the
5-page GAISS submission (submission ID `trn:oid:::1:3627972588`, 3,695 words).

This is a working reference for the camera-ready pass, not for the deadline
submission.

---

## 0. Scope: when this actually matters

| Context | Does the score matter? |
|---|---|
| **GAISS 2026 submission** | **No.** The whole gaiss.info site was read on Aug 15, 2026. There is no AI policy, no disclosure requirement, and no detection step. Zero occurrences of "AI disclosure", "generative AI tool", or equivalent. |
| **Lasell / institutional check** | Yes. The Turnitin run went through `MDSC203 -- Moving Stories: People, Place, and Power_SANDBOX, Lasell University`. |
| **Camera-ready (Sept 15)** | Worth fixing then, with time to verify. |

Do not trade a verified, compiling, anonymized PDF for a lower detector score
under deadline pressure. The score is not a submission requirement.

**Nothing here is about concealment.** The paper openly discloses AI assistance
in the Artifact, Ethics, and AI Assistance section, and that disclosure stays.
The goal is prose that reads in the authors' own voice. Keep the disclosure
sentence exactly as written.

---

## 1. Why this paper scores high

Turnitin highlighted the Abstract, Introduction, and Related Work. The Results
section, which is number-dense and structurally irregular, is far less flagged.
That contrast is the diagnosis: **detectors respond to uniformity, not to
content.**

Three specific patterns in the current text drive the score.

### 1.1 Parallel-chain sentences (worst offender)

Related Work, paragraph 1:

> Cybench evaluates language models on professional capture-the-flag tasks with
> subtask-level scoring [3]. CyberGym scales evaluation to 1,507 real-world
> vulnerabilities across 188 software projects [4]. BountyBench measures
> detection, exploitation, and patching on real bug-bounty systems [6].

Three consecutive sentences, near-identical length, identical
`Subject + verb + object + [cite]` shape. Related Work paragraph 2 does the same
thing across five sentences (ToolEmu / AgentHarm / AgentDojo / ASB / tau-bench).

This is the single strongest machine-writing signal in the paper.

### 1.2 No first person anywhere

`grep -c '\bWe\b' main.tex` returns 0. Human-authored academic writing in this
field uses "we" freely. Its total absence is itself anomalous.

### 1.3 Uniform sentence length

Every sentence was deliberately cut below 30 words. Human technical prose
varies far more: an 8-word sentence next to a 45-word one.

---

## 2. The conflict you need to know about

**The edits that raised this score were deliberate and came from your own style
guides.** They are not mistakes. But they pull in the opposite direction from
detector scores:

| Rule | Source | Effect on AI score |
|---|---|---|
| Split every sentence under ~30 words | `grammar.md` §18.1 (Chad Fenner) | **Raises it** — flattens length variance |
| Prefer "The research/paper/study" over "We" | `grammar.md` §18.2 (Chad Fenner) | **Raises it** — removes human voice marker |
| Add connectors: However, In addition, By contrast | `grammar.md` §5.3 | **Raises it** — formulaic transitions |
| Ban promotional/hedging vocabulary | `prompt.md` §2.1 | **Raises it** — removes idiosyncrasy |

You cannot fully satisfy both. Decide which matters more per venue. For a
conference with no AI policy, follow the style guides. For an institutional
check, relax §18.1 and §18.2 selectively.

**Discuss §18.2 with Chad before reverting it** — it is his stated preference,
and quietly undoing a coauthor's review note is worse than a detector score.

---

## 3. Concrete edits, highest impact first

### Fix 1 — break the parallel chains (biggest single win)

Combine, subordinate, and vary. Before:

> Cybench evaluates language models on professional capture-the-flag tasks with
> subtask-level scoring [3]. CyberGym scales evaluation to 1,507 real-world
> vulnerabilities across 188 software projects [4]. BountyBench measures
> detection, exploitation, and patching on real bug-bounty systems [6].

After:

> Cybench scores language models on professional capture-the-flag tasks, with
> subtask-level credit [3]. Scale came later: CyberGym spans 1,507 real
> vulnerabilities drawn from 188 projects [4], and BountyBench goes further
> still, paying out detection, exploitation, and patching across live bug-bounty
> systems [6].

Same claims, same citations, same facts. Lengths now 14 / 38 words instead of
16 / 15 / 14.

Apply the same treatment to the five-benchmark chain in Related Work paragraph 2.

### Fix 2 — restore first person in three places

- Abstract: `This paper introduces ScopeGym` → `We introduce ScopeGym`
- Abstract: `The study evaluated two local language models` → `We evaluated two local language models`
- Introduction: `The paper makes three contributions` → `We make three contributions`

Three edits, no factual change. (These reverse §18.2 — see the warning above.)

### Fix 3 — vary sentence length deliberately

Target a mix: some sentences under 10 words, some over 35. The Limitations
paragraph and Discussion are the safest places to do this, because they contain
no reported statistics.

### Fix 4 — thin the formulaic connectors

Currently added at paragraph and clause starts: "However," "In addition," "By
contrast." Keep roughly half. Replace others with subordination, a semicolon, or
nothing.

### Fix 5 — leave the Results section alone

It is the least-flagged part of the paper precisely because it is dense with
counts and intervals. **Never** edit a sentence containing a number for stylistic
reasons. Every figure in Results was verified against `outputs/*/runs.csv`.

---

## 4. Hard constraints while editing

- **Do not change any number.** 17/20, 13/20, 43/60, 41/60, 56/60, 28/60, 12/41,
  11/41, 14/60, 10/60, 24/120, 96/120, 54 denials, 461 events, 120 runs.
- **Do not touch citations.** 19 cited, 19 in `references.bib`, all verified.
- **Do not remove the AI-assistance disclosure.**
- **Do not re-introduce author identity.** The paper is double-blind.
- **Do not exceed 6 pages.**

---

## 5. Verification loop after any edit

```bash
cd paper
pdflatex -interaction=nonstopmode main.tex && bibtex main \
  && pdflatex -interaction=nonstopmode main.tex \
  && pdflatex -interaction=nonstopmode main.tex

pdfinfo main.pdf | grep '^Pages:'                      # must be <= 6
grep -c 'Overfull' main.log                            # must be 0
grep -ci 'undefined' main.log                          # must be 0
pdftotext main.pdf - | grep -niE 'varshitha|lasell|vmanjunath|dakota state'   # must be empty
pdffonts main.pdf | tail -n +3 | awk '$5!="yes"'       # must be empty
```

Then re-check that the numbers listed in §4 still appear:

```bash
grep -oE '(17/20|13/20|41/60|43/60|56/60|28/60|12/41|11/41|14/60|10/60|24/120|96/120|461|120 runs)' main.tex | sort | uniq -c
```

---

## 6. Realistic expectations

A careful pass on Fixes 1–4 should move 71% into roughly the 40–55% range. It
will not reach single digits, and chasing that is not worth it:

- Turnitin's own disclaimer, printed in your report, states the assessment "may
  misidentify writing that is likely human generated as AI generated" and
  "should not be used as the sole basis for adverse actions."
- Technical academic prose scores high regardless of authorship. Structured
  argumentation, dense citation, and controlled vocabulary are the register.
- The paper is honestly AI-assisted and says so. A moderate score is consistent
  with the disclosure rather than in conflict with it.

The objective is prose that sounds like the authors, not a number that satisfies
a classifier.

---

## 7. If someone asks about the score

The defensible position, in order:

1. The work is original: the experiment, the 120 runs, the 461 logged events,
   and every reported statistic were produced by the authors' own harness and
   are reproducible from the artifact.
2. AI assistance is disclosed in the manuscript, per the venue's policy and the
   authors' judgment.
3. AI detection is probabilistic, vendor-acknowledged as error-prone, and not a
   finding of misconduct.
4. The raw data, analysis script, and event log are available for inspection.

Point 1 is the one that matters. The research is the authors'.
