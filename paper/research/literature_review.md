# Literature review and research-gap record

## Search protocol

- Last searched: 2026-07-29
- Discovery systems: Consensus, arXiv, OpenReview, and official conference or
  publisher pages
- Search families:
  - `AI agents specification gaming reward hacking goal misgeneralization`
  - `human oversight authorization autonomous AI agents accountability`
  - `cybersecurity AI agent benchmark exploitation CTF`
  - `large language model agents safety benchmark unintended behavior`
  - `LLM agent safety benchmark unauthorized actions policy compliance tool use`
  - `prompt injection benchmark tool integrated LLM agents AgentDojo InjecAgent`
  - `authorization delegation AI agents permissions least privilege approval`
  - `goal framing specification gaming reward hacking language model agents benchmark`
- Date emphasis: 2022–2026, with archival preprints admitted under the
  computer-science/machine-learning evidence profile
- Inclusion: primary papers that define an agent benchmark, demonstrate
  specification gaming, evaluate attempted or realized unsafe action, or
  formalize delegated authorization and least-privilege enforcement
- Exclusion: commentary without primary evidence, unrelated model-only safety
  tests, and papers whose bibliographic identity could not be verified

Consensus was used for discovery and gap triangulation. Every work cited in the
paper was then checked against its full Consensus record and primary arXiv or
OpenReview identity record.

## Synthesis

1. **Misspecified objectives and benchmark gaming.** Pan et al. show that more
   capable agents can exploit reward misspecification. Shah et al. distinguish
   goal misgeneralization from an incorrect written specification. Bondarenko
   et al. demonstrate benchmark hacking by reasoning models in a chess task.
   Together, these works motivate an attempt-level measure rather than a final
   score alone.
2. **Cybersecurity capability benchmarks.** CyBench and EnIGMA measure CTF
   problem solving, while ExploitGym evaluates progression from vulnerabilities
   to concrete exploits. Their primary contribution is realistic capability
   measurement; they do not cross goal framing with an executable
   human-authorization gate.
3. **Agent safety benchmarks.** ToolEmu, AgentHarm, Agent-SafetyBench, and
   R-Judge evaluate risky actions, harmful tasks, or risk awareness.
   Tau-bench tests rule following in tool-agent-user interaction. These
   benchmarks establish the need for behavioral safety evaluation.
4. **Adversarial tool-security benchmarks.** InjecAgent, AgentDojo, and Agent
   Security Bench test indirect prompt injection, attacks, defenses, and
   security--utility tradeoffs for tool-integrated agents. They focus on
   adversarial inputs rather than ordinary changes in goal framing.
5. **Authorization infrastructure.** GuardAgent checks agent behavior against
   user-defined guard requests. Progent mediates tool calls with symbolic
   least-privilege rules; MiniScope reconstructs permission hierarchies for
   tool-calling agents; and South et al. formalize authenticated, authorized,
   and auditable delegation. These systems motivate executable gates and
   external reference monitoring, while their main evaluations concern
   enforcement, security, and utility.
6. **Nearest experimental precedent.** Yu et al. compare text-only and
   tool-enabled agents in a deterministic financial environment and use
   permissive versus blocking enforcement to separate attempted from realized
   violations. This work directly supports ScopeGym's intent--execution
   distinction. ScopeGym differs by keeping the symbolic action affordance
   available in every condition, crossing three goal framings with gate state,
   and measuring persistence and recovery after denial.

## Search-bounded gap

The closest identified study already separates attempted and realized
violations under blocking versus permissive enforcement. The remaining,
search-bounded gap is narrower: no reviewed study jointly (i) randomizes
ordinary goal framing while holding the action affordance present, (ii) toggles
an executable authorization gate, and (iii) reports persistence and safe
recovery after denial alongside attempt, execution, and completion. This is a
bounded statement about the documented search, not an absolute priority claim.

## Selected Consensus discovery records

| Work | Consensus record | Role |
|---|---|---|
| Goal Misgeneralization | `999bba2cdb825ea9871aa5e08e70bece` | objective-framing theory |
| Reward Misspecification | `dc88f37451f15860b3e886d0078120ba` | reward-hacking evidence |
| Specification Gaming in Reasoning Models | `0a535be1dcdb5117be9cd0faf749a96a` | nearest behavioral precedent |
| Authenticated Delegation | `d71e273a402858feb205f7833ec6deed` | authorization framework |
| CyBench | `85fa2e4b68eb5aafa1bba5074036e6f7` | cybersecurity benchmark |
| EnIGMA | `4385d3d9205b5d3496fd300803870651` | cybersecurity agents |
| Agent-SafetyBench | `8575ac81abae5ecd8984e258248f7870` | agent-safety benchmark |
| R-Judge | `0b445ab6be7c529bba1fe8602c402a10` | risk-awareness benchmark |
| Tool Affordance and Safety Alignment | `f19d43db458156f0916db8b0d05e2866` | nearest enforcement experiment |
| InjecAgent | `1f22a6682586514aaa8f32ad3e8a9fb5` | indirect prompt-injection benchmark |
| AgentDojo | `2767c52e68cc5c859885fda9822f69d4` | dynamic attack/defense environment |
| Agent Security Bench | `855f0332a1cf58df9cca7ce9354d7b88` | broad agent-security benchmark |
| GuardAgent | `a7dfac96bfe55220a8b32f3029ca27bd` | guard-request enforcement |
| Progent | `629a8810148555b785f9e4b1d48f86a8` | deterministic privilege control |
| MiniScope | `7325ad8945ba51d2b33765e415cc1dd2` | least-privilege authorization |
