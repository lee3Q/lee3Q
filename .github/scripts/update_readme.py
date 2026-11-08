#!/usr/bin/env python3
"""Automatically update dynamic PR counts, star counts, and OSS contribution tables in README.md."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

USERNAME = "lee3Q"
FLAGSHIP_REPO = "Q00/ouroboros"
COLLAB_OWNERS = {"sergiobuilds", "ouro-labs"}

# Curated concise metadata for known upstream repositories.
# If new PRs are merged into these repos, their PR links (#num) are appended automatically.
# If a PR is merged into a brand-new repository not listed here, a row is generated automatically
# from the repository's GitHub metadata and PR titles.
CURATED_REPOS: dict[str, dict[str, str]] = {
    "Yeachan-Heo/oh-my-claudecode": {
        "display": "Oh My ClaudeCode (OMC)",
        "stack": "TypeScript",
        "summary": "Preflight context-threshold validation and read-budget env override guards preventing malformed values from silently activating",
    },
    "Yeachan-Heo/oh-my-codex": {
        "display": "Oh My Codex (OMX)",
        "stack": "TypeScript",
        "summary": "Stripping OSC terminal-control sequences from notification text and surfacing resolved config paths in `doctor`",
    },
    "lidge-jun/opencodex": {
        "display": "OpenCodex",
        "stack": "TypeScript / Bun",
        "summary": "Portable Bun test batch execution for macOS environments without GNU `timeout`",
    },
    "python-pillow/Pillow": {
        "display": "Pillow",
        "stack": "Python / C",
        "summary": "Raising `SyntaxError` when a SPIDER image within a stack is opened directly",
    },
    "lz4/lz4": {
        "display": "LZ4",
        "stack": "C",
        "summary": "Making `lz4cli` `--stdout` and `--to-stdout` flags consistently enable pass-through mode like `-c`",
    },
    "sqlfluff/sqlfluff": {
        "display": "SQLFluff",
        "stack": "Python",
        "summary": "Hive dialect `GROUP BY` grammar support for trailing `WITH ROLLUP` and `WITH CUBE` clauses",
    },
    "jarun/buku": {
        "display": "buku",
        "stack": "Python / SQLite",
        "summary": "Escaping SQL `LIKE` wildcards (`_` and `%`) in `--deep` and tag search queries",
    },
    "adbar/trafilatura": {
        "display": "Trafilatura",
        "stack": "Python",
        "summary": "Guarding baseline JSON extraction against Discourse topics whose `posts` field is not a list",
    },
    "kaifcodec/user-scanner": {
        "display": "user-scanner",
        "stack": "Python",
        "summary": "Resolving non-stem validator names in library mode and rejecting malformed open CLI ranges missing an end bound",
    },
    "thinkjs/thinkjs": {
        "display": "ThinkJS",
        "stack": "JavaScript",
        "summary": "Fixing `requiredWith` validator method leakage, `escapeHtml` `&quot;` entity encoding, and shared router default mutation",
    },
    "Yeachan-Heo/gajae-code": {
        "display": "Gajae Code",
        "stack": "TypeScript",
        "summary_template": "**{count} merged PRs** across provider stream/abort controls, SSE/EditorConfig/Markdown parsers, CLI/TUI handling, and session analytics ([All {count} merged PRs](https://github.com/Yeachan-Heo/gajae-code/pulls?q=is%3Apr+author%3Alee3Q+is%3Amerged))",
    },
}

OUROBOROS_CURATED_PR_NUMBERS = {
    1764, 2639, 2640, 2745, 2749, 2758, 2842,
    1622, 1630, 2567, 2635, 2636, 2637, 2638, 2746, 2748,
    1568, 1595, 2034, 2406, 2411, 2420, 2499, 2564, 2846, 2847, 2860,
    2415, 2417, 2642, 2643, 2660, 2668, 2669, 2673, 2819,
}

GAJAE_CURATED_PR_NUMBERS = {
    7588, 7597, 7366, 7368, 7347, 7362, 7581,
    7367, 7349, 7344, 7346, 7592, 7348,
    7578, 7579, 7370, 7369, 5780, 7350, 7351, 7364, 7352, 7353, 7363,
}


def get_github_token() -> str | None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token.strip()
    try:
        out = subprocess.check_output(["gh", "auth", "token"], text=True, stderr=subprocess.DEVNULL)
        return out.strip() or None
    except Exception:
        return None


def gh_api_get(url: str, token: str | None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USERNAME}-readme-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_all_external_merged_prs(token: str | None) -> tuple[int, list[dict[str, Any]]]:
    query = f"is:pr author:{USERNAME} is:merged is:public -user:{USERNAME}"
    encoded_q = urllib.parse.quote(query)
    items: list[dict[str, Any]] = []
    total_count = 0

    for page in range(1, 11):
        url = f"https://api.github.com/search/issues?q={encoded_q}&per_page=100&page={page}&sort=updated&order=desc"
        data = gh_api_get(url, token)
        if page == 1:
            total_count = int(data.get("total_count", 0))
        batch = data.get("items", [])
        if not batch:
            break
        items.extend(batch)
        if len(items) >= total_count or len(batch) < 100:
            break

    return total_count, items


def format_stars(stars: int) -> str:
    if stars >= 1000:
        return f"⭐ {stars / 1000:.1f}k"
    return f"⭐ {stars}"


def clean_pr_title(title: str) -> str:
    cleaned = re.sub(r"^(fix|feat|refactor|docs|chore|perf|test)(\([^)]+\))?:\s*", "", title.strip(), flags=re.IGNORECASE)
    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]
    return cleaned.replace("|", "\\|")


def replace_marker_block(content: str, marker: str, new_body: str) -> str:
    pattern = re.compile(
        rf"(<!-- {re.escape(marker)}:START -->).*?(<!-- {re.escape(marker)}:END -->)",
        re.DOTALL,
    )
    if not pattern.search(content):
        raise RuntimeError(f"Marker {marker} not found in README.md")
    return pattern.sub(lambda m: f"{m.group(1)}\n{new_body}\n{m.group(2)}", content)


def build_sections(token: str | None) -> tuple[str, str, str]:
    total_external_prs, items = fetch_all_external_merged_prs(token)

    by_repo: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        repo_url = item.get("repository_url", "")
        repo_full = repo_url.replace("https://api.github.com/repos/", "")
        if not repo_full:
            continue
        by_repo.setdefault(repo_full, []).append(item)

    for repo_prs in by_repo.values():
        repo_prs.sort(key=lambda x: int(x["number"]))

    # Fetch repo info (stars, language)
    repo_meta: dict[str, dict[str, Any]] = {}
    for repo_full in by_repo:
        try:
            meta = gh_api_get(f"https://api.github.com/repos/{repo_full}", token)
            repo_meta[repo_full] = {
                "stars": int(meta.get("stargazers_count", 0)),
                "language": meta.get("language") or "Code",
                "html_url": meta.get("html_url") or f"https://github.com/{repo_full}",
            }
        except urllib.error.HTTPError:
            repo_meta[repo_full] = {
                "stars": 0,
                "language": "Code",
                "html_url": f"https://github.com/{repo_full}",
            }

    ouroboros_prs = by_repo.get(FLAGSHIP_REPO, [])
    ouroboros_count = len(ouroboros_prs)
    ouroboros_stars = format_stars(repo_meta.get(FLAGSHIP_REPO, {}).get("stars", 6300))

    # Filter upstream OSS repos (exclude flagship and small 0-star collab repos under COLLAB_OWNERS)
    upstream_repos: list[str] = []
    for repo_full in by_repo:
        owner = repo_full.split("/")[0].lower()
        if repo_full == FLAGSHIP_REPO:
            continue
        if owner in COLLAB_OWNERS and repo_meta.get(repo_full, {}).get("stars", 0) < 20:
            continue
        upstream_repos.append(repo_full)

    upstream_repos.sort(
        key=lambda r: (repo_meta.get(r, {}).get("stars", 0), len(by_repo[r])),
        reverse=True,
    )

    total_public_repos = 1 + len(upstream_repos)

    # 1. Badges block
    badges_block = "\n".join(
        [
            "[![Ouro Labs](https://img.shields.io/badge/Ouro_Labs-Co--founder-0F172A?style=flat-square)](https://ourolabs.vercel.app/)",
            f"[![Ouroboros](https://img.shields.io/badge/Ouroboros-Core_Maintainer_({ouroboros_count}_Merged_PRs)-4338CA?style=flat-square&logo=github&logoColor=white)](https://github.com/Q00/ouroboros/pulls?q=is%3Apr+author%3A{USERNAME}+is%3Amerged)",
            f"[![Upstream OSS](https://img.shields.io/badge/Open_Source-{total_external_prs}_Merged_PRs_Across_{total_public_repos}_Projects-047857?style=flat-square&logo=git&logoColor=white)](https://github.com/search?q=is%3Apr+author%3A{USERNAME}+is%3Amerged+-user%3A{USERNAME}&type=pullrequests)",
        ]
    )

    # 2. Ouroboros section
    uncategorized_ouroboros = [
        pr for pr in sorted(ouroboros_prs, key=lambda x: int(x["number"]), reverse=True)
        if int(pr["number"]) not in OUROBOROS_CURATED_PR_NUMBERS
    ]
    recent_ouroboros_row = ""
    if uncategorized_ouroboros:
        links = ", ".join(
            f"[#{pr['number']}]({pr['html_url']})" for pr in uncategorized_ouroboros[:12]
        )
        recent_ouroboros_row = (
            f"\n| **Additional & Recent Merged PRs** | Continuing maintenance across CLI, runtime adapters, docs, and verification checks. | {links} |"
        )

    ouroboros_block = f"""### [Ouroboros](https://github.com/Q00/ouroboros) · {ouroboros_stars} — *Core Maintainer*

**Open-source Agent OS for Specification-First AI Software Development**

I am a core maintainer of **Ouroboros** and a co-founder of **[Ouro Labs](https://ourolabs.vercel.app/)**. My work focuses on turning ambiguous human requests into explicit specifications (`Seed`), coordinating multi-runtime agent execution, and preserving verifiable evidence so people can audit the outcome.

- **Verification & Evidence Integrity:** Binding file-modification claims to observed tool-call receipts, isolating source checks from runtime assertions, and rejecting malformed semantic evaluation scores.
- **Execution & Lifecycle Recovery:** Background-job polling and recovery, cancellation lifecycle management, checkpoint compatibility, and unified runner assembly.
- **Multi-Runtime Adapters & Diagnostics:** Zcode runtime and LLM adapters, Antigravity stream normalization, provider routing across OpenAI/Anthropic/Gemini, and `doctor` MCP/installation probes.
- **Intent Alignment & Drift Control:** Structured ambiguity ledgers (`B2`), semantic goal-drift checks, unanswered interview round floors, and locale-independent UTF-8 handling.

👉 **[All {ouroboros_count} merged PRs in `Q00/ouroboros`](https://github.com/Q00/ouroboros/pulls?q=is%3Apr+author%3A{USERNAME}+is%3Amerged)**

<details>
<summary><b>Selected Ouroboros contributions by subsystem</b></summary>
<br/>

| Area | Scope | Merged PRs |
| :--- | :--- | :--- |
| **Verification & Evidence** | Bound `pathlib` write claims to execution records; linked wrapper test receipts to accepted Bash attempts; separated source checks from runtime assertions; captured native tool evidence; rejected malformed semantic scores. | [#1764](https://github.com/Q00/ouroboros/pull/1764), [#2639](https://github.com/Q00/ouroboros/pull/2639), [#2640](https://github.com/Q00/ouroboros/pull/2640), [#2745](https://github.com/Q00/ouroboros/pull/2745), [#2749](https://github.com/Q00/ouroboros/pull/2749), [#2758](https://github.com/Q00/ouroboros/pull/2758), [#2842](https://github.com/Q00/ouroboros/pull/2842) |
| **Orchestrator & Job Recovery** | Hardened MCP background-job polling and recovery; recovered artifact contracts and QA environments; extracted Phase 3 cancellation lifecycle; unified public run builder assembly; bounded workspace fingerprint scans. | [#1622](https://github.com/Q00/ouroboros/pull/1622), [#1630](https://github.com/Q00/ouroboros/pull/1630), [#2567](https://github.com/Q00/ouroboros/pull/2567), [#2635](https://github.com/Q00/ouroboros/pull/2635), [#2636](https://github.com/Q00/ouroboros/pull/2636), [#2637](https://github.com/Q00/ouroboros/pull/2637), [#2638](https://github.com/Q00/ouroboros/pull/2638), [#2746](https://github.com/Q00/ouroboros/pull/2746), [#2748](https://github.com/Q00/ouroboros/pull/2748) |
| **Runtime Adapters & Diagnostics** | Implemented Zcode runtime backend and LLM adapter; built installation `doctor` and local stdio MCP probes; hardened Codex cold starts and locale-independent UTF-8 seed/source decoding. | [#1568](https://github.com/Q00/ouroboros/pull/1568), [#1595](https://github.com/Q00/ouroboros/pull/1595), [#2034](https://github.com/Q00/ouroboros/pull/2034), [#2406](https://github.com/Q00/ouroboros/pull/2406), [#2411](https://github.com/Q00/ouroboros/pull/2411), [#2420](https://github.com/Q00/ouroboros/pull/2420), [#2499](https://github.com/Q00/ouroboros/pull/2499), [#2564](https://github.com/Q00/ouroboros/pull/2564), [#2846](https://github.com/Q00/ouroboros/pull/2846), [#2847](https://github.com/Q00/ouroboros/pull/2847), [#2860](https://github.com/Q00/ouroboros/pull/2860) |
| **Intent Alignment & Routing** | Built typed ambiguity evidence ledger (`B2`); floored ambiguity for unanswered interview rounds; semantic goal-drift checks; quality-first model routing and OpenAI/Anthropic/Gemini compatibility. | [#2415](https://github.com/Q00/ouroboros/pull/2415), [#2417](https://github.com/Q00/ouroboros/pull/2417), [#2642](https://github.com/Q00/ouroboros/pull/2642), [#2643](https://github.com/Q00/ouroboros/pull/2643), [#2660](https://github.com/Q00/ouroboros/pull/2660), [#2668](https://github.com/Q00/ouroboros/pull/2668), [#2669](https://github.com/Q00/ouroboros/pull/2669), [#2673](https://github.com/Q00/ouroboros/pull/2673), [#2819](https://github.com/Q00/ouroboros/pull/2819) |{recent_ouroboros_row}

</details>"""

    # 3. Upstream OSS table & Gajae Code details
    table_rows: list[str] = []
    for repo_full in upstream_repos:
        prs = by_repo[repo_full]
        meta = repo_meta.get(repo_full, {})
        stars_str = format_stars(meta.get("stars", 0))
        repo_url = meta.get("html_url", f"https://github.com/{repo_full}")
        curated = CURATED_REPOS.get(repo_full)

        if curated:
            display = curated["display"]
            stack = curated["stack"]
            if "summary_template" in curated:
                desc_col = curated["summary_template"].format(count=len(prs))
            else:
                pr_links = ", ".join(f"[#{pr['number']}]({pr['html_url']})" for pr in prs)
                desc_col = f"{curated['summary']} ({pr_links})"
        else:
            display = repo_full.split("/")[1]
            stack = meta.get("language") or "Code"
            if len(prs) <= 3:
                parts = [f"{clean_pr_title(pr['title'])} ([#{pr['number']}]({pr['html_url']}))" for pr in prs]
                desc_col = "; ".join(parts)
            else:
                pr_links = ", ".join(f"[#{pr['number']}]({pr['html_url']})" for pr in prs[:5])
                search_url = f"https://github.com/{repo_full}/pulls?q=is%3Apr+author%3A{USERNAME}+is%3Amerged"
                desc_col = f"**{len(prs)} merged PRs** including {pr_links} ([All {len(prs)} merged PRs]({search_url}))"

        table_rows.append(f"| **[{display}]({repo_url})** | {stars_str} | `{stack}` | {desc_col} |")

    gajae_prs = by_repo.get("Yeachan-Heo/gajae-code", [])
    gajae_count = len(gajae_prs)
    extra_gajae = [
        pr for pr in sorted(gajae_prs, key=lambda x: int(x["number"]), reverse=True)
        if int(pr["number"]) not in GAJAE_CURATED_PR_NUMBERS
    ]
    extra_gajae_lines = ""
    if extra_gajae:
        items_str = "\n".join(
            f"  - {clean_pr_title(pr['title'])} ([#{pr['number']}]({pr['html_url']}))"
            for pr in extra_gajae
        )
        extra_gajae_lines = f"\n- **Recent Merged Contributions:**\n{items_str}"

    oss_block = f"""| Project | Stars | Stack | Merged Contributions |
| :--- | :---: | :--- | :--- |
{chr(10).join(table_rows)}

<details>
<summary><b>All {gajae_count} merged PRs in Gajae Code</b></summary>
<br/>

- **AI Provider Streaming, Cancellation & Retry Controls:**
  - Honor retry headers before consuming error bodies ([#7588](https://github.com/Yeachan-Heo/gajae-code/pull/7588))
  - Parse SSE carriage-return (`\\r`) line endings accurately ([#7597](https://github.com/Yeachan-Heo/gajae-code/pull/7597))
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
  - Validate custom-provider recipes with production loader and retain runtime Markdown consumer tests in CI PR plans ([#7352](https://github.com/Yeachan-Heo/gajae-code/pull/7352), [#7353](https://github.com/Yeachan-Heo/gajae-code/pull/7353), [#7363](https://github.com/Yeachan-Heo/gajae-code/pull/7363)){extra_gajae_lines}

</details>

<sub><i>Merged PR counts and repository star snapshots are synced automatically via GitHub Actions.</i></sub>"""

    return badges_block, ouroboros_block, oss_block


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    readme_path = repo_root / "README.md"
    original = readme_path.read_text(encoding="utf-8")

    token = get_github_token()
    badges_block, ouroboros_block, oss_block = build_sections(token)

    updated = original
    updated = replace_marker_block(updated, "AUTO-BADGES", badges_block)
    updated = replace_marker_block(updated, "AUTO-OUROBOROS", ouroboros_block)
    updated = replace_marker_block(updated, "AUTO-OSS", oss_block)

    if updated != original:
        readme_path.write_text(updated, encoding="utf-8")
        print("README.md updated successfully.")
    else:
        print("README.md is already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
