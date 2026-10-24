# Lee Sang Gyu

I build tools for human–AI collaboration, with a focus on how people supervise agent execution and verify its results.

## Main work: [Ouroboros](https://github.com/Q00/ouroboros)

Ouroboros is an agent OS for AI-assisted software development, connecting requirements interviews, execution, and evaluation. I contribute to its orchestration, runtime integrations, and verification layers.

My work concentrates on the boundaries where an agent's report needs to match what actually happened:

- **Execution and recovery.** I work on background-job polling, result recovery, and checkpoint compatibility. I unified how command-line, MCP, and iterative development runs are initialized, including state storage and worker limits. ([Job lifecycle](https://github.com/Q00/ouroboros/pull/1622), [runner assembly](https://github.com/Q00/ouroboros/pull/2748))
- **Evidence for verification.** I tighten how file-change claims are tied to execution evidence, capture tool-call records for artifact collection, and separate source checks from assertions that require an executed test or runtime observation. ([File claims](https://github.com/Q00/ouroboros/pull/1764), [tool evidence](https://github.com/Q00/ouroboros/pull/2640), [runtime assertions](https://github.com/Q00/ouroboros/pull/2758))
- **Runtime integration and diagnosis.** I contributed the Zcode runtime and LLM adapter, and worked on installation diagnostics and MCP probes that distinguish startup, tool discovery, and cleanup failures. ([Zcode](https://github.com/Q00/ouroboros/pull/1568), [LLM adapter](https://github.com/Q00/ouroboros/pull/1595), [installation doctor](https://github.com/Q00/ouroboros/pull/2034), [MCP probe](https://github.com/Q00/ouroboros/pull/2406))
- **Keeping execution aligned with intent.** I added structured records of unclear requirements and their source evidence, and a check comparing the original goal with the execution summary. I also fixed model routing so a user's quality-first preference is preserved. ([Ambiguity evidence](https://github.com/Q00/ouroboros/pull/2417), [goal drift](https://github.com/Q00/ouroboros/pull/2643), [quality-first routing](https://github.com/Q00/ouroboros/pull/2673))

[My merged contributions](https://github.com/Q00/ouroboros/pulls?q=is%3Apr+author%3Alee3Q+is%3Amerged)

## Other work

I also explore how human decisions can be recorded, examined, and turned into action through [codbeing](https://github.com/lee3Q/codbeing), [Pullim](https://github.com/lee3Q/pullim), and [30p / Human30](https://github.com/lee3Q/human30).

Collaborative projects with SergioBuilds: [말결](https://github.com/lee3Q/malgyeol) and [FlashPatch](https://github.com/lee3Q/flashpatch).
