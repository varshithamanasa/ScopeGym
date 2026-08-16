# IEEE Paper Writing Spec: Lessons Learned

> A comprehensive checklist and guidelines for writing IEEE conference/journal papers.
> Based on lessons learned from research paper projects.

---

## Phase 1: Pre-Writing Preparation

### 1.1 Experimental Results First
- [ ] **Run all experiments BEFORE writing**
- [ ] Save results to a structured file (`results.md` or JSON)
- [ ] Include: mean, std, p-values, sample sizes
- [ ] All numbers in paper will reference this single source of truth

### 1.2 Gather References Early
**Process:**
1. Search Google Scholar, IEEE Xplore, arXiv for related work
2. Download PDFs to a `papers/` folder
3. Create `.txt` summaries of key papers
4. Extract: authors, year, method, dataset, results, limitations

**Reference Verification Checklist:**
- [ ] Every reference has a valid DOI (except web resources)
- [ ] DOIs resolve correctly (test with doi.org/YOUR_DOI)
- [ ] BibTeX entries are complete (author, title, year, venue)
- [ ] Use official venue names (not abbreviations)

### 1.3 Create Source of Truth Files
```
project/
├── results.md           # All experimental numbers
├── papers/              # Reference PDFs and summaries
├── ieee_paper/
│   ├── main.tex
│   ├── references.bib
│   └── figures/
├── overleaf.tex         # Copy for Overleaf (sync with main.tex)
└── data/                # Datasets
```

---

## Phase 2: Writing Guidelines

### 2.1 Academic Tone (Avoid AI-Sounding Language)

**❌ Avoid:**
- "significantly" (unless statistically)
- "novel", "innovative", "cutting-edge"
- "powerful", "robust", "comprehensive"
- "interestingly", "importantly"
- "it is worth noting that"
- "This is crucial because"
- Em-dashes (---) for parenthetical remarks
- Avoid unnecessary bold words. Use only where they are required.

**✅ Use Instead:**
- Precise technical terms
- Direct statements
- Semicolons or commas for asides
- "We observe that..." instead of "Interestingly..."
- Numbers and evidence instead of superlatives

**Example Fixes:**
```
❌ "Our novel approach significantly outperforms..."
✅ "Our approach improves Macro-F1 by 9.6pp (p=0.004)."

❌ "This is a powerful technique---one that works well."
✅ "This technique achieves 81.8% Top-5 accuracy."
```

### 2.2 Sentence-Level Transitions

**Use transition words/phrases for flow:**

| Purpose | Transition Words |
|---------|-----------------|
| Adding | Additionally, Furthermore, In addition, Moreover |
| Contrasting | However, In contrast, Nevertheless, Although |
| Cause/Effect | Therefore, Consequently, As a result, Thus |
| Sequencing | First, Second, Finally, Subsequently |
| Clarifying | Specifically, In particular, That is, Namely |
| Summarizing | In summary, Overall, To summarize |

**Example Improvements:**
```
❌ "MLE gives zero probability. Smoothing fixes this."
✅ "MLE assigns zero probability to unseen transitions. To address this, we apply smoothing."

❌ "The model achieves 84% accuracy. Macro-F1 is only 15%."
✅ "The model achieves 84% accuracy; however, Macro-F1 is only 15%."
```

### 2.3 Section-by-Section Consistency

**Each section must be consistent with previous sections:**

| Check | What to Verify |
|-------|----------------|
| Abstract → Introduction | Same problem statement, same key numbers |
| Introduction → Related Work | Claims about gaps should match literature review |
| Related Work → Methodology | Limitations discussed should motivate your method |
| Methodology → Experiments | Same dataset size, same model names, same parameters |
| Experiments → Discussion | Results interpretation matches actual numbers |
| Discussion → Conclusion | Key findings restated accurately |

**Common Mistakes:**
- Different random seed numbers in different sections
- Different model names (e.g., "Baseline" vs "MLE Markov" vs "Baseline MLE")
- Different dataset sizes or split ratios
- Different percentage values (rounding inconsistently)

### 2.4 Naming Consistency
**Use consistent model names throughout:**
- Pick ONE name per model and use it everywhere
- Table headers, figure legends, Key Findings, and text must match
- Example: If table says "Smoothed Markov", figures should say "Smoothed Markov" (not "Smoothed (Ours)")

### 2.5 Number Verification

**Every number MUST appear in results.md first.**

| Type | Format | Example |
|------|--------|---------|
| Accuracy | X.X% ± Y.Y% | 84.1% ± 0.7% |
| p-values | p=0.XXX or p<0.XX | p=0.004 or p<0.01 |
| Counts | Integer | 682 sequences |
| Percentages | X.XX% | 1.39% |

**Rounding Rules:**
- Accuracy: 1 decimal place
- p-values: 3 decimal places
- Percentages in text: 1-2 decimal places

### 2.6 Statistical Rigor for Quantitative Papers

**Essential Elements:**
1. **Multiple Random Seeds** - Run experiments with 5+ seeds (e.g., 42, 123, 456, 789, 1024)
2. **Report Mean ± Std** - Show variance, not just single-run results
3. **Statistical Tests** - Prove differences aren't due to chance
4. **Effect Sizes** - Report magnitude, not just significance

**Which Test to Use:**

| Scenario | Test | When |
|----------|------|------|
| Two models, same test sets | **Paired t-test** | Comparing Model A vs B on same data |
| Two models, different data | Unpaired t-test | Different test sets |
| Multiple models | ANOVA + post-hoc | 3+ models to compare |
| Non-normal data | Wilcoxon signed-rank | When assumptions violated |

**Reporting Format:**
```
✅ "Smoothed Markov improves Macro-F1 by 9.6pp over Baseline 
    (15.5% vs 5.9%, paired t-test, n=5, p=0.004)."

✅ "All differences are statistically significant 
    (paired t-test, α=0.05)."

❌ "Our method is better." (no numbers or test)
```

**What to Report:**
- Sample size (n=5 seeds, N=682 sequences)
- Test type (paired t-test)
- Significance level (α=0.05)
- p-value (p=0.004 or p<0.01)
- Effect size or absolute improvement (+9.6pp)

**Common Mistakes:**
- ❌ Claiming significance without running tests
- ❌ Using unpaired test when paired is appropriate
- ❌ Not reporting sample size
- ❌ Cherry-picking single best run instead of mean

---



## Phase 3: Responding to Reviewer Comments

### 3.1 Addressing Common Reviewer Concerns

| Concern | How to Address |
|---------|----------------|
| Hyperparameter sensitivity | Add sensitivity analysis table |
| Limited baselines | Add more baseline models (e.g., Kneser-Ney for NLP-based methods) |
| Model assumptions | Add paragraph explaining the assumption and any extensions |
| Missing future directions | Add specific items to Future Work section |
| Section flow issues | Add introductory sentences, use bold inline headers |

### 3.2 Response Letter Structure
```markdown
# Response to Reviewer Comments

## Reviewer Comment 1: [Title]
**Reviewer's Question:** [Quote or summarize]

**Our Response:** [Explanation of changes]

**Changes Made:**
- Added Table X showing [specific analysis]
- Updated Section Y with [specific text]
- Modified Figure Z to include [specific addition]

**Location in Manuscript:** Section X.Y, page N
```

### 3.3 Tracking Reviewer Comments
Create a `reply.md` file with:
- [ ] Each reviewer comment listed
- [ ] Status: TODO, IN PROGRESS, DONE
- [ ] Specific changes made for each

---

## Phase 4: LaTeX Formatting

### 4.1 Common LaTeX Issues

| Issue | Solution |
|-------|----------|
| Overfull hbox (table) | `\resizebox{\columnwidth}{!}{...}` |
| Overfull hbox (equation) | Break equation or shorten notation |
| Undefined references | Run pdflatex 3x after bibtex |
| Missing citations | Check .bib file for typos |
| Two-column figure | Use `\begin{figure*}...\end{figure*}` |
| Missing space before citation | Add space: `text \cite{key}` not `text\cite{key}` |

### 4.2 Compilation Command
```bash
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

### 4.3 Check for Warnings
```bash
grep -c "Overfull" main.log    # Should be 0
grep "undefined" main.log       # Should be empty
grep "Citation" main.log        # Check for missing cites
```

### 4.4 Section Transitions
**Good transitions between subsections:**
- Add introductory sentence at start of Results: "We evaluated [models] across [N] random seeds..."
- Add introductory sentence at start of Limitations: "We acknowledge several limitations..."
- Use bold inline headers for sub-points within paragraphs

---

## Phase 5: Pre-Submission Checklist

### 5.1 Content Verification
- [ ] All numbers in Abstract match Tables
- [ ] All numbers in Conclusion match Results
- [ ] All figure captions match figure content
- [ ] All table captions are accurate
- [ ] Method names consistent throughout (tables, figures, text)
- [ ] Dataset size consistent throughout
- [ ] Statistical tests reported correctly (test type, p-value, α level)

### 5.2 Reference Verification
- [ ] All citations in text have corresponding .bib entries
- [ ] All .bib entries are actually cited
- [ ] DOIs work (spot check 5-10)
- [ ] Author names correctly formatted
- [ ] Venue names are official
- [ ] Citation placement correct (space before `\cite{}`)

### 5.3 Formatting Verification
- [ ] Zero overfull boxes (or minimal/acceptable)
- [ ] Figures are high resolution
- [ ] Tables fit within column width
- [ ] Page limit respected
- [ ] Font requirements met
- [ ] All files synced (main.tex ↔ overleaf.tex)

### 5.4 Logical Consistency
Read paper section-by-section and ask:
- Does this section logically follow the previous?
- Are claims made here supported by evidence elsewhere?
- Would a reviewer find any contradictions?

### 5.5 AI Disclosure (If Required)
```latex
\section*{Declaration of AI and AI-assisted Technologies in the Writing Process}
During the preparation of this work, the author used [TOOL NAMES] 
to improve the readability and language of the manuscript. After 
using these tools, the author reviewed and edited the content as 
needed and takes full responsibility for the content of the publication.
```

---

## Phase 6: Common Mistakes to Avoid

### 6.1 Fabricated or Unverified Claims
**Mistake:** Writing case study with made-up probability values
**Prevention:** Every claim must trace to experimental output

### 6.2 Inconsistent Experimental Setup
**Mistake:** Methodology says "seed 42" but Experiments uses 5 seeds
**Prevention:** Review experimental setup description in all sections

### 6.3 Overpromising Results
**Mistake:** "Our method significantly outperforms all baselines"
**Prevention:** Use precise language; acknowledge limitations

### 6.4 Missing Statistical Significance
**Mistake:** Claiming improvements without p-values
**Prevention:** Run statistical tests; report p-values for all key comparisons

### 6.5 Poor Figure-Text Alignment
**Mistake:** Figure shows X-axis as "F1 Score" but caption says "Accuracy"
**Prevention:** Triple-check all figure captions against actual figures

### 6.6 Inconsistent Model Naming
**Mistake:** Table says "Smoothed (Ours)" but figure says "Smoothed Markov"
**Prevention:** Pick ONE name per model; search/replace across all files

### 6.7 Missing Citations for Claims
**Mistake:** "Large vocabularies where method X excels" without citation
**Prevention:** Cite source for any specific claim about methods or datasets

### 6.8 Symbol Used Before Definition
**Mistake:** Using M(N), L(d), or lambda in a pipeline overview before defining them in a later subsection
**Prevention:** At first use, add a parenthetical: "M(N) (colony size multiplier, defined in Section IV-B)". The reader should never encounter a symbol without knowing what it means.

### 6.9 Symbol Collision
**Mistake:** Using the same symbol for two different things (e.g., w for both edge weight and circadian weight)
**Prevention:** Before introducing a symbol, grep the paper for existing uses. Each symbol must have exactly one meaning throughout. If collision exists, rename the less-established one.

### 6.10 Result Numbers in Introduction
**Mistake:** Putting specific results (e.g., "175x median ratio", "71.8% of routes") in the Introduction
**Prevention:** Introduction should state contributions qualitatively. Specific numbers belong in the Results/Experimental section. Use phrases like "orders-of-magnitude differences" instead of exact values.

### 6.11 Equation Terms Explained as Symbols Only
**Mistake:** "where M(N) is a colony size multiplier" -- defines the symbol but not why it's in the equation
**Prevention:** Explain each term's biological/physical meaning AND its role: "M(N) scales risk by colony strength; weaker colonies have reduced thermoregulation and suffer disproportionately greater losses"

### 6.12 Undefined Acronyms and Abbreviations
**Mistake:** Using "TDVRP" without spelling it out, or "ND/SD/MT/MN" without full state names
**Prevention:** Spell out every acronym on first use: "Time-Dependent Vehicle Routing Problem (TDVRP)". Write full names for states, organizations, etc. unless they are universally known (e.g., U.S., NASA).

### 6.13 Domain Jargon Without Context
**Mistake:** Using field-specific terms like "SOD, POD, CAT" (enzyme names) without definition in an optimization paper
**Prevention:** Either define domain-specific terms or replace with plain language. Ask: does the reader of THIS paper need these details, or just the conclusion they support?

### 6.14 Equations Overflowing Column Width
**Mistake:** Using `multline` or long equations that spill into the second column in IEEE two-column format
**Prevention:** Test-compile after adding equations. If overflow occurs, use compact notation (define helper terms), `split` inside `equation`, or `\small` font. Never let an equation cross column boundaries.

### 6.15 Incomplete Sentences
**Mistake:** Ending a sentence with a dangling clause like "without weather-informed optimization" that reads as a fragment
**Prevention:** Every sentence must have a complete thought. Read aloud -- if it sounds like it needs "...and so what?" then the sentence is incomplete.

---

## Phase 7: GitHub Repository Preparation

### 7.1 Repository Structure
```
repo/
├── README.md             # Installation, usage, reproduction instructions
├── requirements.txt      # Python dependencies
├── LICENSE              # MIT or Apache 2.0
├── .gitignore           # Exclude __pycache__, venv, large data
├── src/
│   ├── config.py        # Centralized hyperparameters and paths
│   ├── models/          # Model implementations
│   ├── data_pipeline/   # Data processing scripts
│   ├── run_experiments.py
│   └── generate_figures.py
├── data/
│   └── processed/       # Pre-processed data for quick reproduction
└── figures/             # Generated figures
```

### 7.2 README.md Essentials
- Installation instructions (pip install -r requirements.txt)
- Quick start example
- Full reproduction steps
- Results summary table
- Data sources and attribution
- Citation (BibTeX)
- License

### 7.3 Pre-Release Checklist
- [ ] Clean code (remove debug prints, commented code)
- [ ] Requirements.txt tested in fresh environment
- [ ] All paths are relative, not absolute
- [ ] Sensitive data excluded from repo
- [ ] License file present
- [ ] README has reproduction instructions

---

## Phase 8: Review Cycles

### 8.1 Self-Review Passes
1. **Pass 1: Numbers** - Verify all numbers against results.md
2. **Pass 2: Consistency** - Read section-by-section for logic
3. **Pass 3: Naming** - Verify model names match across tables/figures/text
4. **Pass 4: Tone** - Remove promotional language, em-dashes
5. **Pass 5: References** - Verify DOIs and citations
6. **Pass 6: Formatting** - Check compilation warnings
7. **Pass 7: Inline Headers** - Never use `\textbf{Label.} Text...` as a paragraph header. Use `\subsection{}` or flowing prose instead.
8. **Pass 8: Subsection Count** - Keep subsections to 3--4 per section. Merge related subsections if a section has 5+.

### 8.2 Reviewer Anticipation
Ask yourself:
- What would an IEEE reviewer criticize?
- Are all claims supported by evidence?
- Are limitations honestly discussed?
- Is the contribution clearly stated?

---

## Appendix: Useful Resources

### A1: Reference Lookup
- DOI Resolution: https://doi.org/
- IEEE Xplore: https://ieeexplore.ieee.org/
- Semantic Scholar: https://www.semanticscholar.org/
- arXiv: https://arxiv.org/

### A2: LaTeX Templates
- IEEE Conference: IEEEtran.cls
- Overleaf IEEE templates: https://www.overleaf.com/latex/templates/tagged/ieee

### A3: Statistical Tests
- **Paired t-test**: Comparing two models on same test sets across seeds
- **Report**: test type, α level (e.g., 0.05), p-value, sample size (n seeds)

---

## Summary: The Top 23 Lessons

1. **Results first, writing second** - Run experiments before writing
2. **Single source of truth** - All numbers from one results file
3. **Every claim needs evidence** - No fabricated examples
4. **Consistency across sections** - Same names, numbers, seeds
5. **Consistent model naming** - Same names in tables, figures, text
6. **Verify references** - DOIs must resolve
7. **Academic tone** - No promotional language
8. **No em-dashes** - Use semicolons or commas
9. **Check LaTeX warnings** - Zero overfull boxes
10. **Statistical significance** - Report p-values
11. **AI disclosure** - Add if required by venue
12. **Track reviewer comments** - Use reply.md with status tracking
13. **Add transitions** - Introductory sentences for flow
14. **Sync all files** - main.tex and overleaf.tex must match
15. **Prepare reproducible code** - Clean repo with README
16. **Define symbols at first use** - Never let the reader encounter an undefined symbol
17. **No symbol collisions** - Each symbol gets exactly one meaning in the paper
18. **No result numbers in Introduction** - Keep specific numbers in Results section
19. **Explain equation terms' role, not just names** - Why is each term in the equation?
20. **Spell out all acronyms and abbreviations** - TDVRP, state names, org names
21. **Simplify domain jargon for your audience** - Enzyme names don't help optimization readers
22. **Equations must fit column width** - Test-compile, use compact notation if needed
23. **Complete every sentence** - No dangling clauses or fragments