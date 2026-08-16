# Comprehensive Grammar & Style Guide for Q1 IEEE Journal Writing

**Derived from:** 48 reference papers across bee biology, transport logistics, circadian rhythms, stress physiology, vehicle routing, and USDA policy reports.
**Target venue:** IEEE Transactions on Intelligent Transportation Systems (T-ITS)
**Generated:** March 2026

---

## 1. CITATION RULES

### 1.1 IEEE Format: Numbered Brackets
Since IEEE uses numbered brackets `[1]`, `[2]`, `[3-5]`, all rules below are adapted to this format.

### 1.2 Placement Rules

**Rule 1: Citations go at the END of the claim, never mid-sentence.**
- GOOD: "Long-distance transport exposes colonies to temperature extremes, humidity fluctuations, and vibration [5], [12]."
- BAD: "Long-distance transport [5] exposes colonies to temperature extremes."

**Rule 2: Use narrative citations ONLY when the specific author's contribution is the point.**
- Narrative: "Melicher et al. [5] demonstrated that colony size is the strongest predictor of transport survival."
- Parenthetical (default): "Colony size is the strongest predictor of transport survival [5]."
- Use narrative ~25% of the time; parenthetical ~75% (observed ratio across all papers).

**Rule 3: Stack multiple citations for consensus claims.**
- "Annual colony losses remain 30--40\% [3], [7], [15]."
- "Transport stress affects physiology [5], [12], behavior [9], and lifespan [6]."

### 1.3 Citation Density by Section

| Section | Citations/Paragraph | Why |
|---------|-------------------|-----|
| Introduction | 3-6 | Heavy grounding in prior work |
| Methods | 1-2 | Only for referenced protocols/data sources |
| Results | 0-1 | YOUR data, not others' |
| Discussion | 3-5 | Heavy comparison to prior work |
| Conclusion | 1-2 | Only for key framing references |

**Source papers:** Melicher uses 2-4/paragraph in Intro; Simone-Finstrom uses 3-5 in Discussion; Li et al. uses 0 in Results. All follow this pattern consistently.

### 1.4 When NOT to Cite
- Do not cite your own computed results (they come from your model, not literature)
- Do not cite for universally known facts ("Bees are social insects")
- Do not cite in the middle of a mathematical derivation

---

## 2. SENTENCE STRUCTURE

### 2.1 Length Targets

| Section | Target (words) | Source Pattern |
|---------|---------------|---------------|
| Topic sentences | 10-18 | Mardan: "Adult workers survived well from about 26 to 36 C." |
| Results statements | 15-25 | Simone-Finstrom: "We detected a significant decrease in lifespan." |
| Methods descriptions | 20-35 | Melicher: "Internal hive temperature was recorded every hour during shipping." |
| Discussion analysis | 20-40 | Simone-Finstrom: "While a difference of only 1 day may seem relatively trivial, it represents approximately 5% of the total lifespan." |

**Rule: Alternate short declarative sentences with longer compound ones.** Never write 3+ long sentences in a row.

### 2.2 Active vs. Passive Voice

| Section | Active | Passive | Rule |
|---------|--------|---------|------|
| Abstract | 60% | 40% | Lead with active for your contributions |
| Introduction | 70% | 30% | Active for framing, passive for background facts |
| Methods | 25% | **75%** | Passive dominates: "Routes were generated via..." |
| Results | 45% | 55% | Mix: passive for computed outputs, active for findings |
| Discussion | 65% | 35% | Active for interpretation: "Our results demonstrate..." |
| Conclusion | 70% | 30% | Active for claims: "We formulated..." |

**Examples from papers:**
- Active (Discussion): "We found that colonies experienced cold stress during shipping." (Melicher)
- Passive (Methods): "Bees were maintained according to standard beekeeping techniques." (Simone-Finstrom)
- Active (Conclusion): "Transportation stress should be considered an important component." (Melicher)

### 2.3 First Person Rules
- Use **"We"** for multi-author papers: "We found," "We conclude," "Our results"
- **Never** use "the authors" -- use "we" or passive construction
- **Never** use "I" in journal papers (only in theses -- see Andress)
- In Methods for IEEE: prefer passive ("Routes were generated") over "We generated routes"

### 2.4 Sentence Variety Patterns

**Pattern A: Short declarative + long analytical**
> "Temperature had the highest effect. This finding, consistent with earlier field observations across multiple subspecies, suggests that thermal tolerance may be the primary constraint on transport survival during winter months."

**Pattern B: Result + (statistic) + (figure reference)**
> "The maximum health loss reached 80.55% for the Seattle-to-Presque Isle route (January 12, 2024; Fig. 3)."

**Pattern C: Comparison with "whereas" or "while"**
> "A significant difference was found between A. cerana and A. mellifera at 35C, whereas no significant differences were found among the other treatments (Table 1)." (Li et al.)

**Pattern D: Colon-introduced enumeration**
> "Three contributions emerge. First, departure timing is the dominant variable. Second, intermediate stops benefit 71.8% of routes. Third, the polar vortex concentrated worst-case outcomes."

---

## 3. HEDGING LANGUAGE

### 3.1 Hedging Hierarchy (weakest to strongest)

| Strength | Phrase | Use When | Source |
|----------|--------|----------|--------|
| Very soft | "may," "might," "could," "possibly" | Speculative mechanisms | Reitmayer: "diesel exposure may be disrupting cellular stress machinery" |
| Soft | "suggests," "appears to," "indicates," "is consistent with" | Interpreting results | Simone-Finstrom: "Our results suggest that worker bees exhibit increased stress" |
| Moderate | "our results show," "we found," "reveals" | Reporting direct findings | Melicher: "We found that colonies experienced cold stress" |
| Strong | "demonstrates," "confirms," "establishes" | Well-supported conclusions | Simone-Finstrom: "provides the first comprehensive evidence that" |
| **NEVER** | "proves," "proof" | **Never used in any of the 48 papers** | -- |

### 3.2 Hedging Templates by Context

**For speculative claims:**
- "It is possible that X, which may in turn affect Y." (Ahn)
- "One possible explanation is that..." (Kovac)
- "This could be attributed to..." (Bordier)

**For results interpretation:**
- "These results suggest that..." (Li)
- "This finding is consistent with..." (Rodriguez-Zas)
- "Our data indicate that..." (Simone-Finstrom)

**For qualified conclusions:**
- "It is not possible from the current work to conclusively link..." (Reitmayer)
- "We can only state that there was a significant positive correlation." (Reitmayer)

**For acknowledging uncertainty:**
- "We do not know whether X is the result of Y or Z, or both." (Kovac)
- "Whether such changes deleteriously affect foraging is currently unknown." (Lusebrink)

**For model-based papers (YOUR paper):**
- Use "demonstrates" and "reveals" for computed outputs
- Use "suggests" or "indicates" for ecological interpretations
- Use "is consistent with" when comparing model output to literature values
- Use "may be attributed to" for mechanistic explanations

### 3.3 Hedging Calibration Rules
1. **Never claim "proves"** -- use "demonstrates" at strongest
2. **Always hedge mechanism proposals** -- use "may," "possibly," "presumably"
3. **Use double-hedging for speculative chains** -- "It is possible that X, which may in turn affect Y"
4. **Admit failed predictions honestly** -- "Thus, we reject our hypothesis that..." (Tan/ken)
5. **Be declarative for YOUR computed results** -- "The maximum health loss is 80.55%" (no hedging needed for a number your model produced)
6. **Hedge the INTERPRETATION, not the DATA** -- "80.55% health loss suggests severe risk" (hedge is on "suggests severe risk," not on the number)

---

## 4. RESULTS PRESENTATION

### 4.1 Number Introduction Patterns

**Pattern A: Finding + (statistic) + (figure reference)**
> "Colony treatment (X2 = 11.39, p = 0.0007) and trial (X2 = 21.11, p < 0.0001) significantly impacted worker lifespan." (Simone-Finstrom)

**Pattern B: Value with context and route**
> "The maximum health loss reached 80.55% (Seattle to Presque Isle, January 12, 2024, hour 19)."

**Pattern C: Comparison with "whereas"**
> "Mean best-case health loss stays 0.31--0.72%, whereas mean worst-case varies 21--30% with winter severity."

**Pattern D: Fold-change emphasis**
> "The median risk ratio between worst-case and best-case departures is 175x across all 15,912 route-year pairs."

**Pattern E: Range + extrema**
> "Results showed minimum and maximum temperatures of 12.4C and 34.7C inside queen shipment boxes (average 25.0 +/- 3.1C)." (Rousseau)

**Pattern F: Threshold-based reporting**
> "At all humidities below 50% R.H., all eggs that had shown initial embryonic development were completely shrivelled." (Doull)

### 4.2 Statistical Reporting Conventions
- **Inline, never on separate lines**: "(P < 0.05; n = 21; F = 131.44)"
- **ANOVA**: "F1,18 = 50.05, P < 0.0001" (Tan)
- **Chi-square**: "X2 = 11.39, p = 0.0007" (Simone-Finstrom)
- **Correlation**: "(df = 38, r = 0.77, P < 0.001)" (Reitmayer)
- **Non-significant results**: report them too -- "p > 0.5" or "ns"
- **For computational papers**: report computed values directly without p-values (exhaustive search = no sampling error)

### 4.3 Contextualizing Results
**Always explain WHY a number matters, not just WHAT it is:**
> "While a difference of only 1 day may seem relatively trivial, it represents approximately 5% of the total lifespan of an adult worker and maybe up to 20% of their foraging lifespan." (Simone-Finstrom)

> "The median risk ratio of 175x means the same route, same truck, same cargo -- only the departure time changes."

### 4.4 Contextualizing Small Effects
When an effect seems small, justify its significance:
- Frame as percentage of total: "represents ~5% of total risk reduction"
- Frame as practical impact: "even 0.37% improvement, applied across 2 million colonies, prevents thousands of colony losses"
- Compare to cost of implementation: "achievable with no infrastructure changes"

---

## 5. TRANSITION PATTERNS

### 5.1 Between Paragraphs

| Type | Connectors | Source Example |
|------|-----------|----------------|
| Causal | "Therefore," "Thus," "As a result," "Consequently," "Hence" | "Therefore, these findings indicate that social inhibition was effective." (Meshi) |
| Contrast | "However," "By contrast," "Unlike," "In contrast to," "Nevertheless" | "However, the results were very heterogeneous." (Martinez-Lopez) |
| Addition | "In addition," "Furthermore," "Moreover," "Additionally" | "Furthermore, studies examining the impact rarely include a control group." (Alger) |
| Validation | "Consistent with," "Similarly," "As expected," "In agreement with" | "Consistent with earlier studies, transcripts oscillated in foragers." (Rodriguez-Zas) |
| Concession | "Although," "While," "Despite," "Nonetheless" | "Although migratory colonies are implicated as disease sources..." (Alger) |
| Reversal | "However, unlike our previous understanding," | "However, unlike our previous understanding, high humidity can also adversely affect bees." (Li) |

### 5.2 Between Sections
- **Methods to Results**: "Using this method, we found..." (Meshi)
- **Results to Discussion**: "The major finding from this study was that..." (Ahn)
- **Discussion to Conclusion**: "Taken together, the studies reviewed above show that..." (Eban-Rothschild)
- **Intro to Methods**: "To address this, we developed..." or "To answer these questions, we..."

### 5.3 Transition Rules
1. **Every paragraph must connect to the previous one** -- no orphan paragraphs
2. **Use a variety of connectors** -- don't repeat "However" three paragraphs in a row
3. **Topic sentences should bridge** -- restate the link to the prior point before making the new one
4. **Never start a paragraph with a citation** -- start with YOUR claim, then cite

---

## 6. FIGURE AND TABLE REFERENCES

### 6.1 IEEE Format Rules
- Use "Fig." (abbreviated) in running text, "Figure" in captions
- Use Roman numerals for tables in IEEE: "TABLE I," "TABLE II"
- Always reference BEFORE the reader encounters the figure in the document flow

### 6.2 In-Text Reference Patterns

**Parenthetical (most common, ~80%):**
> "The risk matrix reveals clear geographic structure (Fig. 5)."

**Narrative (for introducing key visuals, ~20%):**
> "Fig. 3 shows the seasonal distribution of worst-case departures."

**Embedded with data:**
> "The maximum health loss reached 80.55% (Fig. 4, January 2024 panel)."

### 6.3 Caption Conventions
- **Descriptive and self-contained**: Reader should understand figure without main text
- **Include key numbers**: "Median improvement 0.37%, maximum 5.88%"
- **Sub-panel labeling**: "(a)", "(b)", "(c)" with description of each
- **No analysis in captions** -- describe what is shown, not what it means

---

## 7. OPENING PATTERNS

### 7.1 Abstract Opening (3 patterns observed)

**Pattern A: Broad importance + specific problem + contribution (most common)**
> "Each year, over two million managed honeybee colonies are transported across the United States to support crop pollination. Despite this scale, no quantitative tools exist for weather-based optimization."

**Pattern B: Paradox or contrast + knowledge gap**
> "Honey bee workers care for the brood around the clock without circadian rhythmicity, but then they forage outside with strong circadian rhythms." (Rodriguez-Zas)

**Pattern C: Direct problem statement**
> "The causes underlying the increased mortality of honeybee colonies observed over the past decade remain unclear." (Horn)

### 7.2 Introduction First Sentence Rules
**Always start with an ESTABLISHED FACT or BROAD CONTEXT, never with methodology.**
- GOOD: "Over two million managed honey bee colonies are transported annually." (broad fact)
- GOOD: "The ecological success of honey bees depends in part on their ability to thermoregulate." (Tan)
- BAD: "We developed a two-layer optimization framework." (methodology -- save for contribution statement)

### 7.3 Gap Identification Templates
Use these to signal novelty (transition from literature review to your contribution):
- "However, there is scarce information about..." (stress1)
- "...has currently received minimal investigation." (Simone-Finstrom)
- "Little is known, however, about..." (Meshi)
- "To date there have been no studies rigorously addressing whether..." (Simone-Finstrom)
- "We understand little how..." (Ahn)
- "A unified methodology...is still lacking." (Kostrub)
- "No prior work combines..." (YOUR paper's key gap statement)

### 7.4 Contribution Statement (end of Introduction)
For IEEE, use an explicit numbered list:
> "The contributions of this paper are: 1) a physiologically grounded risk model...; 2) exhaustive departure timing optimization...; 3) multi-year empirical validation..."

---

## 8. DISCUSSION ARCHITECTURE

### 8.1 Standard Discussion Paragraph Structure (5-step)

1. **Restate major finding** (1-2 sentences, no hedging)
   > "The major finding from this study was that HPG sizes were consistently and negatively affected by transportation." (Ahn)

2. **Compare to prior work** (2-4 sentences, use "consistent with" / "in contrast to")
   > "Previous studies have shown that consumption rate of protein diets had a positive correlation with the development of HPG." (Ahn)
   > "Our findings are consistent with / in contrast to..."

3. **Propose mechanism** (hedged, 2-3 sentences)
   > "...possibly due to their inability to find or consume pollen normally. It is also possible that trophallaxis was adversely affected." (Ahn)

4. **Acknowledge limitations** (1-2 sentences)
   > "Our experimental hives were trucked only short distances (~1 hour) compared to the typical migratory experience." (Simone-Finstrom)

5. **Bridge to next point or future work** (1 sentence)
   > "A laboratory proxy for long distance transportation is needed to further dissect the detailed mechanisms." (Ahn)

### 8.2 Comparison Templates

**Confirming prior work:**
- "Our results are consistent with [prior work], which showed..."
- "This finding confirms the observations of Smith et al. [5]."
- "Consistent with earlier studies [3], [7], we found..."

**Contradicting prior work:**
- "In contrast to [Author] [5], we found..."
- "Unlike [prior finding] [3], our data show..."
- "Thus, we reject our hypothesis that..." (Tan -- rare but powerful)

**Extending prior work:**
- "While Smith et al. [5] showed X for a single route, we extend this to 2,652 routes."
- "Building on [prior work] [3], our analysis reveals..."
- "Previous studies focused on [scope]; we expand to [broader scope]..."

### 8.3 How to Discuss Null or Unexpected Results
McAfee et al. provides the gold standard -- enumerate alternative explanations:
> "There are several potential explanations for this null result, none of which are necessarily mutually exclusive: 1) previous studies were not conducted blindly...2) our samples could be contaminated...3) not all subjects are equally sensitive...4) not all responses are equally sensitive."

---

## 9. LIMITATION ACKNOWLEDGMENT

### 9.1 Rules
1. **Embed limitations throughout Discussion** -- don't isolate in a single paragraph
2. **Frame as opportunities**, not failures
3. **Quantify scope**, don't just state existence
4. **Always pivot to future work**

### 9.2 Templates

**Scope limitation:**
> "Our study concentrated on medium colonies (8 frames). Weak colonies (M = 3.0) experience approximately 3x higher risk; optimal timing for medium colonies may not adequately protect weak ones."

**Methodological limitation:**
> "Our experimental hives were trucked only short distances (~1 hour) compared to the typical migratory experience, where they can remain confined on a truck for 12-72 hours." (Simone-Finstrom)

**Model limitation (for YOUR paper):**
> "The piecewise quadratic form is a modeling choice designed to capture the qualitative shape of physiological stress responses, not an empirically fitted dose-response curve."
> "Health loss percentages should be interpreted as relative risk rankings, not validated mortality predictions, until confirmed by field measurements."

**Pivot to future work:**
> "A laboratory proxy for long distance transportation is needed to further dissect the detailed mechanisms." (Ahn)
> "Further experiments with detailed video analysis will be needed to decide..." (Kovac)

---

## 10. CONCLUSION PATTERNS

### 10.1 Standard Structure

1. **Restatement of findings** (often numbered):
   > "Three contributions emerge. First,... Second,... Third,..."

2. **Practical implication:**
   > "Transportation stress should be considered an important component of annual colony losses which can be mitigated with improved management strategies." (Melicher)

3. **Broader significance:**
   > "Understanding the consequences of these events should help us better manage the honey bees." (Wang/qing)

4. **Future work (final sentence):**
   > "Future research needs to deepen our understanding of these fascinating behaviors." (Eban-Rothschild)

### 10.2 Closing Sentence Templates
- "Understanding [X] should help us better manage [Y]."
- "[Finding] should be considered an important component of [broader issue] which can be mitigated with [approach]."
- "The framework generalizes to any [scope] with available [data] -- no [retraining/recalibration] is needed."
- "Our results will be valuable in discussing [topic] and highlight the necessity for [next step]."
- "The framework is origin-destination agnostic: extending to additional hubs requires only weather data at new waypoint coordinates."

---

## 11. MULTI-STRESSOR INTERACTION LANGUAGE

### 11.1 Cascading Effects (Horn et al. is the gold standard)
- "Forage availability affected colonies via cascading effects on queen's egg-laying rate, reduction of brood, pollen debt, lack of workforce, and reduced foraging activity."
- Use "cascading effects," "knock-on effects," "chain of consequences" rather than simply listing stressors.

### 11.2 Sub-Critical Compounding
- "A combination of stressors that are individually at sub-critical levels may still put a colony at severe risk." (Horn)
- "Their simultaneous occurrence can cause the multistress phenomenon." (Nicewicz)

### 11.3 Interaction > Main Effects
Report interactions as the central finding, with main effects as context:
> "No significant overall effects were detected for age. However, significant interactions were detected for 'environment x season' (F = 8.19, p < 0.005)." (Simone-Finstrom)

### 11.4 Masking and Offsetting
> "Resource availability may mask these effects later in life." (Simone-Finstrom)
> "Food scarcity had an even larger impact; some detrimental effects may be alleviated by greater forage abundance."

---

## 12. EQUATION AND FORMULA PRESENTATION (IEEE)

### 12.1 Introduction Pattern
Always introduce with a context sentence, then display equation, then define variables:
> "The composite hourly risk is computed as:
> [Equation (1)]
> where alpha_T is the temperature weight coefficient..."

### 12.2 Rules
- Number all displayed equations: (1), (2), etc.
- Reference as "(1)" in text, not "Equation 1"
- Define EVERY variable after first use
- Use "where" (lowercase) after display equation, not "Where"
- Key equations (cost function, optimization objective) should be numbered and referenced

---

## 13. ANTI-PATTERNS TO AVOID

These violations were **never observed** across 48 papers:

1. **Never start a sentence with a number** -- write "A total of 2,652 routes" not "2,652 routes were..."
2. **Never use "prove" or "proven"** -- use "demonstrate," "show," "establish"
3. **Never use first person in Methods** for IEEE -- use passive voice
4. **Never use colloquialisms** -- no "a lot of," "huge," "game-changer," "basically"
5. **Never present results without context** -- always compare to prior work or baseline
6. **Never end Discussion without future work** -- every limitation needs a "further research" pivot
7. **Never use "very" or "extremely"** -- quantify instead (use "3.0x" not "very much higher")
8. **Never introduce acronyms without definition** -- "Hours of Service (HOS)" on first use
9. **Never cite a single study as definitive** -- use multiple citations for consensus claims
10. **Never conflate correlation with causation** -- use "associated with," not "caused by"
11. **Never start a paragraph with a citation** -- start with YOUR claim, then cite
12. **Never use "we believe"** (too informal) -- use "our results indicate" or "the data suggest"
13. **Never write three consecutive long sentences** -- alternate with a short declarative
14. **Never use promotional language** -- no "dramatically improves," "groundbreaking," "hard-to-replicate advantage" (see Kostrub as anti-model)

---

## 14. QUICK REFERENCE: PHRASE BANK

### Problem Framing
- "X plays a crucial role in Y, [quantified impact]."
- "Despite the [importance/requirement] of X, we understand little how X affects Y."
- "Concerns have been raised about whether X causes Y; however to date there have been no studies rigorously addressing this."
- "No prior work combines [domain A] with [domain B] for [application]."

### Methodology
- "To address this, we [developed/implemented/applied] a [method/framework]."
- "For each [unit], we exhaustively evaluate all [scenarios]."
- "The [model/framework] was calibrated against [benchmark/industry data]."

### Results
- "Across [N] [units] and [M] years, [finding] is the dominant [factor]."
- "The maximum [metric] was [value] ([route/condition]; [date/time])."
- "The median [metric] across all [N] pairs is [value]."
- "[X]% of [units] ([count]/[total]) [finding] within [condition]."

### Discussion
- "The operationally significant finding is [X], not the [Y] maximum."
- "Layer 1 captures the large majority of achievable risk reduction; Layer 2 provides incremental improvement."
- "[Heuristic] is broadly correct but [quantification] reveals [nuance]."
- "The concentration of [metric] in a small [subset] has direct operational implications."

### Limitations
- "The model is calibrated against [proxy]; field validation against measured [outcomes] remains for future work."
- "[Parameter] is a modeling choice designed to capture the qualitative shape of [phenomenon], not an empirically fitted [curve]."
- "Health loss values should be interpreted as relative risk rankings, not precise mortality predictions."

### Conclusion
- "[Framework] is origin-destination agnostic; extending requires only [data] at new [locations]."
- "No changes to [infrastructure/compliance/fleet] are required."
- "[Metric] confirms that [optimization] is not an edge-case improvement -- it is relevant for essentially every [unit] in the network."

---

## 15. PAPER-SPECIFIC STYLE MODELS

### Best Models for YOUR Paper (ranked by relevance)

| Aspect | Best Model Paper | Why |
|--------|-----------------|-----|
| Overall structure | Simone-Finstrom (2016) | Best Discussion flow, limitation handling, contextualizing small effects |
| Results presentation | Melicher (2019) | Clean statistical reporting, practical conclusions |
| Temperature data | Kovac (2014) | Most precise threshold reporting, systematic comparison to prior work |
| Multi-stressor framing | Horn (2016) BEEHAVE | Cascading effects, sub-critical interactions, tipping points |
| Limitations section | McAfee (2019) | Enumerates alternative explanations, self-critical |
| Transportation data | Bond (2021) USDA | Contextualizes distances, pairs % with absolutes |
| Dose-response curves | Stefanec (2021) | Mathematical models for vibration response, threshold definitions |
| Hedging calibration | Simone-Finstrom (2016) | Balances confidence with appropriate uncertainty |
| Opening/closing | Melicher (2019) | Clean funnel intro, practical conclusion |
| **Anti-model** | **Kostrub (2025)** | **Too promotional, insufficient hedging, no stats -- do NOT emulate** |

---

---

## 16. IEEE T-ITS VENUE-SPECIFIC CONVENTIONS

**Source:** 3 IEEE T-ITS papers (Vol. 26, No. 12, Dec 2025): Hossam et al. (AV fail-degraded survey), Zhang et al. (hazmat routing optimization), Dal'Col et al. (joint perception/prediction survey).

### 16.1 Abstract Blueprint (~120-180 words)

IEEE T-ITS abstracts follow a 5-element funnel:
1. **Domain context** (1 sentence): Establish the field's importance
2. **Problem/gap** (1-2 sentences): Pivot with "However," to identify the challenge
3. **This study** (1-2 sentences): "This study proposes..." or "This paper presents..."
4. **Method summary** (1-2 sentences): What was done technically
5. **Results/implications** (1-2 sentences): Validated findings, key patterns

**Never use "I" in abstract.** Use "This study" or passive voice.
**Include "Index Terms--"** after abstract with 4-6 comma-separated keyword phrases.

### 16.2 Introduction Structure (2-3 pages)

IEEE T-ITS introductions are LONG (~2.5 pages) and follow this exact flow:
1. **Broad domain context** (1-2 paragraphs): Open with drop-cap. Statistics, societal importance.
2. **Problem narrowing** (1-2 paragraphs): Funnel from general to specific challenge.
3. **Literature gap** (1 paragraph): Review existing approaches, then pivot: "However, [gap]."
4. **Contribution statement** (1 paragraph): Bulleted list (see 16.5 below).
5. **Paper roadmap** (1 paragraph): "The remainder of this paper is structured as follows: Section II presents..."

### 16.3 Voice and Person

Three viable strategies observed:
- **"This study" dominant** (recommended for our paper): "This study proposes..." / "This study investigates..." — used 3:1 over "we"
- **"We" for active methodology choices**: "We develop..." / "We employ..." — acceptable in contributions and methods
- **Full third-person/passive** (survey-only): "The article includes..." — too impersonal for original research

**Best practice for our paper:** Lead with "this study" for framing, use "we" for specific methodological decisions, passive for results ("the model was validated").

### 16.4 Citation Patterns (T-ITS Specific)

- **Citation clusters** for broad claims: "[1], [3], [4], [5]" — up to 11 refs in one sentence
- **Author-integrated** for specific methods: "Batta and Chiu [7] proposed..." / "Wang et al. [17] considered..."
- **"The authors of [X]"** construction when not naming: "The authors of [52] introduced..."
- **Chronological evolution language** in lit review: "Early studies..." → "Later studies..." → "Subsequent research..." → "More recent efforts..."
- **Verb choices with citations**: proposed, developed, introduced, examined, extended, addressed, incorporated, formulated

### 16.5 Contribution Statements

**Lead-in phrases** (pick one):
- "The main contributions of this research encompass three key aspects:"
- "The contributions of this paper are as follows:"
- "The main contribution of the paper is to fill this gap, addressing also the following points:"

**Format:** Bulleted list, NOT numbered. Two styles observed:
- **Infinitive style**: "To present... To propose... To provide..." (semicolons between, period at end)
- **Full-paragraph style**: Each bullet is a multi-sentence paragraph starting with "This study addresses..."

**Always 3-4 contributions.** Each should be distinct and verifiable.

### 16.6 Equation Presentation

IEEE T-ITS has a specific equation rhythm:
1. **Name the concept** in prose: "the adjusted accident probability is formulated as..."
2. **Display the equation** (numbered right-aligned)
3. **"where" block**: Define EVERY variable — "where N is the total number of samples, ŷ_i(T) is the predicted position..."
4. **Interpretive sentence** (optional): "In other words, FDE measures the L2 distance..."

**Notation tables:** For papers with many variables, a dedicated "B. Notations" subsection with a two-column table (Symbol | Explanation) BEFORE equations. Our paper should consider this.

**Constraint explanations:** Each constraint labeled and explained: "Constraint (6) ensures each customer is visited exactly once."

### 16.7 Section Hierarchy

IEEE T-ITS uses strict Roman numeral hierarchy:
```
I. INTRODUCTION           (ALL CAPS, Roman numerals)
   A. Subsection           (Capital letter, title case)
      1) Sub-subsection    (Number with parenthesis)
         a) Sub-sub        (Lowercase letter)
```

**Standard flow for optimization papers:**
I. Introduction → II. Literature Review → III. Problem/Model → IV. Solution Method → V. Results/Analysis → VI. Conclusion

### 16.8 Transition Phrases (T-ITS Favorites)

**Dominant transitions (by frequency across 3 papers):**
- "However," — **the workhorse** (~61 uses in one paper alone). Used after describing an approach to introduce its limitation.
- "As can be seen from [Fig./Table/the discussion above]," — signature IEEE T-ITS phrase (~10 uses/paper)
- "Nevertheless," — stronger contrast than "However"
- "Building on this," / "Extending this perspective," — for citing related work progression
- "To address these challenges," — solution framing after problem statement
- "It is important to note that" / "It is worth noting that" — for caveats

**Section-opening formulas:**
- "In this section, [topic] is discussed."
- "This section discusses [X] and is organized into [Y] main parts."

**Literature evolution sequence:** "Early studies..." → "Later studies..." → "Subsequent research..." → "Building on this..." → "More recent efforts..."

### 16.9 Figure and Table References

**Figures:**
- Mid-sentence: "Fig. N" (abbreviated with period)
- Start of sentence: "Figure N" (spelled out)
- Captions: "Fig. 1. Descriptive sentence." (abbreviated)
- Active verbs: "Fig. 3 illustrates..." / "Figure 1 presents..." / "as shown in Fig. 5"

**Tables:**
- Always: "Table N" (never abbreviated, always capitalized)
- Captions: "TABLE I" (all caps, Roman numeral) with title on next line
- "As shown in Table IX," / "Table II provides detailed specifications..."

### 16.10 Conclusion Blueprint

IEEE T-ITS conclusions are SHORT (~1 page) with this structure:
1. **Domain importance restatement** (1 sentence): Echo intro but don't copy
2. **Paper summary** (1 paragraph): "This paper proposes..." — what was done
3. **Key findings** (2-3 sentences): Most important results, briefly
4. **Future directions** (1 paragraph): "Future research can be carried out in the following directions." Then numbered: "First,... Second,... Third,..."

**DO NOT** start with "In conclusion" — the section heading "VI. CONCLUSION" (singular) speaks for itself.
**DO NOT** restate all numerical results — just the key takeaways.

### 16.11 Literature Review Organization

**Always taxonomy-based**, organized by sub-problem or methodology type:
- Split literature into 2-3 major categories
- Each category gets sub-categories
- Within each: define → pioneer → evolution → limitations
- End each category with synthesis paragraph: "Overall, these studies reveal a clear evolution..."
- Bridge to your contribution: "Despite [developments], few studies have explored [your gap]."

**Gap statement formula:** "To the best of our knowledge, this combination of factors has not been previously examined in the academic literature."

### 16.12 Hedging Calibration (T-ITS Level)

IEEE T-ITS papers are **more confident** than biology journals. Hedging is minimal and strategic:
- **Strong claims** for validated results: "The results demonstrate that..."
- **"can" for capability**: "can amplify errors," "can lead to loss of accuracy"
- **"may" for speculation**: "may also yield cost-risk benefits" (only in future work/sensitivity)
- **"typically" for common patterns**: "typically involves three key tasks"
- **Avoid**: "seems to," "appears to," "might suggest" — too weak for T-ITS

**Anti-pattern:** Do not over-hedge. IEEE T-ITS reviewers expect confidence backed by data.

### 16.13 Notation and Model Presentation (Optimization Papers)

Based on Wen et al. and Zhang et al. (both optimization papers in T-ITS):

**Front-load notation:** Dedicate a subsection ("B. Notations") with a two-column table (Symbol | Description) BEFORE any equations. This lets readers reference symbols without hunting through prose.

**Objective function composition:** Define individual cost/risk components separately (Z₁, Z₂, Z₃), each with its own equation number, then combine into a weighted sum: Z = ω₁Z₁ + ω₂Z₂ + ω₃Z₃. Define weights immediately.

**Constraint presentation:** Group by category with italic headers ("1) Route Constraints:", "2) Capacity Constraints:"). Explain in batches: "Constraints (5)-(8) ensure that each route satisfies minimum distance requirements..."

**Assumptions list:** Present numbered assumptions (1-4) before the model, each as a conditional statement.

### 16.14 Weather Data Description (Critical for Our Paper)

Based on Patil et al. (weather-aware traffic forecasting):

**Must describe ALL of these explicitly:**
1. **Data source** with authority: "weather data from 215 Ohio RWIS sensors" — we need: "hourly reanalysis data from ERA5 (ECMWF)"
2. **Sensor/grid count**: They state 215 sensors for 273 stations — we need: "12,516 waypoint coordinates across 2,652 routes"
3. **Spatial resolution**: They describe IDW interpolation with K=3 — we need: "~25 km ERA5 grid resolution, nearest-grid-point retrieval"
4. **Temporal resolution**: "hourly" — we use: "hourly, 8,760 time steps per year"
5. **Variables extracted**: They list temperature, wind speed, precipitation type — we use: temperature, humidity, wind speed
6. **How weather enters the model**: Their weather SCALES travel time multiplicatively: T_adj = T × (1 + Σαₖρₖ). Our weather creates additive penalty components. State this explicitly.

**Interpolation/mapping algorithm:** They include a pseudocode algorithm (Algorithm 1) for weather-to-station mapping. Consider a similar algorithm block for our waypoint-weather mapping.

### 16.15 Results Presentation Patterns

**Two-tier validation** (observed in both Wen and Patil):
1. Small/controlled case (artificial network or subset) — verifiable against exact solver
2. Full-scale real-world case — demonstrates scalability

**Comparison table structure:**
- Rows = methods/scenarios, Columns = metrics
- Include baseline comparisons (GUROBI solver, static models)
- Compact format: slash-separated values across parameter settings

**Sensitivity analysis presentation:**
- Name each configuration descriptively (AAW-Base, StatAdj-W, etc.)
- Show in a single table with one row per configuration
- Conclude with: "Overall, combining [all components] gave the best results."

**Statistics to report (if applicable):**
- Both test statistic AND p-value: "KS = 0.042, p = 0.91"
- Trade-off language: "Lower ω₁ values decrease [X] costs but increase [Y] costs"

### 16.16 Introduction Impact Statistics

IEEE T-ITS introductions open with **concrete, authoritative statistics** for real-world impact:
- Patil: "drivers in the United States wasted an average of 42 hours each year, resulting in a total cost of $70 billion" (citing FHWA)
- Zhang: "surpassing 2 trillion CNY in value and encompassing 13,000 specialized logistics enterprises"

**For our paper:** Open with USDA/EPA pollinator economic impact: "$15 billion in crop pollination annually" + colony loss statistics: "annual losses of 30-40%" + transport scale: "1.7 million colonies shipped annually for almond pollination alone."

### 16.17 Literature Positioning Table

Wen et al. include a **comparison table in the Introduction** (Table I) with columns for: Publication | System | Method | Key Feature 1 | Key Feature 2 | ... The final row is "This paper" with checkmarks showing what distinguishes it.

**For our paper, consider:** A table comparing existing transport-risk studies with columns: Reference | Species | Risk Factors | Temporal Optimization | Intermediate Stops | Weather Integration | Scale (routes). Final row = "This study" showing we are the only one combining all factors.

---

## 17. TONE, VERB CHOICE, AND ACADEMIC REGISTER

**Source:** 7 papers analyzed in detail (5 IEEE T-ITS + Simone-Finstrom 2016, Melicher 2019, Li 2019).

### 17.1 Verb Vocabulary by Function

**Reporting verbs (citing others — use variety, never repeat the same verb 3 times in a row):**
- **Tier 1 (most common):** proposed, showed, demonstrated, found, reported, developed, introduced
- **Tier 2 (variation):** examined, investigated, addressed, extended, considered, incorporated, characterized, formulated, validated
- **Tier 3 (rare but precise):** hypothesized, argued, concluded, emphasized, highlighted, noted

**Methodology verbs (describing your own work):**
- **Active:** develop, propose, design, evaluate, assess, conduct, determine, formulate, integrate, employ, construct, implement, model, calibrate
- **Passive (Methods section):** "was assessed," "were placed," "is formulated," "was measured," "were generated"
- **Forbidden:** "utilize" (use "employ" or "use"); "impact" as verb (use "affect"); "leverage" (use "use" or "exploit")

**Results verbs (presenting findings):**
- **Neutral:** yielded, produced, resulted in, varied, remained, reached, exceeded
- **Positive direction:** outperformed, achieved, maintained, confirmed
- **Negative direction:** declined, decreased, reduced, failed
- **Interpretive:** exhibited, displayed, indicated, revealed, emerged

**Discussion verbs (interpretation — MUST hedge):**
- **Hedged:** suggests, indicates, may support, is consistent with, appears to, could be attributed to
- **Strong (only with strong evidence):** demonstrates, confirms, establishes, corroborates
- **FORBIDDEN:** proves, impacts (as verb), believes

### 17.2 Adjective and Adverb Register

**The cardinal rule: Numbers replace adjectives.** Write "a 10.62% improvement" not "a dramatic improvement." Write "175× difference" not "a huge difference."

**Acceptable adjectives (with correct usage):**

| Adjective | Correct Usage | Wrong Usage |
|-----------|--------------|-------------|
| significant | ONLY with statistical evidence: "significant (p < 0.05)" | "a significant improvement" without p-value |
| substantial | Qualitative magnitude without stats: "a substantial increase" | |
| considerable | Emphasis on importance: "considerable temperature stress" | |
| notable | Calling attention: "a notable finding" | |
| critical | Threshold/essential: "the critical threshold 38°C" | |
| novel | Genuinely new: "a novel vehicle routing problem" | "our novel approach" (overused) |
| robust | Tested across conditions: "robust to perturbation" | "a robust framework" (vague) |
| comprehensive | Complete coverage: "the first comprehensive survey" | |

**FORBIDDEN adjectives/adverbs (never observed in any Q1 paper):**
- very, extremely, hugely, massively, tremendously, incredibly, really
- dramatic/dramatically, groundbreaking, revolutionary, game-changing
- obvious, clearly (if obvious, why state it?)
- Unfortunately, sadly, excitingly (emotional language)
- Basically, essentially (informal hedges)

**Acceptable intensifiers:**
- significantly (with p-value), substantially, considerably, markedly, particularly, notably, slightly, approximately

### 17.3 Tonal Register by Section

| Section | Tone | Example |
|---------|------|---------|
| Abstract | Confident, factual | "This study presents..." / "The framework evaluates..." |
| Introduction | Declarative for facts, gap language for novelty | "No prior work combines..." / "has received minimal investigation" |
| Methods | Neutral, procedural, passive | "Routes were generated via..." / "Temperature was recorded every hour" |
| Results | Factual, numbers-forward, no hedging on computed values | "The maximum health loss was 80.55%" |
| Discussion | Hedged for interpretation, confident for comparisons | "This suggests that..." / "Our results are consistent with..." |
| Conclusion | Confident summary, measured future directions | "Three key findings emerge." / "Future research should address..." |

### 17.4 How to Handle Disagreement with Prior Work

**NEVER directly criticize.** Use gap language instead:

- BAD: "Smith et al. [5] were wrong about X."
- BAD: "Previous work failed to consider X."
- GOOD: "However, X has not been adequately addressed in the existing literature."
- GOOD: "X has currently received minimal investigation."
- GOOD: "To the best of our knowledge, no prior work combines X with Y."
- GOOD: "However, unlike our previous understanding, Z can also adversely affect bees" (Li — softest possible contradiction)

### 17.5 Contribution Tone

Contributions are **factual and itemized**, never promotional:

- GOOD: "We develop a bi-objective mixed integer programming model that minimizes risk and cost."
- GOOD: "This study provides the first comprehensive evidence that migratory management impacts bee health."
- BAD: "We present a groundbreaking framework that dramatically improves..."
- BAD: "Our novel and innovative approach revolutionizes..."

Using "first" is acceptable ONLY when genuinely novel: "the first comprehensive survey" (Dal'Col), "the first practitioner-oriented methodology" (Kostrub).

### 17.6 Limitation Tone

State limitations **matter-of-factly, without apology**, then pivot to mitigation or future work:

- GOOD: "However, computational complexity leads to longer training times, which can be alleviated by using high-performance computing resources." (Patil)
- GOOD: "Low sample size constrains the statistical power to make strong inferences at the colony level." (Simone-Finstrom)
- BAD: "Unfortunately, we were unable to validate against field data."
- BAD: "A weakness of our approach is that..."

### 17.7 Sentence-Level Style Rules

**Nominalization:** IEEE papers prefer nominalized forms: "the optimization of departure timing" over "optimizing departure timing." Biology papers accept either.

**Number presentation:**
- Fold-change: "a fourfold increase" or "1.86-fold" (hyphenated when pre-modifier)
- Multiplier: "175×" (with times symbol) or "a factor of 175"
- Percentages: always with % symbol, never spelled out
- Ranges: en-dash: "20--30°C" in LaTeX
- "Approximately" preferred over "about" or "roughly"

**"Respectively":** Always at end of clause, used only when mapping is not obvious: "accounting for 19.2% and 18.8% of boardings and alightings, respectively."

**Compound modifiers:** Always hyphenated before noun: "weather-dependent risk," "time-dependent routing," "bi-objective model," "long-term survival." Not hyphenated after verb: "the model is time dependent."

**Semicolons:** Rare in IEEE T-ITS. Use periods for most sentence breaks. Semicolons only for tightly parallel constructions: "Layer 1 optimizes timing; Layer 2 optimizes routing."

### 17.8 Forbidden Constructions (NEVER in Q1 papers)

1. Contractions: don't, can't, it's, won't
2. Rhetorical questions: "What if we could optimize...?"
3. Exclamation marks: never
4. "We believe that..." → use "Our results indicate" or "The data suggest"
5. "It is obvious/clear that..." → if obvious, why state it?
6. "As everyone knows..." → use "It has been reported that..."
7. "This paper will show..." (future tense promise) → use present or past
8. "etc." → use "among others" or "including"
9. "A lot of" → use "numerous," "a large number of," or quantify
10. "Due to the fact that" → use "because" or "since"
11. "In order to" → just "to" (simpler, preferred)
12. First person singular "I" → always "we" in multi-author papers
13. Value judgments without data: "This is a great result" → "the deviation is less than 0.3%"
14. Emotional language: unfortunately, sadly, excitingly, surprisingly (unless citing a genuinely surprising finding with "Unexpectedly,")

---

## 18. CHAD FENNER REVIEW PATTERNS

**Source:** Annotations by Chad Fenner. Applied selectively per page-budget constraint.

### 18.1 Sentence splitting — break compound into 2-3 short declarative

Any sentence with multiple independent clauses joined by `and`, `;`, `, with`, `, while` should split into 2-3 shorter sentences. Each new sentence starts with a strong subject and verb. If a sentence has more than one independent clause, split it. If it has more than ~30 words, consider splitting.

### 18.2 Voice preference — "The research/paper/study" over "We"

Chad's note (verbatim): *"try to get away from 'We', it is okay, but I think in research that is always what is talked about, the data not the people who did it."*

In Methods, Results, and Discussion, prefer "The research evaluates..." / "The paper characterizes..." / "The model is trained..." / "The findings show..." over "We...". Exception: "We" is acceptable where the sentence states the assumptions OF the researchers as researchers.

### 18.3 Italicize methodological subheadings

For paragraphs beginning with a labeled subheading (e.g., `Capabilities:`, `Assumptions:`), italicize the label: `\textit{Capabilities}:`. Defer to template constraints.

### 18.4 No promotional verbs for methodology

Rewrite active "We train/evaluate/assess" into passive past-tense "was trained/evaluated/assessed" in Methods.

### 18.5 Drop hedge words where the data is direct

Strip indirect hedges where a direct verb is clearer ("must be flagged" -> "to detect").

### 18.6 List/bullet formatting for enumerable items

Convert long inline enumerations into bulleted lists. Defer if page budget tight.

### 18.7 Reviewer's own typos != paper errors

Verify any apparent typo in a reviewer comment against the actual paper before treating it as an error.

### 18.8 Page-budget discipline when applying review feedback

Apply selectively: zero-risk first (italicize subheadings, "We" -> "The research" swaps); sentence splits next (only the most awkward); recompile + page-check after each batch; stop the moment the body exceeds the limit.

---

*Compiled from analysis of 48 reference papers (Sections 1-15) + 5 IEEE T-ITS venue papers (Section 16) + detailed verb/tone analysis of 7 papers (Section 17) + Chad Fenner review patterns (Section 18). Each paper analyzed for: citation integration, sentence structure, results presentation, transitions, limitations, hedging, figure/table references, opening/closing patterns, interdisciplinary concept explanation, verb vocabulary, tonal register, and academic style markers.*