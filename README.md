# Lee Sang Gyu (이상규)

**Co-founder, Ouro Labs** · **Core Maintainer, Ouroboros** · Hansung University

I build tools and protocols for human–AI collaboration.

My work asks a practical question: how can AI make human judgment easier to examine, test, and act on while keeping people responsible for their decisions?

## Main Work

### [Ouroboros](https://github.com/Q00/ouroboros) · 6k+ stars

I am a core maintainer of Ouroboros, an open-source agent OS for AI-assisted software development. I work on specifying tasks, coordinating agent execution, and preserving evidence that people can use to evaluate the results.

Through Ouro Labs, a collaborative team, I also work on research and applied AI projects.

[My merged contributions](https://github.com/Q00/ouroboros/pulls?q=is%3Apr+author%3Alee3Q+is%3Amerged)

### [codbeing](https://github.com/lee3Q/codbeing)

A local-first experimental tool for recording decisions as structured `DecisionTrace` records, revisiting their original reasoning, and producing evidence-grounded runtime analysis.

### [30p / Human30](https://github.com/lee3Q/human30)

An exploratory simulation of fictional human perspectives. It examines how the same situation can lead to different actions as body, memory, identity, and world-model conditions change. It is a thought experiment, not a validated model of real people.

## Prior Protocol & Collaborative Projects

- **[Pullim](https://github.com/lee3Q/pullim)**: Earlier protocol research, now also an experimental decision-support app. It helps turn a difficult situation into a clearer problem, usable evidence, a provisional decision, and a next action chosen by the person.
- **[말결 (Malgyeol)](https://github.com/lee3Q/malgyeol)**, with SergioBuilds: Bounded agent-payment infrastructure that connects human intent with policy checks, consent, purchasing, and payment evidence.
- **[FlashPatch](https://github.com/lee3Q/flashpatch)**, with SergioBuilds: Open-source visual safety QA for detecting potentially hazardous flashing, applying scoped repairs, rerunning checks, and recording the evidence.

## How the Projects Connect

`codbeing` records and revisits judgment. `Pullim` explores how judgment leads to action. `30p` examines how choices can branch under different human conditions. `Ouroboros` provides an execution and verification layer for carrying out AI-assisted work with traceable evidence.

Across these projects, I am interested in systems where AI helps people see, challenge, and improve their reasoning while they remain accountable for the decisions.

<details>
<summary>Selected Ouroboros contributions</summary>

- **Execution and recovery:** background-job polling, result recovery, checkpoint compatibility, and shared runner initialization. ([Job lifecycle](https://github.com/Q00/ouroboros/pull/1622), [runner assembly](https://github.com/Q00/ouroboros/pull/2748))
- **Verification evidence:** connecting file-change claims to execution records, collecting tool-call evidence, and separating source checks from runtime assertions. ([File claims](https://github.com/Q00/ouroboros/pull/1764), [tool evidence](https://github.com/Q00/ouroboros/pull/2640), [runtime assertions](https://github.com/Q00/ouroboros/pull/2758))
- **Runtime integration and diagnosis:** Zcode runtime and LLM adapters, installation diagnostics, and MCP startup, discovery, and cleanup probes. ([Zcode](https://github.com/Q00/ouroboros/pull/1568), [LLM adapter](https://github.com/Q00/ouroboros/pull/1595), [installation doctor](https://github.com/Q00/ouroboros/pull/2034), [MCP probe](https://github.com/Q00/ouroboros/pull/2406))
- **Alignment with intent:** structured ambiguity records, goal-drift checks, and quality-first model routing. ([Ambiguity evidence](https://github.com/Q00/ouroboros/pull/2417), [goal drift](https://github.com/Q00/ouroboros/pull/2643), [quality-first routing](https://github.com/Q00/ouroboros/pull/2673))

</details>
