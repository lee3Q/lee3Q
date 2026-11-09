# Lee Sang Gyu (이상규)

**Co-founder, [Ouro Labs](https://ourolabs.vercel.app/)** · **Core Maintainer, [Ouroboros](https://github.com/Q00/ouroboros)**

I build tools and protocols for human–AI collaboration.  
My work asks a practical question: *how can AI make human judgment easier to examine, test, and act on while keeping people responsible for their decisions?*

<!-- AUTO-BADGES:START -->
[![Ouro Labs](https://img.shields.io/badge/Ouro_Labs-Co--founder-0F172A?style=flat-square)](https://ourolabs.vercel.app/)
[![Ouroboros](https://img.shields.io/badge/Ouroboros-Core_Maintainer_(53_Merged_PRs)-4338CA?style=flat-square&logo=github&logoColor=white)](https://github.com/Q00/ouroboros/pulls?q=is%3Apr+author%3Alee3Q+is%3Amerged)
[![Upstream OSS](https://img.shields.io/badge/Open_Source-104_Merged_PRs_Across_13_Projects-047857?style=flat-square&logo=git&logoColor=white)](https://github.com/search?q=is%3Apr+author%3Alee3Q+is%3Amerged+-user%3Alee3Q&type=pullrequests)
<!-- AUTO-BADGES:END -->

---

## Main Work

<!-- AUTO-OUROBOROS:START -->
### [Ouroboros](https://github.com/Q00/ouroboros) · ⭐ 6.3k — *Core Maintainer*

**Open-source Agent OS for Specification-First AI Software Development**

I am a core maintainer of **Ouroboros** and a co-founder of **[Ouro Labs](https://ourolabs.vercel.app/)**. My work focuses on turning ambiguous human requests into explicit specifications (`Seed`), coordinating multi-runtime agent execution, and preserving verifiable evidence so people can audit the outcome.

- **Verification & Evidence Integrity:** Binding file-modification claims to observed tool-call receipts, isolating source checks from runtime assertions, and rejecting malformed semantic evaluation scores.
- **Execution & Lifecycle Recovery:** Background-job polling and recovery, cancellation lifecycle management, checkpoint compatibility, and unified runner assembly.
- **Multi-Runtime Adapters & Diagnostics:** Zcode runtime and LLM adapters, Antigravity stream normalization, provider routing across OpenAI/Anthropic/Gemini, and `doctor` MCP/installation probes.
- **Intent Alignment & Drift Control:** Structured ambiguity ledgers (`B2`), semantic goal-drift checks, unanswered interview round floors, and locale-independent UTF-8 handling.

👉 **[All 53 merged PRs in `Q00/ouroboros`](https://github.com/Q00/ouroboros/pulls?q=is%3Apr+author%3Alee3Q+is%3Amerged)**

<details>
<summary><b>Selected Ouroboros contributions by subsystem</b></summary>
<br/>

| Area | Scope | Merged PRs |
| :--- | :--- | :--- |
| **Verification & Evidence** | Bound `pathlib` write claims to execution records; linked wrapper test receipts to accepted Bash attempts; separated source checks from runtime assertions; captured native tool evidence; rejected malformed semantic scores. | [#1764](https://github.com/Q00/ouroboros/pull/1764), [#2639](https://github.com/Q00/ouroboros/pull/2639), [#2640](https://github.com/Q00/ouroboros/pull/2640), [#2745](https://github.com/Q00/ouroboros/pull/2745), [#2749](https://github.com/Q00/ouroboros/pull/2749), [#2758](https://github.com/Q00/ouroboros/pull/2758), [#2842](https://github.com/Q00/ouroboros/pull/2842) |
| **Orchestrator & Job Recovery** | Hardened MCP background-job polling and recovery; recovered artifact contracts and QA environments; extracted Phase 3 cancellation lifecycle; unified public run builder assembly; bounded workspace fingerprint scans. | [#1622](https://github.com/Q00/ouroboros/pull/1622), [#1630](https://github.com/Q00/ouroboros/pull/1630), [#2567](https://github.com/Q00/ouroboros/pull/2567), [#2635](https://github.com/Q00/ouroboros/pull/2635), [#2636](https://github.com/Q00/ouroboros/pull/2636), [#2637](https://github.com/Q00/ouroboros/pull/2637), [#2638](https://github.com/Q00/ouroboros/pull/2638), [#2746](https://github.com/Q00/ouroboros/pull/2746), [#2748](https://github.com/Q00/ouroboros/pull/2748) |
| **Runtime Adapters & Diagnostics** | Implemented Zcode runtime backend and LLM adapter; built installation `doctor` and local stdio MCP probes; hardened Codex cold starts and locale-independent UTF-8 seed/source decoding. | [#1568](https://github.com/Q00/ouroboros/pull/1568), [#1595](https://github.com/Q00/ouroboros/pull/1595), [#2034](https://github.com/Q00/ouroboros/pull/2034), [#2406](https://github.com/Q00/ouroboros/pull/2406), [#2411](https://github.com/Q00/ouroboros/pull/2411), [#2420](https://github.com/Q00/ouroboros/pull/2420), [#2499](https://github.com/Q00/ouroboros/pull/2499), [#2564](https://github.com/Q00/ouroboros/pull/2564), [#2846](https://github.com/Q00/ouroboros/pull/2846), [#2847](https://github.com/Q00/ouroboros/pull/2847), [#2860](https://github.com/Q00/ouroboros/pull/2860) |
| **Intent Alignment & Routing** | Built typed ambiguity evidence ledger (`B2`); floored ambiguity for unanswered interview rounds; semantic goal-drift checks; quality-first model routing and OpenAI/Anthropic/Gemini compatibility. | [#2415](https://github.com/Q00/ouroboros/pull/2415), [#2417](https://github.com/Q00/ouroboros/pull/2417), [#2642](https://github.com/Q00/ouroboros/pull/2642), [#2643](https://github.com/Q00/ouroboros/pull/2643), [#2660](https://github.com/Q00/ouroboros/pull/2660), [#2668](https://github.com/Q00/ouroboros/pull/2668), [#2669](https://github.com/Q00/ouroboros/pull/2669), [#2673](https://github.com/Q00/ouroboros/pull/2673), [#2819](https://github.com/Q00/ouroboros/pull/2819) |
| **Additional & Recent Merged PRs** | Continuing maintenance across CLI, runtime adapters, docs, and verification checks. | [#2776](https://github.com/Q00/ouroboros/pull/2776), [#2647](https://github.com/Q00/ouroboros/pull/2647), [#2646](https://github.com/Q00/ouroboros/pull/2646), [#2645](https://github.com/Q00/ouroboros/pull/2645), [#2644](https://github.com/Q00/ouroboros/pull/2644), [#2641](https://github.com/Q00/ouroboros/pull/2641), [#2634](https://github.com/Q00/ouroboros/pull/2634), [#2633](https://github.com/Q00/ouroboros/pull/2633), [#2632](https://github.com/Q00/ouroboros/pull/2632), [#2631](https://github.com/Q00/ouroboros/pull/2631), [#2630](https://github.com/Q00/ouroboros/pull/2630), [#2629](https://github.com/Q00/ouroboros/pull/2629) |

</details>
<!-- AUTO-OUROBOROS:END -->

---

## Decision & Perspective Projects

<table>
  <tr>
    <td width="33%" valign="top">
      <h4><a href="https://github.com/lee3Q/codbeing">codbeing</a></h4>
      <p><b>Local-first decision records &amp; prospective judgment analysis</b></p>
      <p>Records consequential choices as structured <code>DecisionTrace</code> entries (context, options, and judgment basis) and keeps later observations separate from original records via SHA-256 snapshot digests so hindsight never rewrites initial reasoning.</p>
    </td>
    <td width="33%" valign="top">
      <h4><a href="https://github.com/lee3Q/human30">30p / Human30</a></h4>
      <p><b>Counterfactual human perspective simulator</b></p>
      <p>An exploratory simulation of 30 fictional agents across four structural layers (<code>Body</code>, <code>Memory</code>, <code>Identity</code>, and <code>Context</code>). Examines how the same situation branches into different actions as underlying conditions shift.</p>
    </td>
    <td width="33%" valign="top">
      <h4><a href="https://github.com/lee3Q/pullim">Pullim (풀림)</a></h4>
      <p><b>Decision-support &amp; action-promise protocol</b></p>
      <p>Helps turn an unstructured personal concern into separated facts vs. assumptions, a provisional decision, and a concrete next action (<code>Ladder</code> promise) chosen by the user, with local history export.</p>
    </td>
  </tr>
</table>

### Collaborative & Protocol Prototypes

- **[말결 (Malgyeol)](https://github.com/lee3Q/malgyeol)** *(with SergioBuilds)* — Bounded agent-payment infrastructure connecting human purchasing intent with policy checks, explicit consent gates, and auditable payment evidence.
- **[FlashPatch](https://github.com/lee3Q/flashpatch)** *(with SergioBuilds)* — Open-source visual safety QA pipeline for detecting potentially hazardous photosensitive flashing in media, applying scoped repairs, and recording verification evidence.

### How the Projects Connect

```text
  codbeing (Record & revisit judgment without hindsight distortion)
     │
     ├──► Pullim (Separate facts from assumptions & commit to a next action)
     ├──► 30p / Human30 (Explore how choices branch under different conditions)
     │
     ▼
  Ouroboros (Specify intent as a Seed, execute across runtimes, and verify with evidence)
```

Across these projects, I am interested in systems where AI helps people see, challenge, and improve their reasoning while they remain accountable for the final decision.

---

## Open-Source Contributions

Beyond my own projects and **Ouroboros**, I contribute bug fixes, parser/protocol compliance patches, input-validation guards, and regression tests across open-source projects in **C, Python, TypeScript, JavaScript, and SQL**:

<!-- AUTO-OSS:START -->
| Project | Stars | Stack | Merged Contributions |
| :--- | :---: | :--- | :--- |
| **[Oh My ClaudeCode (OMC)](https://github.com/Yeachan-Heo/oh-my-claudecode)** | ⭐ 40.7k | `TypeScript` | Preflight context-threshold validation and read-budget env override guards preventing malformed values from silently activating ([#4069](https://github.com/Yeachan-Heo/oh-my-claudecode/pull/4069), [#4070](https://github.com/Yeachan-Heo/oh-my-claudecode/pull/4070), [#4071](https://github.com/Yeachan-Heo/oh-my-claudecode/pull/4071)) |
| **[Oh My Codex (OMX)](https://github.com/Yeachan-Heo/oh-my-codex)** | ⭐ 33.7k | `TypeScript` | Stripping OSC terminal-control sequences from notification text and surfacing resolved config paths in `doctor` ([#3691](https://github.com/Yeachan-Heo/oh-my-codex/pull/3691), [#3693](https://github.com/Yeachan-Heo/oh-my-codex/pull/3693), [#3694](https://github.com/Yeachan-Heo/oh-my-codex/pull/3694)) |
| **[OpenCodex](https://github.com/lidge-jun/opencodex)** | ⭐ 18.3k | `TypeScript / Bun` | Portable Bun test batch execution for macOS environments without GNU `timeout` ([#5456](https://github.com/lidge-jun/opencodex/pull/5456)) |
| **[Pillow](https://github.com/python-pillow/Pillow)** | ⭐ 14.0k | `Python / C` | Raising `SyntaxError` when a SPIDER image within a stack is opened directly ([#10425](https://github.com/python-pillow/Pillow/pull/10425)) |
| **[LZ4](https://github.com/lz4/lz4)** | ⭐ 12.7k | `C` | Making `lz4cli` `--stdout` and `--to-stdout` flags consistently enable pass-through mode like `-c` ([#2062](https://github.com/lz4/lz4/pull/2062)) |
| **[SQLFluff](https://github.com/sqlfluff/sqlfluff)** | ⭐ 10.0k | `Python` | Hive dialect `GROUP BY` grammar support for trailing `WITH ROLLUP` and `WITH CUBE` clauses ([#8974](https://github.com/sqlfluff/sqlfluff/pull/8974)) |
| **[buku](https://github.com/jarun/buku)** | ⭐ 7.3k | `Python / SQLite` | Escaping SQL `LIKE` wildcards (`_` and `%`) in `--deep` and tag search queries ([#915](https://github.com/jarun/buku/pull/915)) |
| **[Trafilatura](https://github.com/adbar/trafilatura)** | ⭐ 7.1k | `Python` | Guarding baseline JSON extraction against Discourse topics whose `posts` field is not a list ([#1088](https://github.com/adbar/trafilatura/pull/1088)) |
| **[user-scanner](https://github.com/kaifcodec/user-scanner)** | ⭐ 5.6k | `Python` | Resolving non-stem validator names in library mode and rejecting malformed open CLI ranges missing an end bound ([#772](https://github.com/kaifcodec/user-scanner/pull/772), [#773](https://github.com/kaifcodec/user-scanner/pull/773)) |
| **[lancet](https://github.com/duke-git/lancet)** | ⭐ 5.3k | `Go` | **9 merged PRs** including [#419](https://github.com/duke-git/lancet/pull/419), [#421](https://github.com/duke-git/lancet/pull/421), [#422](https://github.com/duke-git/lancet/pull/422), [#423](https://github.com/duke-git/lancet/pull/423), [#424](https://github.com/duke-git/lancet/pull/424) ([All 9 merged PRs](https://github.com/duke-git/lancet/pulls?q=is%3Apr+author%3Alee3Q+is%3Amerged)) |
| **[ThinkJS](https://github.com/thinkjs/thinkjs)** | ⭐ 5.3k | `JavaScript` | Fixing `requiredWith` validator method leakage, `escapeHtml` `&quot;` entity encoding, and shared router default mutation ([#1792](https://github.com/thinkjs/thinkjs/pull/1792), [#1793](https://github.com/thinkjs/thinkjs/pull/1793), [#1794](https://github.com/thinkjs/thinkjs/pull/1794)) |
| **[Gajae Code](https://github.com/Yeachan-Heo/gajae-code)** | ⭐ 3.1k | `TypeScript` | **24 merged PRs** across provider stream/abort controls, SSE/EditorConfig/Markdown parsers, CLI/TUI handling, and session analytics ([All 24 merged PRs](https://github.com/Yeachan-Heo/gajae-code/pulls?q=is%3Apr+author%3Alee3Q+is%3Amerged)) |

<details>
<summary><b>All 24 merged PRs in Gajae Code</b></summary>
<br/>

- **AI Provider Streaming, Cancellation & Retry Controls:**
  - Honor retry headers before consuming error bodies ([#7588](https://github.com/Yeachan-Heo/gajae-code/pull/7588))
  - Parse SSE carriage-return (`\r`) line endings accurately ([#7597](https://github.com/Yeachan-Heo/gajae-code/pull/7597))
  - Honor request controls in GitLab Duo direct access ([#7366](https://github.com/Yeachan-Heo/gajae-code/pull/7366)) and clean up Ollama NDJSON response readers ([#7368](https://github.com/Yeachan-Heo/gajae-code/pull/7368))
  - Observe rejected promises on pre-aborted timeout signals ([#7347](https://github.com/Yeachan-Heo/gajae-code/pull/7347), [#7362](https://github.com/Yeachan-Heo/gajae-code/pull/7362)) and accept `kiro-codewhisperer-stream` in config API enums ([#7581](https://github.com/Yeachan-Heo/gajae-code/pull/7581))
- **CLI, TUI & Parser Fidelity:**
  - Preserve caller `argv` when parsing inline CLI option values ([#7367](https://github.com/Yeachan-Heo/gajae-code/pull/7367))
  - Strip terminal control sequences from status-line text ([#7344](https://github.com/Yeachan-Heo/gajae-code/pull/7344)) and preserve pre-yank text when cycling combining characters in TUI ([#7349](https://github.com/Yeachan-Heo/gajae-code/pull/7349))
  - Respect explicit `EditorConfig` `tab_width`/`unset` and `..` section matching ([#7346](https://github.com/Yeachan-Heo/gajae-code/pull/7346), [#7592](https://github.com/Yeachan-Heo/gajae-code/pull/7592))
  - Preserve literal content inside Markdown fences ([#7348](https://github.com/Yeachan-Heo/gajae-code/pull/7348))
- **Built-in Tools, Archive Indexing & Session Analytics:**
  - Match Vixie cron day-field semantics for stepped-star expressions ([#7578](https://github.com/Yeachan-Heo/gajae-code/pull/7578)) and accept signed exponent operands in `calc` ([#7579](https://github.com/Yeachan-Heo/gajae-code/pull/7579))
  - Preserve TAR directory/duplicate-file index fidelity ([#7370](https://github.com/Yeachan-Heo/gajae-code/pull/7370)) and `Object.prototype`-named keys in root JSON previews ([#7369](https://github.com/Yeachan-Heo/gajae-code/pull/7369))
  - Attribute managed sessions to recorded working directories and preserve stats labels/entries ([#5780](https://github.com/Yeachan-Heo/gajae-code/pull/5780), [#7350](https://github.com/Yeachan-Heo/gajae-code/pull/7350), [#7351](https://github.com/Yeachan-Heo/gajae-code/pull/7351), [#7364](https://github.com/Yeachan-Heo/gajae-code/pull/7364))
  - Validate custom-provider recipes with production loader and retain runtime Markdown consumer tests in CI PR plans ([#7352](https://github.com/Yeachan-Heo/gajae-code/pull/7352), [#7353](https://github.com/Yeachan-Heo/gajae-code/pull/7353), [#7363](https://github.com/Yeachan-Heo/gajae-code/pull/7363))

</details>

<sub><i>Merged PR counts and repository star snapshots are synced automatically via GitHub Actions.</i></sub>
<!-- AUTO-OSS:END -->
