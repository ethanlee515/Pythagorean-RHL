# Evidence and preservation notes for the human-effort narrative

These notes accompany the November 8, 2026 rewrite of
[the AI-assistance appendix](acknowledgment-of-ai-assistance.tex) following
[the proposed outline](ai-assistance-outline.md). They supplement
[the existing audit notes](AI-ASSISTANCE-NOTES.md); they do not replace or
update the frozen November 4 usage audit. No new usage is added to its totals.

The appendix now follows the human decisions within four overlapping strands:
probability analysis, program logic, compiler, and noise-flooding application.
The final subsection retains the approximate allocation by purpose. The
application is to abstract approximate HE; calling it a complete formalization
of concrete CKKS would exceed the theorem's scope.

## What the interaction counts mean

The new episode counts come from the existing `sessions.csv`,
`user-records.csv`, and `turns.csv` exports in [ai-assistance-data/](ai-assistance-data/).
The selected private rollouts were also read to check the mathematical story.
Their paths and hashes are already in `sessions.csv`; no full conversations
are copied into this repository.

- **Requests** are the audit's `request_record` events in user-facing
  conversations, after its syntactic exclusion of injected context/control
  messages and automatic goal continuations. Retries, restarts, approvals,
  syntax questions, and routine instructions remain. These are candidate
  human requests, not a count of distinct corrections.
- **Completed turns** are retained `task_complete` events. A turn can follow
  an automatic continuation, and an interrupted request can lack a completed
  turn. A request count and a completion count are therefore separate
  measurements, not necessarily one-to-one round trips.
- **Automatic continuations** are the separately classified
  `automatic_goal` records. Their count need not equal the difference between
  completed turns and requests.
- Dates of conversation events in these notes and the appendix use UTC.
  Git dates retain their recorded offsets. Calendar spans include gaps and
  do not measure attention or continuous work.

The selections below are named episodes, not an exhaustive partition of all
work on each layer. In particular, the last probability push includes
compiler obligations, and the initial compiler episode excludes later
quantitative-rule proofs. The counts must not be added to estimate total
human effort. The missing May conversations also prevent a complete count
for Pythagorean preservation or the initial Gaussian KL work.

| Episode | Selection | Requests | Completed turns | Automatic continuations |
| --- | --- | ---: | ---: | ---: |
| Final probability/assumption-discharge push | Five full conversations, June 19–21 | 60 | 82 | 26 |
| Discrete-Gaussian rule restoration | One full conversation, June 22 | 8 | 8 | 0 |
| Initial sequencing proof | One full conversation, June 9–11 | 51 | 50 | 0 |
| Missing-mass review and completion | Two full conversations, June 12–13 | 28 | 28 | 0 |
| Initial compiler construction and correctness | Twelve full conversations, June 3–6 | 47 | 45 | 0 |
| Application through the July 10 milestone | Prefix of three conversations, defined below | 46 | 297 | 269 |

### Selection manifest

Every full-conversation row below includes all events in that conversation
retained by the November 4 audit.

| Episode | Session ID | Requests | Completed turns |
| --- | --- | ---: | ---: |
| Final probability push | `019edf7f-ab0b-7373-adad-676ff93cc4db` | 7 | 7 |
| Final probability push | `019ee0cc-e3cc-7a92-9871-0e49dd6bcb5e` | 32 | 31 |
| Final probability push | `019ee2e4-9ec9-7223-8b51-0f6f79f285ed` | 12 | 12 |
| Final probability push | `019ee3d0-38d7-7e00-a640-e18d807764ad` | 3 | 6 |
| Final probability push | `019ee58d-e712-70b1-92d4-3c3f5974ea83` | 6 | 26 |
| Gaussian restoration | `019eee80-315f-7e61-acb5-c9243b8423a8` | 8 | 8 |
| Initial sequencing proof | `019eacd8-3e1e-7d63-a5f0-67061c5f888f` | 51 | 50 |
| Missing-mass review | `019ebce8-0a3b-7593-9573-7fd944a290ec` | 8 | 8 |
| Completion | `019ebeb6-6c18-7300-b084-bcd7a98117a1` | 20 | 20 |
| Initial compiler | `019e8fb1-2e3b-7231-809b-fa5fdc8551ca` | 1 | 1 |
| Initial compiler | `019e9050-ebff-7c22-95a4-ed7ea5f48332` | 2 | 2 |
| Initial compiler | `019e9066-6f3e-7ba3-aaad-07dabdc4dc8f` | 1 | 1 |
| Initial compiler | `019e906d-7fba-7693-92d4-25444a7741aa` | 1 | 1 |
| Initial compiler | `019e9071-a238-75b3-aa66-ac926d420522` | 3 | 3 |
| Initial compiler | `019e9083-9ed9-7803-ae46-1472572b10c4` | 4 | 4 |
| Initial compiler | `019e90a7-f2a7-7531-aa0b-ee209620261d` | 5 | 5 |
| Initial compiler | `019e90bf-05a3-7380-ad22-2133fb7d5005` | 4 | 4 |
| Initial compiler | `019e9149-6991-75d3-b332-717a32c1dfd8` | 2 | 2 |
| Initial compiler | `019e914f-a0ca-7180-889a-b16fbf11bc8a` | 7 | 5 |
| Initial compiler | `019e9c45-f3d2-7de2-8697-f02dc5629b3e` | 14 | 14 |
| Initial compiler | `019e9c9a-af96-7f92-a5a0-e9c747e77f24` | 3 | 3 |

The final probability push spans June 19 at 10:49:07 through June 21 at
03:57:24 UTC. Its reported completed-turn durations sum to 10.70 hours;
that is agent time under the audit's convention, not researcher labor.
The initial sequencing conversation spans June 9–11. The initial compiler
selection spans June 3 at 22:54 through June 6 at 11:32 UTC, ending around
the correctness-proof repair recorded in `9245c47`.

The application episode includes events in the following three sessions
**strictly before July 10, 2026, 04:48:51 UTC**, the timestamp of completion
commit `da878fb`:

- `019f1816-c139-7d12-8c0a-1108b4687a5f`
- `019f1edf-fab7-72b0-9ea7-7373d8b16719`
- `019f4224-099b-7d53-879f-23e05ef54fd2`

Count requests/continuations at their `timestamp_utc` and completed turns at
their `end_utc`. The first two sessions are included in full; the cutoff
restricts the third. This excludes the explicit switch to manuscript work
at source line 41136, July 10 at 04:51:50 UTC, and all subsequent mixed
writing/refactoring work in that conversation. Summed completed-turn duration
in the selected window is 61.84 hours. The July 10 milestone is provisional:
the July 11 adversary-bound correction is described separately in the text.

The counts can be reproduced from the public exports alone, without the
private conversation bodies. Run this from the manuscript directory:

```python
import csv
from collections import Counter
from datetime import datetime
from pathlib import Path

data = Path("ai-assistance-data")
sessions = list(csv.DictReader((data / "sessions.csv").open()))
requests = list(csv.DictReader((data / "user-records.csv").open()))
turns = list(csv.DictReader((data / "turns.csv").open()))
groups = {
    "probability": ["019edf7f", "019ee0cc", "019ee2e4", "019ee3d0", "019ee58d"],
    "gaussian": ["019eee80"],
    "sequencing": ["019eacd8"],
    "completion": ["019ebce8", "019ebeb6"],
    "compiler": ["019e8fb1", "019e9050", "019e9066", "019e906d",
                 "019e9071", "019e9083", "019e90a7", "019e90bf",
                 "019e9149", "019e914f", "019e9c45", "019e9c9a"],
    "application": ["019f1816", "019f1edf", "019f4224"],
}

def instant(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

for name, prefixes in groups.items():
    selected = []
    for prefix in prefixes:
        matches = [s for s in sessions if s["session_id"].startswith(prefix)]
        assert len(matches) == 1 and matches[0]["kind"] == "user"
        selected.extend(matches)
    ids = {s["session_id"] for s in selected}
    cutoff = instant("2026-07-10T04:48:51Z") if name == "application" else None
    rr = [r for r in requests if r["session_id"] in ids
          and (cutoff is None or instant(r["timestamp_utc"]) < cutoff)]
    tt = [t for t in turns if t["session_id"] in ids
          and (cutoff is None or instant(t["end_utc"]) < cutoff)]
    counts = Counter(r["category"] for r in rr)
    print(name, counts["request_record"], len(tt), counts["automatic_goal"])
```

## Additional evidence checked for this narrative

Source-line numbers refer to the private rollout identified in `sessions.csv`.
The human requests are paraphrased here; their timestamps, classifications,
and hashes are in `user-records.csv`.

| Claim | Evidence | Interpretation |
| --- | --- | --- |
| First Gaussian KL work and preservation target | Artifact `6ed6bf7`, May 6; `f68ae73`, `cfc7e93`, `b8eb9ff`, `539a2c5`, May 16 | An AI-assisted Gaussian calculation and explicit preservation target predate available conversations. These commits do not establish that the final dependency chain was already complete. |
| Early logic encodings and statements | `6e14495`, July 12, 2025; `d40b2ff`, `c2834de`, July 14 | Initial encodings, rule statements, and an admitted conversion theorem. The initial Pythagorean encoding was inductive; later versions used semantic judgments. Do not date a completed soundness proof from these statements or the July 21 commit titled “Fix broken proof,” which only repairs the theorem's application syntax. |
| AI-assisted logic work predates the retained chats | `971cfce`, May 17, 2026; `d918537`, `3183b79`, May 18 | Codex coauthor footers record assistance with judgment revisions, rule development, and a sequencing-soundness repair. These dates establish involvement by May 17–18, not the exact first AI interaction. Together with the 2025 prototypes, they explain the year boundary in subsection B. The earliest recorded AI assistance elsewhere in the artifact is the May 6, 2026 Gaussian work; May 29 dates the available conversations, not the start of assistance. |
| Human review of totalized KL | `019edbf4-0f21-79c1-89a4-7b254c5e1988`, lines 1754 and 1775, June 19 at 04:48 and 04:55 | The author asks what a nonconvergent KL sum means and how to discharge the resulting debt. The explicit finiteness requirement led to widespread interface changes. |
| LaTeX before further summability engineering | `019ee0cc-e3cc-7a92-9871-0e49dd6bcb5e`, lines 325, 943, 997, 1078 | June 19: requests an informal summability proof, then an iterated-chain-bound proof, questions sum interchange, and chooses the positive-part summability obligation next. |
| Review does not always prevent a false intermediate lemma | `019ee2e4-9ec9-7223-8b51-0f6f79f285ed`, around lines 723–893 | June 20: after resuming the proof, a proposed statement is found unsound; the author acknowledges having missed it. Avoid claiming every checkpoint detected the problem in advance. |
| Pinsker proof strategy and organization | `019ee58d-e712-70b1-92d4-3c3f5974ea83`, lines 5824, 5912, 6072, 6099, 6272 | June 21: requests LaTeX, discusses binary data processing and the calculus step, and directs top-down/depth-first organization. `9799d05` records completion of Pinsker and compiler-rule analysis, still relative to inherited library assumptions. |
| Gaussian convergence review after the logic changes | `019eee80-315f-7e61-acb5-c9243b8423a8`, lines 6, 790–1016, 1387–1416; `46da66d` | June 22: restore sampling rules, revisit `finite_kl` and injective pushforwards, then reconnect the proof. The commit is dated June 23 at +08:00, equivalent to June 22 UTC. |
| Author-directed compiler redesign and proof repair | `019e9c45-f3d2-7de2-8697-f02dc5629b3e`, lines 6 and 48; `019e9c9a-af96-7f92-a5a0-e9c747e77f24`, line 6 | June 6: the author says the intended selected-call/resumption behavior was lost and asks to restore it; correctness is then reproved for the revised construction. |
| Adversary-independent security-bound correction | `019f4224-099b-7d53-879f-23e05ef54fd2`, lines 48493, 48657, 48781; artifact `06fa6c5` | July 11 at 04:51:09: the author challenges a bound uniform over all adversaries, including unbounded ones. At 05:02 the author requests an adversary-dependent conclusion exposing the reduction, then asks to explain the external efficiency obligation. The correction is after the July 10 milestone and outside its interaction-count window. |

The hidden-mixture, missing-mass, chart-repair, and pruning evidence remains
in the [existing chronology](AI-ASSISTANCE-NOTES.md#chronology-and-supporting-records)
and [recovery-episode provenance](AI-ASSISTANCE-NOTES.md#provenance-of-the-selected-recovery-episodes).
The chart argument and the adversary-dependent bound are separate issues;
neither should be described merely as fixing Rocq syntax.

## Material retained outside the shorter appendix

The complete earlier wording is also recoverable from the existing manuscript
revision `9e0ae42b3ceb01965a95144ad90d6f5c6639e90a`, without relying on these
summaries:

```sh
git show 9e0ae42b3ceb01965a95144ad90d6f5c6639e90a:acknowledgment-of-ai-assistance.tex
```

The rewrite removes detailed accounting tables and instrumentation from the
paper's narrative, while preserving their sources:

| Earlier material | Retained location |
| --- | --- |
| Audit inclusion rules, missing Copilot records, source hashes, model identifiers, and complete core/subagent/review/upstream totals | [Sources and selection](AI-ASSISTANCE-NOTES.md#sources-and-selection), [quantitative checks](AI-ASSISTANCE-NOTES.md#quantitative-checks-for-the-narrative), `sessions.csv`, `summary.json` |
| Monthly table and its whole-session month assignment | `monthly.csv`; [accounting conventions](AI-ASSISTANCE-NOTES.md#accounting-conventions-and-cautions) |
| Completed-turn duration sum versus union, unmatched starts, tools, compactions, request records, and counter decreases | [Accounting conventions](AI-ASSISTANCE-NOTES.md#accounting-conventions-and-cautions), `turns.csv`, `unmatched-starts.csv`, `summary.json` |
| API rates, source URLs, cache assumptions, formula, long-context premiums, model-specific totals, and unpriced review | [Hypothetical API equivalent](AI-ASSISTANCE-NOTES.md#hypothetical-api-list-price-equivalent), `api-pricing.json`, `api-cost-*.csv` and `api-cost-summary.json` |
| The frozen November 4 documentation prefix and purpose-boundary rules | [Three-way purpose allocation](AI-ASSISTANCE-NOTES.md#approximate-three-way-allocation-by-purpose), `bucket-snapshot.json`, `bucket-rules.json`, `purpose-*.csv` and `purpose-summary.json` |
| Pinned Git revisions, coauthor footers, cumulative insertions/deletions, individual pruning commits | [Quantitative checks](AI-ASSISTANCE-NOTES.md#quantitative-checks-for-the-narrative), [recovery provenance](AI-ASSISTANCE-NOTES.md#provenance-of-the-selected-recovery-episodes), `commits.csv`, `summary.json` |
| Costs and time of the heap-counter detour, hidden-mixture discussion, completion repair, chart-recovery interval, and pruning | [Recovery provenance](AI-ASSISTANCE-NOTES.md#provenance-of-the-selected-recovery-episodes), [episode API equivalents](AI-ASSISTANCE-NOTES.md#hypothetical-api-list-price-equivalent), `episodes.csv`, `api-cost-by-episode.csv` |

All data filenames in the table are relative to `ai-assistance-data/`.
These are locally reported usage measurements, not invoices, a causal cost
of mistakes, or a division of authorship. In particular, the chart-recovery
window includes useful work on other application obligations.

The former persistent-goal examples are also retained in `goal-events.csv`:

| Last selected snapshot (UTC) | Goal-accounting tokens | Goal-accounting seconds | Status |
| --- | ---: | ---: | --- |
| July 2, 03:07:50 | 3,508,334 | 14,249 | paused |
| July 2, 23:53:25 | 5,787,219 | 35,655 | paused |
| July 10, 03:20:01 | 22,341,787 | 136,552 (37.9 hours) | paused |

These goal counters have their own scope and accounting. Do not add them to
conversation totals or infer from `paused` that the eventual proof failed.

### Untested reconstruction conjecture

The former opening included the following author conjecture, recorded during
the October 13 revision:

> As of October 2026, we consider it plausible that an agent using GPT-6 Astra,
> given this manuscript with its Rocq excerpts (including those in Appendix E)
> removed and access to Rocq and the stated dependencies, could independently
> recreate the full formalization from scratch for at most US$200 in model
> usage. We have not performed this experiment; both its success and its cost
> remain conjectural.

“Appendix E” here means the formal-interface-excerpts appendix identified by
`app:formal-interface-excerpts`, independently of future renumbering.
The human-effort narrative keeps the general historical qualification and
the absence of a reconstruction experiment; the specific model and US$200
budget are retained here for author review. The measured development cost
does not test that conjecture: it includes design exploration, failed routes,
review, and manuscript preparation. A future reconstruction experiment would
need to exclude access to the existing artifact, including via manuscript
links, while allowing the stated dependencies.

## Remaining limits

No missing dates or counts are filled from guesses. In particular, the
records do not establish the date of the original LaTeX design, the total
number of early probability interactions, total researcher hours, or a
counterfactual time/cost saving from author skepticism. No unresolved factual
placeholder is needed in the LaTeX; the limits are stated directly.

## Recovery check on November 8, 2026

Absence from the inspected stores does not establish expiration or deletion.
A further read-only inventory found 505 Codex rollouts across the active and
archived directories; the oldest session metadata is May 19, 2026,
02:02:43 UTC. The local thread database has the same earliest creation time.
Thirteen rollouts predate May 29, but none contains the checked project names
or distinctive theorem identifiers. No earlier project conversation was
recovered. Current configuration does not explicitly set `history.persistence`
or `history.max_bytes`; this does not establish the historical settings or
explain the missing early records.

The additional search did find a project-specific **Copilot transcript** in
VS Code workspace storage, separate from the global Copilot database inspected
in the November 4 audit:

```text
~/.vscode-server/data/User/workspaceStorage/0baff809a2a4f50a510bc5fcee318e13/GitHub.copilot-chat/transcripts/de6aaa72-b41e-4e56-a61a-e97982d34e21.jsonl
```

Its recorded events span June 14, 2026, 09:56:04–10:26:10 UTC. Its SHA-256 is
`1bcd7748c7a20b8a91ac26455949c5311ab4008d1731b08b72028c307eb87863`.
It concerns `codeLinkCompileCallsFromTraceS_decompose` and the use of
SSProve's `code_link_bind` and monad laws. Five user-message records survive;
the file starts with an assistant response, so it does not contain the initial
user prompt. Its event schema differs from the Codex exports and its agent
turn markers must not be interpreted as the completed Codex turns counted
above. No private conversation body is copied here.

This find expands the available qualitative evidence, without changing the
frozen Codex usage totals or recovering the early-May conversations. The
earlier audit's statement about the inspected global Copilot database remains
specific to that database; it must not be generalized to all editor storage.

For possible recovery elsewhere, official OpenAI documentation identifies
[active and archived local transcript directories](https://learn.chatgpt.com/docs/reference/troubleshooting)
and documents [exporting an available conversation with `/export`](https://learn.chatgpt.com/docs/developer-commands).
These instructions do not establish a server-side restore mechanism for a
missing local transcript. Other machines, alternate Codex homes, backups,
and any separately saved cloud conversations remain possible sources; their
existence has not been established by this local check.
