# IEEE-style citation audit

## Summary

| Metric | Result |
|---|---:|
| In-text reference keys | 19 |
| BibTeX entries | 19 |
| Orphan in-text citations | 0 |
| Orphan bibliography entries | 0 |
| Numbering style | IEEE, order of first appearance |
| Direct quotations from literature | 0 |
| Self-citations | 0/19 |
| Sources dated 2022–2026 | 19/19 |

## Verification status

- ArXiv identity pages verified for:
  `2201.03544`, `2210.01790`, `2502.13295`, `2408.08926`,
  `2409.16165`, `2605.11086`, `2412.14470`, `2401.10019`,
  `2406.12045`, `2403.02691`, `2406.13352`, `2410.02644`,
  `2406.09187`, `2504.11703`, `2512.11147`, `2501.09674`, and
  `2603.20320`.
- OpenReview conference records verified for ToolEmu
  (`GEcwtMk1uA`, ICLR 2024) and AgentHarm (`AC5n7xHuR1`, ICLR
  2025).
- ArXiv-issued DOI strings are retained in `references.bib`; IEEEtran renders
  the primary URLs in the manuscript.
- Long author lists are rendered with `et al.` in the paper, following IEEE
  reference-list conventions. Titles, years, identifiers, and venues remain
  explicit.
- Claims use paraphrase, so no page/quote locator is required.
- Full Consensus records were fetched before the seven newly added sources
  were cited. Their primary arXiv identities were then verified.
- The author's Google Scholar profile was used to confirm identity and
  disciplinary context. No prior paper from the profile was inserted solely to
  create a self-citation.

## Claim-faithfulness check

| Manuscript use | Source support | Status |
|---|---|---|
| Capable agents exploit reward misspecification | Pan et al., abstract and results framing | PASS |
| Correct specifications can still produce undesired learned goals | Shah et al., definition of goal misgeneralization | PASS |
| Reasoning models can hack a chess benchmark | Bondarenko et al., experimental finding | PASS |
| Cyber benchmarks emphasize capability/task completion | CyBench, EnIGMA, and ExploitGym benchmark definitions | PASS |
| Agent-safety benchmarks cover risky actions or risk awareness | ToolEmu, AgentHarm, Agent-SafetyBench, R-Judge | PASS |
| Tau-bench evaluates domain-policy following | Tau-bench benchmark definition | PASS |
| Tool-security benchmarks evaluate prompt injection, attacks, and defenses | InjecAgent, AgentDojo, Agent Security Bench | PASS |
| Guard and privilege systems enforce action or permission policies | GuardAgent, Progent, MiniScope | PASS |
| Delegation frameworks separate scope, permission, and auditability | South et al., proposed framework | PASS |
| Blocking can separate attempted from realized violations | Yu et al., paired permissive/blocking study | PASS |
| No reviewed study combined framing, gate state, and post-denial persistence/recovery | Documented, date-bounded Consensus and primary-record search | PASS WITH BOUND |

No citation is used to support a stronger claim than its primary record
establishes.
