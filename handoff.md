ScopeGym GAISS Deadline Handoff Specification

1. Objective

Prepare the paper titled "ScopeGym: Evaluating Human-Authorization Boundaries in Goal-Directed AI Agents" for immediate double-blind GAISS submission.

This is a deadline-minimum revision. Do not redesign or rerun the experiment. The required work is:

Anonymize the manuscript and compiled PDF.

Replace non-approved references with the 19-reference allowlist in this specification.

Update the introduction, related work, and impact text so every retained reference supports a precise claim.

Position ScopeGym against the closest peer-reviewed work without overstating novelty.

Compile, verify six-page compliance, and confirm there are no unresolved citations or identifying metadata.

2. Non-negotiable constraints

Target format: IEEE conference format for GAISS.

Maximum submission length: 6 pages, including references unless the conference instructions explicitly state otherwise.

Review mode: double blind.

Approved scholarly sources: IEEE, ACM, ICLR, NeurIPS, ICMR, and Springer Nature.

Single approved exception: the ExploitGym arXiv preprint, because it directly inspired ScopeGym and must receive intellectual credit.

Do not cite ACL, EMNLP, USENIX, NDSS, AAAI workshops, blogs, GitHub pages, or other arXiv-only papers.

Do not describe an accepted or unpublished paper as published.

Do not change experimental data, figures, statistical values, model names, run counts, or conclusions.

Do not convert the statistically inconclusive framing result into a significant or causal claim.

Do not add more self-citations than the two specified IEEE papers.

Use ASCII hyphens in source text. Do not introduce Unicode dash characters.

3. Locate the source files

Claude Code must locate the project rather than assume a filename:

rg -n "ScopeGym: Evaluating Human-Authorization Boundaries" -g '*.tex'
rg -n '\\bibliography\{|\\addbibresource\{' -g '*.tex'
rg --files -g '*.bib'

Expected logical files:

Main IEEE LaTeX manuscript containing the ScopeGym title.

references.bib, or the equivalent BibTeX database referenced by the main manuscript.

figures/ directory containing the current figures.

Do not overwrite unrelated project files.

4. Priority order

P0: Submission blockers

Remove author identities and PDF-identifying metadata.

Ensure the paper compiles.

Ensure the output PDF is no more than six pages.

P1: Bibliography repair

Remove disallowed references.

Add the approved references below.

Update all citation keys and in-text claims.

Ensure the only arXiv reference is ExploitGym.

P2: Novelty positioning

Replace the related-work section with the compact text supplied below.

Explicitly distinguish ScopeGym from ExploitGym, MAC-Bench, and the ACM FAccT cognitive-action-decoupling paper.

P3: Final validation

Run the compilation and anonymity checks.

Inspect the final PDF for layout defects.

Stop if a proposed change would push the paper over six pages or alter reported evidence.

5. Double-blind anonymization

Replace the complete identified author block, including commented identified-author alternatives, with:

\author{\IEEEauthorblockN{Anonymous Author(s)}}

After loading hyperref, add or update:

\hypersetup{
  pdfauthor={Anonymous},
  pdftitle={ScopeGym: Evaluating Human-Authorization Boundaries in Goal-Directed AI Agents}
}

Remove from the submission source and generated PDF:

Karthik Pappu

Varshitha Manjunath

Srimonti Dutta

Dakota State University

Lasell University

All email addresses

All ORCID identifiers

Author-identifying acknowledgments

Phrases such as "our previous work" when citing the authors' published papers

The two self-citations must remain ordinary third-person citations. Do not anonymize their published bibliographic records, but do not identify them as the submitting authors' work.

6. Citation-key migration

Keep these keys

pan2022reward

wang2026exploitgym

ruan2024toolemu

andriushchenko2025agentharm

debenedetti2024agentdojo

Rename/update these keys to final publication years or titles

Old key

New key

zhang2024cybench

zhang2025cybench

yao2024taubench

yao2025taubench

zhang2024asb

zhang2025asb

yu2026toolaffordance

yu2026cognitiveaction

Delete these references and every citation to them

shah2022goal

bondarenko2025specification

abramovich2024enigma

zhang2024agentsafetybench

yuan2024rjudge

zhan2024injecagent

xiang2024guardagent

shi2025progent

zhu2025miniscope

south2025delegation

Do not leave deleted BibTeX entries in the database.

Add these new keys

wang2026cybergym

zhang2025bountybench

zhao2026macbench

zhang2026humanauth

odersky2026capabilities

zouari2025agenticiam

bhushan2026riskadaptive

pappu2026intentgated

ieee7001

ieee7009

7. Approved final reference allowlist

The final bibliography must contain exactly these 19 works unless a duplicate is automatically suppressed by BibTeX.

Pan et al., reward misspecification, ICLR 2022: https://openreview.net/forum?id=JYtwGwIL7ye

Wang et al., ExploitGym, arXiv 2026, approved exception: https://arxiv.org/abs/2605.11086

Ruan et al., ToolEmu, ICLR 2024: https://openreview.net/forum?id=GEcwtMk1uA

Andriushchenko et al., AgentHarm, ICLR 2025: https://openreview.net/forum?id=AC5n7xHuR1

Zhang et al., CyBench, ICLR 2025: https://openreview.net/forum?id=tc90LV0yRL

Yao et al., tau-bench, ICLR 2025: https://openreview.net/forum?id=roNSXZpUDN

Debenedetti et al., AgentDojo, NeurIPS 2024: https://openreview.net/forum?id=m1YYAQjO3w

Zhang et al., Agent Security Bench, ICLR 2025: https://openreview.net/forum?id=V4y0CpX4hK

Yu et al., cognitive-action decoupling, ACM FAccT 2026: https://doi.org/10.1145/3805689.3812378

Wang et al., CyberGym, ICLR 2026: https://openreview.net/forum?id=2YvbLQEdYt

Zhang et al., BountyBench, NeurIPS 2025: https://openreview.net/forum?id=pIsP4lMlFd

Zhao et al., MAC-Bench, ACM KDD 2026: https://doi.org/10.1145/3770855.3817590

Zhang and Wang, human-centered agent authorization, ACM CHI EA 2026: https://doi.org/10.1145/3772363.3798851

Odersky et al., tracked capabilities, ACM CAIS 2026: https://doi.org/10.1145/3786335.3813127

Zouari, Agentic IAM, IEEE/ACM BDCAT 2025: https://doi.org/10.1145/3773276.3776564

Bhushan et al., risk-adaptive authorization, IEEE SoutheastCon 2026: https://doi.org/10.1109/SOUTHEASTCON63549.2026.11476129

Pappu, intent-gated access control, IEEE ISDFS 2026: https://doi.org/10.1109/ISDFS69419.2026.11459115

IEEE 7001-2021, transparency of autonomous systems: https://standards.ieee.org/ieee/7001/6929/

IEEE 7009-2024, fail-safe design: https://standards.ieee.org/ieee/7009/7096/

8. Replacement BibTeX database

Replace the old entries with the following records. Preserve unrelated BibTeX configuration only if the project contains additional manuscripts. For the ScopeGym submission, only these records may be cited.

@inproceedings{pan2022reward,
  author    = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},
  title     = {The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models},
  booktitle = {International Conference on Learning Representations},
  year      = {2022},
  url       = {https://openreview.net/forum?id=JYtwGwIL7ye}
}

@misc{wang2026exploitgym,
  author        = {Zhun Wang and others},
  title         = {{ExploitGym}: Can {AI} Agents Turn Security Vulnerabilities into Real Attacks?},
  year          = {2026},
  eprint        = {2605.11086},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CR},
  url           = {https://arxiv.org/abs/2605.11086},
  note          = {Preprint}
}

@inproceedings{ruan2024toolemu,
  author    = {Yangjun Ruan and others},
  title     = {Identifying the Risks of {LM} Agents with an {LM}-Emulated Sandbox},
  booktitle = {International Conference on Learning Representations},
  year      = {2024},
  url       = {https://openreview.net/forum?id=GEcwtMk1uA}
}

@inproceedings{andriushchenko2025agentharm,
  author    = {Maksym Andriushchenko and others},
  title     = {{AgentHarm}: A Benchmark for Measuring Harmfulness of {LLM} Agents},
  booktitle = {International Conference on Learning Representations},
  year      = {2025},
  url       = {https://openreview.net/forum?id=AC5n7xHuR1}
}

@inproceedings{zhang2025cybench,
  author    = {Andy K. Zhang and others},
  title     = {{CyBench}: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models},
  booktitle = {International Conference on Learning Representations},
  year      = {2025},
  url       = {https://openreview.net/forum?id=tc90LV0yRL}
}

@inproceedings{yao2025taubench,
  author    = {Shunyu Yao and Noah Shinn and Pedram Razavi and Karthik Narasimhan},
  title     = {{$\tau$-bench}: A Benchmark for Tool-Agent-User Interaction in Real-World Domains},
  booktitle = {International Conference on Learning Representations},
  year      = {2025},
  url       = {https://openreview.net/forum?id=roNSXZpUDN}
}

@inproceedings{debenedetti2024agentdojo,
  author    = {Edoardo Debenedetti and Jie Zhang and Mislav Balunovi{\'c} and Luca Beurer-Kellner and Marc Fischer and Florian Tram{\`e}r},
  title     = {{AgentDojo}: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for {LLM} Agents},
  booktitle = {Advances in Neural Information Processing Systems, Datasets and Benchmarks Track},
  year      = {2024},
  url       = {https://openreview.net/forum?id=m1YYAQjO3w}
}

@inproceedings{zhang2025asb,
  author    = {Hongwei Zhang and others},
  title     = {Agent Security Bench ({ASB}): Formalizing and Benchmarking Attacks and Defenses in {LLM}-Based Agents},
  booktitle = {International Conference on Learning Representations},
  year      = {2025},
  url       = {https://openreview.net/forum?id=V4y0CpX4hK}
}

@inproceedings{yu2026cognitiveaction,
  author    = {Shasha Yu and Fiona Carroll and Barry L. Bentley},
  title     = {When Saying ``No'' Is Not Enough: Cognitive-Action Decoupling and the Illusion of Safety in {LLM} Agents},
  booktitle = {Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency},
  pages     = {5593--5612},
  year      = {2026},
  doi       = {10.1145/3805689.3812378},
  url       = {https://doi.org/10.1145/3805689.3812378}
}

@inproceedings{wang2026cybergym,
  author    = {Zhun Wang and Tianneng Shi and Jingxuan He and Matthew Cai and Jialin Zhang and Dawn Song},
  title     = {{CyberGym}: Evaluating {AI} Agents' Real-World Cybersecurity Capabilities at Scale},
  booktitle = {International Conference on Learning Representations},
  year      = {2026},
  url       = {https://openreview.net/forum?id=2YvbLQEdYt}
}

@inproceedings{zhang2025bountybench,
  author    = {Andy K. Zhang and others},
  title     = {{BountyBench}: Dollar Impact of {AI} Agent Attackers and Defenders on Real-World Cybersecurity Systems},
  booktitle = {Advances in Neural Information Processing Systems, Datasets and Benchmarks Track},
  year      = {2025},
  url       = {https://openreview.net/forum?id=pIsP4lMlFd}
}

@inproceedings{zhao2026macbench,
  author    = {Yiyang Zhao and Zhuo Zhang and Qingxuan Le and Lizhen Qu and Zenglin Xu},
  title     = {Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems},
  booktitle = {Proceedings of the ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages     = {10338--10347},
  year      = {2026},
  doi       = {10.1145/3770855.3817590},
  url       = {https://doi.org/10.1145/3770855.3817590}
}

@inproceedings{zhang2026humanauth,
  author    = {Yi Evie Zhang and Ge Wang},
  title     = {Towards Human-Centered Agent Authorization: A Landscape Analysis of Commercial {AI} Agents},
  booktitle = {Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems},
  pages     = {684:1--684:10},
  year      = {2026},
  doi       = {10.1145/3772363.3798851},
  url       = {https://doi.org/10.1145/3772363.3798851}
}

@inproceedings{odersky2026capabilities,
  author    = {Martin Odersky and Yaoyu Zhao and Yichen Xu and Oliver Bra{\v{c}}evac and Cao Nguyen Pham},
  title     = {Securing Agents With Tracked Capabilities},
  booktitle = {Proceedings of the ACM Conference on AI and Agentic Systems},
  pages     = {812--838},
  year      = {2026},
  doi       = {10.1145/3786335.3813127},
  url       = {https://doi.org/10.1145/3786335.3813127}
}

@inproceedings{zouari2025agenticiam,
  author    = {Jaouaher Zouari},
  title     = {Toward Agentic {IAM}: A Probabilistic Authorization Framework for Least Privilege {AI} Workflows},
  booktitle = {2025 IEEE/ACM International Conference on Big Data Computing, Applications and Technologies},
  pages     = {1--6},
  year      = {2025},
  doi       = {10.1145/3773276.3776564},
  url       = {https://doi.org/10.1145/3773276.3776564}
}

@inproceedings{bhushan2026riskadaptive,
  author    = {Badal Bhushan and Karthik Pappu and VasanthRao Jadav and Nilesh Jaiswal},
  title     = {Risk-Adaptive Authorization for Agentic {AI} Systems},
  booktitle = {IEEE SoutheastCon},
  year      = {2026},
  doi       = {10.1109/SOUTHEASTCON63549.2026.11476129},
  url       = {https://doi.org/10.1109/SOUTHEASTCON63549.2026.11476129}
}

@inproceedings{pappu2026intentgated,
  author    = {Karthik Pappu},
  title     = {Contextual Reinforcement Learning for Linguistic Intent-Gated Access Control in Production {AI} Systems},
  booktitle = {International Symposium on Digital Forensics and Security},
  year      = {2026},
  doi       = {10.1109/ISDFS69419.2026.11459115},
  url       = {https://doi.org/10.1109/ISDFS69419.2026.11459115}
}

@techreport{ieee7001,
  author      = {{IEEE}},
  title       = {{IEEE} Standard for Transparency of Autonomous Systems},
  institution = {Institute of Electrical and Electronics Engineers},
  number      = {IEEE Std 7001-2021},
  year        = {2021},
  url         = {https://standards.ieee.org/ieee/7001/6929/}
}

@techreport{ieee7009,
  author      = {{IEEE}},
  title       = {{IEEE} Standard for Fail-Safe Design of Autonomous and Semi-Autonomous Systems},
  institution = {Institute of Electrical and Electronics Engineers},
  number      = {IEEE Std 7009-2024},
  year        = {2024},
  url         = {https://standards.ieee.org/ieee/7009/7096/}
}

9. Required manuscript text replacements

9.1 Introduction citation paragraph

Replace the paragraph beginning with This distinction creates the central problem studied here and ending with the final outcome hides an important part of the action path with:

This distinction creates the central problem studied here. Suppose an agent
returns the expected flag after consulting an answers service that the operator
explicitly placed outside the task boundary. A conventional pass/fail metric
may record only the accepted flag and miss the unauthorized route. This is a
practical concern for agents that can call tools, query services, or modify
state. Reward-misspecification research shows that optimizing a proxy can move
behavior away from the intended objective \cite{pan2022reward}. MAC-Bench
similarly evaluates whether agents sacrifice procedural compliance while
pursuing task success \cite{zhao2026macbench}. These findings motivate an
evaluation that records the selected action path rather than only the final
answer.

9.2 Replace the complete Related Work and Research Gap section

Replace everything after:

\section{Related Work and Research Gap}

and before the first following figure* environment with:

Execution-based cybersecurity benchmarks measure whether agents can complete
security tasks in interactive environments. CyBench evaluates language-model
cybersecurity capabilities \cite{zhang2025cybench}; CyberGym scales evaluation
to real-world vulnerable projects \cite{wang2026cybergym}; and BountyBench
measures offensive and defensive performance on realistic systems
\cite{zhang2025bountybench}. ExploitGym is the direct inspiration for our
path-sensitive design: it asks agents to turn a proof of vulnerability into
unauthorized code execution and validates the resulting trajectory
\cite{wang2026exploitgym}. ScopeGym adopts the lesson that the route matters but
changes the object of study from exploitation capability to selection and
enforcement at an inert human-specified authorization boundary.

General agent-safety benchmarks examine failures across tools and environments.
ToolEmu uses emulated tools to reveal high-stakes failures
\cite{ruan2024toolemu}; AgentHarm evaluates harmful multi-step behavior
\cite{andriushchenko2025agentharm}; AgentDojo evaluates prompt-injection attacks
and defenses \cite{debenedetti2024agentdojo}; Agent Security Bench formalizes
security--utility tradeoffs \cite{zhang2025asb}; and $\tau$-bench evaluates
tool-agent-user interaction under domain policies \cite{yao2025taubench}.
ScopeGym narrows the evaluation target to the requested action, enforcement
decision, and continuation after denial.

Two recent studies are especially close. MAC-Bench audits procedural
compliance when agents face pressure to maximize task success
\cite{zhao2026macbench}. Yu et al. separate textual refusal from unsafe
tool-mediated action and distinguish attempted from realized violations under
blocking and permissive conditions \cite{yu2026cognitiveaction}. ScopeGym does
not claim to originate attempt-versus-execution measurement. Its narrower
contribution is to cross ordinary goal framing with an explicit authorization
gate and then measure persistence and safe recovery after denial in a sealed
cybersecurity-style trajectory.

Authorization research supplies complementary enforcement mechanisms.
Commercial-agent analysis identifies shortcomings in permission negotiation,
revocation, and user oversight \cite{zhang2026humanauth}. Agentic IAM applies
probabilistic least-privilege authorization \cite{zouari2025agenticiam}, while
tracked capabilities constrain agent effects through a capability-safe type
system \cite{odersky2026capabilities}. Risk-adaptive authorization and
intent-gated access control provide further policy-level approaches
\cite{bhushan2026riskadaptive,pappu2026intentgated}. These systems decide what
may execute. ScopeGym instead evaluates what the model requests before
enforcement and how it adapts after the system refuses that request.

9.3 Update the Impact of the Experiment authorization paragraph

Replace the paragraph beginning with For deployed tool-using agents and ending with recovery behavior with:

For deployed tool-using agents, the experiment supports two complementary
safeguards. Scope instructions can influence which action a model selects, but
their effect may be uncertain and model-dependent. A least-privilege gate can
independently prevent the selected action from changing the environment. This
layered design is consistent with probabilistic authorization, tracked
capabilities, risk-adaptive authorization, and intent-gated access control
\cite{zouari2025agenticiam,odersky2026capabilities,
bhushan2026riskadaptive,pappu2026intentgated}. Recording the requested action
and enforcement decision supports autonomous-system transparency, while a
deterministic denial path provides fail-safe behavior
\cite{ieee7001,ieee7009}. Logs then provide an audit trail for improving
prompts, policies, and recovery behavior.

9.4 Preserve the ExploitGym flag citation

Keep the citation to wang2026exploitgym in the subsection explaining what the flag represents. Do not imply that ScopeGym performs real exploitation.

10. Claims and novelty guardrails

The final manuscript may claim:

ScopeGym records the requested action before policy enforcement.

It distinguishes requested, permitted, executed, persistent, recovered, and completed behavior.

It crosses goal framing with an authorization gate in a sealed symbolic environment.

It reports descriptive pilot evidence from 120 runs and 461 logged actions.

It studies post-denial persistence and safe recovery.

The final manuscript must not claim:

ScopeGym invented the distinction between attempted and executed violations.

Goal framing caused a statistically significant difference.

The two evaluated models represent all LLM agents.

A blocked request proves that the model internally intended harm.

The deterministic gate result is evidence of model alignment.

ScopeGym is a replacement for realistic cyber ranges or exploitation benchmarks.

11. Compilation and verification commands

Adjust the main filename if necessary.

latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
pdfinfo main.pdf | rg '^Pages:'
pdftotext main.pdf - | rg -ni 'Karthik|Varshitha|Srimonti|Dakota State|Lasell|@|0009-'
rg -n 'shah2022goal|bondarenko2025specification|abramovich2024enigma|zhang2024agentsafetybench|yuan2024rjudge|zhan2024injecagent|xiang2024guardagent|shi2025progent|zhu2025miniscope|south2025delegation' -g '*.tex' -g '*.bib'
rg -n 'arxiv|arXiv' -g '*.bib'
rg -n 'undefined citations|Citation.*undefined|There were undefined references' main.log
rg -n 'Overfull \\hbox|Overfull \\vbox' main.log

Expected outcomes:

Page count is 6 or fewer.

Identity search returns no matches from the PDF.

Deleted-key search returns no matches.

The BibTeX arXiv search returns only wang2026exploitgym.

No undefined citations or references.

No material overfull boxes.

Also run a final source-level citation audit:

rg -o '\\cite\{[^}]+\}' -g '*.tex' | sort -u

Confirm every citation key exists in the active .bib file and every active BibTeX entry is cited.

12. Visual PDF inspection

Render the final PDF and inspect every page:

mkdir -p /tmp/scopegym_render
pdftoppm -png -r 150 main.pdf /tmp/scopegym_render/page

Check for:

Clipped references or URLs

Reference entries crossing columns incorrectly

Figure movement that separates figures from their discussion

Widows, orphans, or large blank areas

Text or tables extending beyond column boundaries

Author information or identifying PDF headers

A seventh page created by the expanded bibliography

If the paper exceeds six pages, shorten prose in Related Work first. Do not shrink fonts, margins, figures, captions, or line spacing below the IEEE template defaults.

13. Definition of done

The task is complete only when all of the following are true:

The source and PDF are double-blind.

The PDF is no more than six pages.

The paper contains exactly the approved reference set, with ExploitGym as the only preprint exception.

CyBench, CyberGym, BountyBench, AgentHarm, ToolEmu, tau-bench, AgentDojo, and ASB use their peer-reviewed venue records.

MAC-Bench and the ACM FAccT cognitive-action paper are cited and distinguished from ScopeGym.

The two authorization self-citations are written in neutral third person.

No experiment, number, figure, or statistical conclusion has changed.

LaTeX compilation completes without errors or unresolved citations.

The rendered PDF has no material layout defects.

The final output includes the anonymized PDF and its exact source bundle.

14. Deliverables from Claude Code

Claude Code should return:

The modified main .tex file.

The modified references.bib file.

The compiled anonymous submission PDF.

A short change log listing deleted, updated, and added citation keys.

The page count and results of the anonymity and unresolved-citation checks.

Do not create a camera-ready author version during this deadline pass.