# Evidence for the AI-assistance appendix

Working notes for the authors; this file is not an input to the manuscript or
its source-package script. The appendix is in
`acknowledgment-of-ai-assistance.tex` and is included after the technical
appendices in both manuscript formats.

The account combines the author's recollection supplied on October 13, 2026,
the local Git histories, and retained Codex conversations. The relevant local
conversations located for this reconstruction begin on May 29, 2026. Earlier
AI assistance is recorded in Git, but the available conversations do not
establish its full extent. Git coauthor footers establish recorded assistance,
not a percentage of authorship; their absence does not establish that work was
entirely manual. Dates below follow the commit's recorded date or, for
conversations, its UTC timestamp.

## Chronology and supporting records

| Episode | Evidence | What it supports |
| --- | --- | --- |
| Initial logic encodings, July 2025 | Artifact commits `6e14495`, `d40b2ff`, `c2834de` | Judgments and initial inference rules existed well before the intensive 2026 proof work. Their manual origin and the preceding LaTeX design are the author's recollection. |
| FHE interfaces and games, July–August 2025 | Artifact commits `6abc881`, `67e8fe1`, `766ce5c`, `34b7e9d` | Early correctness, IND-CPA, IND-CPAD, and security-target statements. `34b7e9d` explicitly contains an admitted theorem and placeholder noise/security parameters; the final quantitative statement was not already complete. |
| Early manuscript | Manuscript initial import `257a030`, September 2025 | LaTeX judgments, proposed rules, a soundness subsection, and the intended square-root composition argument existed in the early draft. The import date does not date the original writing. |
| Return to AI-assisted proofs, May 2026 | Artifact commits `6ed6bf7`, `f68ae73`, `b8eb9ff`, `539a2c5`, `3183b79`, `2ba4a9c` | Work resumed in May, rather than only in summer. Some probability work records both Codex and Copilot assistance; proposed sequence rules required soundness repairs. |
| Nominal migration, May 28–29 | Artifact commits `bdb3b68`, `85a8e2f`, `2d388f4` | Adoption of the nominal extension preceded the trace compiler and involved Codex-assisted interface repairs. |
| Need for adaptive factoring, May 31 | Session `019e7d58-95c7-7060-8ff9-3e61eca1eacc`, initial user message | The author already identified the query-counting problem and asked about compiling general adversaries into factored ones. |
| Trace/replay construction, June 3–4 | Artifact commits `c167990`, `e7609e2`, `7460a2b`; sessions `019e8fb1-2e3b-7231-809b-fa5fdc8551ca` and `019e90a7-f2a7-7531-aa0b-ee209620261d` | The author supplied a partial implementation for review, including new suspension/traversal scaffolding, and Codex implemented its TODO. The earlier trace/replay commit also records Codex assistance, so the entire skeleton should not be attributed exclusively to the author. The author challenged an unnecessary bounded-call premise and noticed that residual calls require linking. |
| Compiler correctness, June 4 | Session `019e90bf-05a3-7380-ad22-2133fb7d5005`; artifact commits `83bb12b`, `6f796d0`, `501ea2c` | An explicit author request to prove correctness or break it into lemmas, followed by Codex-assisted proof work. The first proof was subsequently repaired and the construction revised. |
| Zero-budget coordinates, June 7 | Session `019e9fbc-8458-7c13-8389-403a7a23eba0`, especially messages at 02:10, 02:11, 02:35, and 02:53 UTC; artifact commit `162cc37` | The author questioned mixture preservation; Codex provided a hidden-mixture counterexample; the discussion retained a zero-budget branch coordinate. The author also questioned whether dropping it would be sound. These coordinates address conditioning, beyond simplifying proofs. |
| Missing mass and completion, June 12–13 | Sessions `019ebce8-0a3b-7593-9573-7fd944a290ec` and `019ebeb6-6c18-7300-b084-bcd7a98117a1`; artifact commits `b81d93b`, `4242f48`, `6a30c03`, `a53cf79` | The author identified a false full-mass implication, asked about null programs, and proposed reusing completion. The completed judgment, sequencing proof, and conversion rule were developed interactively. |
| Extended proof tasks, June 20–21 | Sessions `019ee3d0-38d7-7e00-a640-e18d807764ad` and `019ee58d-e712-70b1-92d4-3c3f5974ea83`; artifact commit `9799d05` | Delegation of extended assumption-discharge work, including compiler and Pinsker analysis, with author checkpoints and preference for a top-down proof. |
| Application proof, June 30–July | Sessions `019f1816-c139-7d12-8c0a-1108b4687a5f`, `019f1edf-fab7-72b0-9ea7-7373d8b16719`, and `019f4224-099b-7d53-879f-23e05ef54fd2` | Explicit persistent-goal requests to prove the noise-flooding result from the existing outline and compiler rule, with progress records and intervening review. |
| Chart-assumption correction, July 9–10 | Session `019f4224-099b-7d53-879f-23e05ef54fd2`, July 9 at 15:27 and 15:44 UTC; artifact commits `5021745`, `e526e7f`, `da878fb` | The author challenged `finite_common_inverse_isometry_encoding` and proposed sample-then-postprocess reasoning. The subsequent proof used origin-centered chart translation and removed the problematic proof route. |
| H0–H6 presentation, July 10 | Same session, user messages at 11:06, 12:24, 12:39, 12:45, and **12:50:36 UTC**, then Codex responses at 12:50–12:51; manuscript commit `54a48db` | Codex drafted and explained the detailed chain, but the author explicitly proposed the seven-stage organization, adding original and linked games before the compiled representation. It was not entirely an AI-originated presentation. |
| Conceptual games versus implementation stages, late July | Session `019f9f4e-754f-78c0-8780-badace3928e5`; manuscript commit `7d7df47` | Further author feedback questioned treating all seven stages as cryptographic hybrids, leading to the distinction retained in the current draft. |
| Broader manuscript revisions | Manuscript commits `9e23aef`, `53558da`, `9f91a0c` and the associated July–August sessions | Extensive Codex drafting, restructuring, and repeated author feedback; the existing acknowledgment was retained rather than removed. |

Recorded session metadata identifies `gpt-5.5` for the inspected May–July
proof sessions, `gpt-5.6-sol` for subsequent manuscript sessions, and
`gpt-6.1-sol` for the inspected October revisions. Some smaller editorial
sessions used other models. These identifiers describe major observed phases,
not every model or every interaction, and are retained here rather than in the
manuscript's opening historical note.

The October 13 revision adds the author's conjecture that an independent
GPT-6 Astra agent could reconstruct the full formalization from the manuscript
with Rocq excerpts removed, for at most US$200 in model usage. No reconstruction
experiment or cost measurement has been performed. A future experiment would
need to exclude access to the existing artifact, including through manuscript
links, while permitting the stated dependencies.
[Official GPT-6 Astra documentation](https://developers.openai.com/api/docs/models/gpt-6-astra),
checked on October 13, lists standard token rates of US$10 per million input
tokens and US$50 per million output tokens, with different rates for caching,
long contexts, and other processing modes. These rates do not establish the
total cost or feasibility of reconstructing this development. The appendix
therefore explicitly presents both the proposed outcome and budget as
conjectural.

The current trusted-base discussion is authoritative for the final
assumptions. This historical reconstruction is separate from the Rocq
assumption audit performed when upgrading the artifact's dependencies.

## November 4, 2026 local measurement audit

The appendix now includes measurements as well as the historical narrative.
The extraction cutoff is **2026-11-04 00:00:00 UTC, exclusive**, so the
conversation conducting this audit is excluded. All episode timestamps below
are UTC; Git's original author and committer offsets are preserved in the CSV.
No commits were made for this audit.

Run from the artifact root:

```sh
python3 Pythagorean-RHL/scripts/audit-ai-assistance.py
```

The script requires Python 3.11 or later and Git, with no third-party packages
or network access. `--codex-home` selects a different local Codex store;
`--output` selects an output directory. The default Git references are pinned
to artifact `4b8625d11f908dc72428493634a3ec3e19a09b16` and manuscript
`e6035b21d269f57adbda96ef38102eec9fe5d938`, rather than floating `HEAD`s.
The private source conversations are necessary to regenerate the usage data;
Git statistics alone can be checked from the repositories. Log migrations or
new unrelated sessions can change source hashes or the inventory's scanned
file count without changing the selected historical measurements.

To calculate the hypothetical API equivalent from the frozen inventory and
the dated rate snapshot, also run:

```sh
python3 Pythagorean-RHL/scripts/price-ai-assistance.py
```

This second script does not change the usage audit or query the API. It checks
the selected source-log hashes before repricing their counters.

The subsequent approximate allocation by purpose is reproduced with:

```sh
python3 Pythagorean-RHL/scripts/bucket-ai-assistance.py
```

It preserves the preceding historical exports and adds a fixed prefix of the
November 4 documentation conversation, recorded in `bucket-snapshot.json`.
The prefix can be checked and read even after the live conversation grows.

### Sources and selection

Inspected sources were `~/.codex/sessions/`,
`~/.codex/archived_sessions/`, the read-only `state_5.sqlite`,
`goals_1.sqlite`, `thread_history_1.sqlite`, and `logs_2.sqlite` stores, the
artifact and manuscript Git histories, and the VS Code server's Copilot
session store. No credentials, account identifiers, raw conversation bodies,
or unrelated research conversations are included in the export.

Of 482 rollout files present when extracted, 140 are selected:

| Scope | Threads | Selection rule |
| --- | ---: | --- |
| Core, user-facing | 126 | 124 threads in the artifact working directory, plus the two manuscript threads explicitly identified below |
| Core, delegated work | 3 | Child sessions in the same working directory; their input messages are agent tasks, not human prompts |
| Core, automatic action review | 6 | Guardian sessions, identified by metadata, excluded from the user-facing totals |
| Upstream support | 5 | Explicitly identified supporting MathComp contribution conversations, listed in the script |

The two core conversations outside the artifact working directory are
`019f8cc3-ed82-7a63-bc09-dd8a951d35be` (CSF manuscript restructuring) and
`019f9d79-ce2a-77c3-91ec-b14b43663950` (SSProve syntax and semantics appendix).
The five upstream threads concern building Analysis, staging and polishing
reusable lemmas, grafting them upstream, and responding to upstream review.
Mending presentation-slide work is excluded, as are all other research
projects. The exact ID allowlists are in the script.

All selected final token totals were independently reconciled against
`state_5.sqlite.threads.tokens_used`: **140 matches, no missing rows, no
discrepancies**. The earliest selected core event is
2026-05-29 06:53:46.878 UTC and the last is
2026-10-28 22:59:44.628 UTC. Metadata start times are exported separately;
event timestamps, not filenames, determine the reported period.

The local Copilot database at
`~/.vscode-server/data/User/globalStorage/github.copilot-chat/session-store.db`
contains 12 sessions, but none has a project working directory/repository or
an associated file path identifying Mending/Pythagorean-RHL. Thus its contents
do not extend this project's measured history. This does **not** establish
that Copilot was unused: two artifact commits have Copilot footers.
The inspected Codex diagnostic-log database begins only on October 28 and
does not recover the earlier missing sessions or a historical bill.
The goal database retains two relevant latest-goal rows; rollouts preserve
26 goal-update events, including older goals no longer represented there.

### Files in the export

All CSVs have headers. Token and millisecond counts are integers, dates in
event files are UTC ISO timestamps, and `line` fields are one-based line
numbers in the rollout file identified by `sessions.csv`.

| File | Contents |
| --- | --- |
| `ai-assistance-data/summary.json` | Selection cutoff, aggregate counters by scope and thread kind, duration summaries, pinned Git revisions, and Git totals |
| `ai-assistance-data/sessions.csv` | One row per selected session: relative source filename, exact-file SHA-256, metadata/event dates, observed models, message/control/goal counts, tool counts, compactions, turn accounting, and final token counters |
| `ai-assistance-data/turns.csv` | Every retained completed-turn event, matched start when available, source line numbers, and client-reported duration |
| `ai-assistance-data/unmatched-starts.csv` | Start records with no matching completion, including interrupted work; their duration is unknown |
| `ai-assistance-data/user-records.csv` | Timestamp, source line, classification, and content hash for each user-role record; no message text. Includes agent/guardian inputs, which must be filtered by `kind` before interpreting counts |
| `ai-assistance-data/monthly.csv` | Usage grouped by the month of the session's **first event**; whole sessions are assigned to one month |
| `ai-assistance-data/goal-events.csv` | All retained goal updates, including repeated snapshots; these must not be summed as independent usage |
| `ai-assistance-data/episodes.csv` | Selected conversation/window counters and completed-turn duration sums, with exact baseline/final counter line numbers |
| `ai-assistance-data/commits.csv` | Non-merge commits reachable from each pinned revision, dates, subjects, recorded AI footers, and rename-aware line counts |
| `ai-assistance-data/api-pricing.json` | Dated Standard API rate snapshot, official source URLs, long-context rules, and explicit assumptions |
| `ai-assistance-data/api-cost-by-model.csv` | Token totals and hypothetical charges by scope, thread kind, and actual observed model; includes a comparison omitting the long-context premium |
| `ai-assistance-data/api-cost-by-session.csv` | Hypothetical charge for each conversation with an identified public model rate |
| `ai-assistance-data/api-cost-by-episode.csv` | Same repricing convention applied to the selected recovery windows |
| `ai-assistance-data/api-cost-summary.json` | Category totals and the explicit list of six unpriced automatic-review conversations |
| `ai-assistance-data/bucket-rules.json` | Reviewed purpose definitions, conversation-level exceptions, and source-line boundaries with reasons for mixed conversations |
| `ai-assistance-data/bucket-snapshot.json` | Exact immutable prefix of today's documentation conversation to include, identified by source filename, line limit, byte count, SHA-256, timestamp, and final token counters; no raw text |
| `ai-assistance-data/purpose-segments.csv` | Disjoint purpose segments, source-line bounds and rationale, token fields, completed-turn durations, message/tool counts, API-equivalent dollars, and explicitly unpriced review tokens |
| `ai-assistance-data/purpose-sessions.csv` | Reconciled conversation totals and the purposes represented in each conversation |
| `ai-assistance-data/purpose-totals.csv` | Three-way allocation for the original historical sample, today's added snapshot, and both together |
| `ai-assistance-data/purpose-summary.json` | The same aggregates, definitions, snapshot date, and allocation limitations |

The private rollouts are not included in the manuscript or source package.
The source-package script currently packages manuscript inputs and excerpts;
the audit data and script are reviewable in the repository, not dependencies
of LaTeX compilation.

### Accounting conventions and cautions

1. **Token totals.** Use the last `event_msg/token_count` record with an
   `info.total_token_usage` before the cutoff in each session. Cached input is
   a subset of input, and reasoning output is a subset of output. Reported
   total equals input plus output in all selected sessions. The script checks
   these invariants. Repeated `token_count` snapshots are not new requests;
   newer `token_usage_record` events are another representation and are not
   added a second time.
2. **Nonmonotone counters.** Four decreases occur in
   `019f0890-395a-76b0-aae9-5670f81a8f9a` and three in
   `019f59ec-6e13-78a3-9898-59b771ae41c8`. They occur within existing large
   cumulative totals and are not treated as resets. For the latter thread,
   the final reported total is 88,957,338. Treating each decrease as a reset
   would incorrectly inflate it to 279,238,014. The retained final history
   cannot establish provider charges for every discarded/retried branch.
3. **Time.** The 1,019 completed core user-facing turns report a summed
   `duration_ms` of 439,686,204 (122.135 hours). The union of matched
   start/completion **event-timestamp** intervals is 418,903.151 seconds
   (116.362 hours). Client-reported duration and timestamp differences are
   different measurements and need not agree. Union removes overlaps between
   recorded turns. Both measures include tools/waits inside a turn, omit
   unobserved work and thinking, and are not measures of researcher labor or
   pure inference time. Seventeen core user-facing starts are unmatched.
4. **Human input.** Count only `response_item/message` records of role `user`,
   without recursively counting messages repeated inside compaction summaries.
   Separate the explicitly marked automatic goal continuations and injected
   environment, AGENTS, plugin, open-page and turn-aborted control records.
   The remaining 780 records are candidates for human requests, **not** 780
   independent interventions. Retries and repeated submissions remain: the
   July 13 tail-bound request, for example, appears twice, 2.551 seconds
   apart. Guardian input contains copied transcripts and is never interpreted
   as fresh human messages. Classifications are deliberately syntactic and
   are not a full qualitative annotation of the conversations.
5. **Tools.** Count top-level `function_call`, `custom_tool_call`, and
   `web_search_call` response items. A JavaScript orchestration tool can invoke
   several nested tools; therefore 33,741 is not the count of shell commands,
   compiler invocations, or model requests.
6. **Goals.** `tokensUsed` and `timeUsedSeconds` are exported verbatim and have
   a narrower goal scope. The audit does not infer their charging formula,
   convert them into cumulative conversation tokens, or add them to those
   tokens. An `active` last snapshot may simply be incomplete; `paused` does
   not mean failure, nor does a commit titled "Finish" establish absence of
   later corrections. For example, the application also has the July 11
   soundness-fix commit `06fa6c5`.
7. **Git churn.** Use `git log --no-merges --reverse --numstat -M -z` separately
   in each repository, counting each reachable non-merge commit once. Artifact
   selected lines are `.v` files under `theories/`; manuscript selected lines
   are `.tex`. Full-file renames receive Git's rename detection, and NUL-separated
   paths are parsed to select by the destination filename rather than Git's
   brace-abbreviated display of a rename. Modified
   lines contribute both a deletion and an insertion, and moves within a
   file can still count as churn. Blank lines and comments count. Artifact
   submodule pointers are excluded from the Rocq counts; manuscript copies
   of Rocq excerpts are not counted again as artifact changes.
8. **Authorship.** Footer counts record assistance, including the two commits
   mentioning Copilot. They are neither a percentage of AI-written lines nor
   evidence that commits without footers were manual. All line-churn figures
   aggregate human and AI changes. Author/committer dates do not measure time
   spent on a commit. Month/phase claims here use recorded author dates.
9. **Cost.** No monetary charges or invoice were found in the inspected
   project records. The author subsequently confirmed that the work used
   monthly subscriptions with changing tiers and requested an API-price
   counterfactual. Subscription-limit fields and token counters are not
   invoices. The hypothetical dollar figures below use a dated public API
   price snapshot, the observed model and caching counters, and explicit
   processing assumptions. They do not reconstruct an actual-dollar total,
   isolate the cost of failed attempts, or test the $200 conjecture.

### Quantitative checks for the narrative

The core user-facing totals are 99,421,907 uncached input, 3,535,606,912 cached
input, and 8,682,819 output tokens (3,643,711,638 total). Recorded reasoning
output is 3,078,872, already included in output. All other categories are
separate in `summary.json`; they should not silently be folded into the core
table. The 126 core conversations include 92 recording `gpt-5.5`, 24
`gpt-5.6-sol`, two `gpt-5.6-luna`, one both latter identifiers, and seven
`gpt-6.1-sol`.

The pinned artifact has 231 commits, all non-merge, with 161 Codex and two
Copilot footers. Its Rocq history has 77,096 inserted and 49,866 deleted lines;
May--July accounts for 74,171 and 47,827 respectively. The pinned manuscript
has 134 reachable commits, of which 114 are non-merge; 77 of those have Codex
footers. Its `.tex` churn is 10,875 insertions and 7,497 deletions. These totals
include the early imported material, not just the intensive assisted phase.

### Provenance of the selected recovery episodes

Look up each full session ID in `sessions.csv` to find the private source
rollout and its hash. Line numbers below refer to that exact source; the
exported `user-records.csv` permits timestamp/hash checks without publishing
the messages. Qualitative statements are paraphrases of those records.

| Episode | Conversation and source lines | Dated evidence and outcome |
| --- | --- | --- |
| Heap-dependent/counter sequencing | `019e7e45-2c84-7be3-b63b-53b78a7be1b6`, lines 646, 671, 1131, 1209 | May 31, 14:57:21: author challenges a premise collapsing the randomized counter; 15:06:44: requests its removal; 17:29:29: explicitly reopens soundness; 17:35:40: says original informal argument fails but agrees to continue. The later `078fbd6` diff removes the heap-dependent budget interface. This is an example of questioning that did not immediately end the detour. |
| Hidden mixtures | `019e9fbc-8458-7c13-8389-403a7a23eba0`, lines 179, 197, 374 | June 7, 02:10:43: asks whether the measure respects mixture; 02:35:46: accepts prepending a zero entry; 02:53:11: questions dropping it even for identical randomized programs. `162cc37` repairs the rule. |
| Missing mass | `019ebce8-0a3b-7593-9573-7fd944a290ec`, line 1087 | June 12, 18:46:00: author points out that null output distributions make the claimed full-mass result false. The completion development continues in `019ebeb6-6c18-7300-b084-bcd7a98117a1` and the June 13 commits listed above. |
| Chart correction | `019f4224-099b-7d53-879f-23e05ef54fd2`, lines 26183, 26193, 26322 | July 9, 15:27:33.160: identifies contradiction with origin-centered charts; 15:29:24: requests documentation before further work; 15:44:42: proposes sample-then-common-postprocess sequencing. `e526e7f:status.md` records the flawed certificate and proposed repair. `da878fb` records completion of the application route at July 10, 04:48:51 UTC; later corrections still occurred. |
| Application pruning | `019f59ec-6e13-78a3-9898-59b771ae41c8`, lines 7, 1705, 2487 | July 13, 05:25:10, 06:53:22, and 07:49:28: author successively requests pruning the application, logic, and probability layers. Commits `4dced90`, `b62edcc`, and `88465c2` record the changes. |
| Retaining an unused result | Same July 13 session, lines 3136 and 3140 | At 08:26:45, the author asks to retain `discrete_gaussian_tail_bound` for future imperfect-correctness work. The repeated request appears at 08:26:47. `88465c2` retains the result and adds a future-use comment, illustrating why unused does not automatically mean wasted. |

`episodes.csv` defines windows using timestamps and takes the last cumulative
counter strictly before each boundary. For a full conversation, the baseline
is zero. For the chart-repair window the boundary counter lines are 26178 and
41131, and the increase is 341,717,678 total tokens. The pre-objection window
has 647,734,790 total tokens. No counter decrease occurs in these two windows.
Turn-duration attribution uses turns **ending** within the window; a turn
straddling a boundary is attributed in full to its ending window. Neither the
token snapshots nor this time convention resolve the precise instant an
individual model request or turn consumed resources. These are contextual
windows with reusable work, not labeled collections of entirely wasted calls.

The three July 13 cleanup commits, restricted to Rocq files, have the following
rename-aware `--numstat` counts. The submodule-pointer edits are excluded:

| Commit | Inserted | Deleted | Net reduction |
| --- | ---: | ---: | ---: |
| `4dced90` | 4 | 3,933 | 3,929 |
| `b62edcc` | 93 | 1,888 | 1,795 |
| `88465c2` | 23 | 1,634 | 1,611 |
| Total | 120 | 7,455 | 7,335 |

`078fbd6` separately reports 463 insertions and 1,160 deletions across four
Rocq files. Its title calls the change a reversion, but the diff is a design
replacement, not a byte-for-byte reversal of a single preceding commit.
`2b7499b` is another explicitly titled simplification of the trace construction
(13 inserted, 56 deleted lines). These support concrete rework examples; they
do not justify attributing all 49,866 deleted lines to failed AI output.

### Hypothetical API list-price equivalent

On November 4, after the usage audit, the author clarified that monthly
OpenAI subscriptions were used and tiers changed during development. At the
author's request, the appendix now reports an API list-price equivalent as an
illustrative overestimate of the subscription-based workflow's attributable
cost. This is not a universal claim that subscriptions are cheaper for every
utilization pattern, nor a strict upper bound on all project expenditure.
Actual project-specific subscription fees remain unreconstructed.

The rates below were checked by fetching the official model pages on
**November 4, 2026**. Rates are US dollars per million tokens, for Standard
processing and ordinary context length:

| Model and official source | Ordinary input | Cached input | Output |
| --- | ---: | ---: | ---: |
| [GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5) | 5.00 | 0.50 | 30.00 |
| [GPT-5.6 Sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol) | 4.00 | 0.40 | 20.00 |
| [GPT-5.6 Luna](https://developers.openai.com/api/docs/models/gpt-5.6-luna) | 0.20 | 0.02 | 1.20 |
| [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol) | 2.00 | 0.10 | 10.00 |

GPT-5.6 Sol's page describes its rate as promotional through at least
November 21, 2026; this audit freezes the currently listed rate and does not
attempt to recover every historical price. The rate snapshot is stored in
`api-pricing.json`, separately from the computation.

For a usage increment with total input `I`, cached input `H`, output `O`, and
the model's rates `r_in`, `r_cache`, `r_out`, the base charge is
`((I-H)*r_in + H*r_cache + O*r_out) / 1_000_000`.
Reasoning output is already included in `O`. The repricing script attributes
each signed cumulative-counter increment to the model in the associated
`turn_context`, handling the one conversation that switches between Luna and
Sol rather than assigning its entire usage to a single model. Repeated
snapshots contribute zero. Signed corrections reconcile exactly to every
priced session's final audited counters; they are not positive new usage.

There are **52 GPT-6.1 Sol usage updates with request input above 272,000
tokens**, all of which have increments matching `last_token_usage`. The
model's documented premium multiplies ordinary and cached input prices by
two and output by 1.5 for those requests. This adds **$2.7602644** to the main
conversations' base-rate equivalent of $2,441.7643702. All GPT-5.5, GPT-5.6
Sol, and GPT-5.6 Luna requests are below the threshold (observed maxima
250,694, 237,892, and 91,741 input tokens, respectively). Thus GPT-5.5's
session-wide long-context rule is not activated. The GPT-6.1 Sol maximum is
381,384 input tokens. The script retains the distinction between session-wide
and per-request premiums for the supported models and rejects ambiguous
counter attribution for a surcharged request. The seven counter decreases
are confined to short-context GPT-5.5 sessions, so their exact timing does not
change the multiplier applied to them.

| Core user-facing model | Ordinary input tokens | Cached input tokens | Output tokens | API-equivalent USD |
| --- | ---: | ---: | ---: | ---: |
| `gpt-5.5` | 87,999,099 | 3,211,685,760 | 7,544,829 | 2,272.18 |
| `gpt-5.6-sol` | 9,227,415 | 256,076,544 | 834,215 | 156.02 |
| `gpt-5.6-luna` | 197,514 | 2,031,360 | 15,729 | 0.10 |
| `gpt-6.1-sol` | 1,997,879 | 65,813,248 | 288,046 | 16.22 |
| Total | 99,421,907 | 3,535,606,912 | 8,682,819 | **2,444.52** |

The three subagent conversations add **$1.6661376**, giving **$2,446.19** for
the core user-facing and delegated work together. The five upstream-support
conversations add **$28.65562**, giving **$2,474.85** across all 134 priced
conversations. No surrogate rate is assigned to `codex-auto-review`: the
remaining six conversations and their 911,508 total tokens are explicitly
listed as unpriced. The CSV and JSON dollar fields retain six decimal places;
the manuscript rounds to cents or whole dollars. Individual rounded lines
should not be used in place of the unrounded aggregate.

The same convention gives the following equivalents for contextual episodes:

| Episode | API-equivalent USD |
| --- | ---: |
| May 31 heap-dependent sequencing conversation | 53.63 |
| June 7 hidden-mixture discussion | 4.72 |
| June 12 missing-mass review | 22.34 |
| June 13 completion development | 27.24 |
| Application session before the July 9 chart objection | 424.70 |
| Chart objection to July 10 completion commit | 226.68 |
| July 13 pruning conversation | 58.97 |

These are not additional charges to add to the conversation totals. They
include useful work and human interaction around the selected detours and
repairs, and do not measure dollars wasted. The episode boundaries are the
same as in `episodes.csv`; no episode has a long-context premium or model
switch.

The estimate assumes API requests attain the cache-read counts observed in
the subscription logs. All priced source counters report zero cache-write
tokens, so no separate write charge is added; the script checks this rather
than silently accepting new nonzero write usage. Zero local write counters
do not prove that an API replay would incur no writes or achieve identical
caching. The official [prompt-caching guide](https://developers.openai.com/api/docs/guides/prompt-caching)
describes separate write accounting for applicable models. Hosted-tool fees,
local compute, taxes, alternative processing tiers, unavailable usage, and
unpriced action review are excluded. The result is a token-price comparison,
not an exact API-replay invoice or an estimate of the cost to recreate the
final formalization with today's knowledge of its finished design.

### Approximate three-way allocation by purpose

At the author's request the appendix further distinguishes work toward the
formalization, paper writing broadly construed, and other work such as the
MathComp Analysis contribution. This allocation is based on task purpose,
not the directory in which a session happened to start or the number of
lines changed in each repository.

The original 140 historical conversations are retained without changing their
usage or price totals. For this table only, one additional conversation is
included: `01a1a79c-6f7c-76b1-8d50-1162ba070f87`, the current documentation
conversation, through **2026-11-04 18:04:08.685 UTC** (13:04:08.685 in the
author's America/New_York timezone). This snapshot includes all usage up to
source line 330, with 7,547,175 total tokens and a hypothetical API equivalent
of $1.809348. It is assigned entirely to paper writing. Two completed turns
report 1,212,082 milliseconds (0.336689 hours); the then-ongoing turn has no
completion-duration record and is excluded from time totals. Later work in
the current conversation is excluded, even when it continues this audit.

`bucket-snapshot.json` identifies the source prefix using its one-based line
limit, 3,009,429-byte length, SHA-256, and final counters. The script verifies
that prefix rather than hashing the entire ever-growing live rollout. The
raw conversation is not copied into the manuscript repository. All historical
source hashes continue to be checked against the frozen audit inventory.

The buckets are defined as follows:

- **Repository/formalization:** definitions, proof design, Rocq proof scripts,
  supporting probability results, unsuccessful experiments, refactoring,
  upgrades of dependencies, build validation, and instructions or packaging
  for the artifact. This is work in support of the formalization, not a claim
  that every resulting lemma survives on the final theorem's dependency path.
  Informal mathematical sketches written to guide verification remain here.
- **Paper:** exposition, literature and comparison research, manuscript review,
  reviewer responses, figures, displayed code excerpts, LaTeX builds, and the
  AI-assistance disclosure and measurements, including today's conversation.
- **Other:** preparing and reviewing upstream MathComp Analysis contributions,
  their service-related planning and cleanup, and one accidental archived
  greeting. Other unrelated projects and presentation slides remain outside
  the selected corpus, rather than being silently added to this bucket.

The important conversation-level exceptions to a simple directory split are
June 27's `019f0890-395a-76b0-aae9-5670f81a8f9a` (community-service proofs and
contribution planning) and June 30's
`019f1806-f9ab-7cf0-97fa-0cdc65c1a34b` (cleanup of that service scaffolding).
Both started in the artifact directory but belong to Other. Together with the
five formerly labeled upstream conversations and the accidental archived
greeting, they account for $45.335758. Thus the new Other bucket is broader
than the earlier $28.65562 category, which contained only those five upstream
conversations.

Six mixed historical conversations are split at manually reviewed requests:

| Conversation | Basis of the split |
| --- | --- |
| `019f4224-099b-7d53-879f-23e05ef54fd2` | The large July 8--11 conversation begins with proving security. At source line 41136, July 10 04:51:50 UTC, the author explicitly switches to updating the paper. Later requests alternate between exposition, formal refactoring, build modernization, and the adversary-dependent bound repair. All 17 reviewed purpose changes are recorded in the rules file. |
| `019f6f0a-7010-7340-b794-15bd2b310862` | Coupling-interface refactoring becomes checking and expanding displayed manuscript excerpts at line 549. |
| `019f783e-30cb-7413-b1fe-1bd87c9182a7` | An initial question about the displayed Gaussian rule changes to formalizing its specialization at line 72. |
| `019fb104-2647-75b0-94fe-2b6c6084f19c` | Build/reproduction validation becomes paper wording about benchmark time at line 1282, then artifact README anonymization at line 1330. |
| `01a13603-65cb-7b61-aed7-74c8fd275762` | Reviewer-driven formal interface changes and dependency inspection become response/exposition work at line 216, then return to removing unused lemmas and rebuilding at line 286. |
| `01a18449-12a9-7cd0-85af-ed097665fbd9` | The dependency migration becomes expanding the manuscript account of upstream contributions at line 1007. |

Purely editorial and LaTeX sessions are labeled Paper; formalization sessions
retain the Repository default. `bucket-rules.json` explicitly lists the Paper
and Other exceptions, together with every mixed-session boundary and reason.
The three August subagent threads work on manuscript figure layout and are
Paper. The six automatic-review threads inherit the initial purpose of their
parent conversations; their 723,607 Repository and 187,901 Paper tokens remain
unpriced. They are included in token and completed-turn duration totals, not
assigned an invented API rate.

| Purpose, including today's fixed snapshot | Uncached input | Cached input | Output | Total tokens | Reported agent hours | API-equivalent USD |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Repository/formalization | 83,111,876 | 3,257,091,456 | 7,484,596 | 3,347,687,928 | 110.755812 | 2,231.82 |
| Paper | 15,940,666 | 268,130,816 | 1,218,477 | 285,289,959 | 11.012949 | 199.50 |
| Other | 3,032,398 | 50,343,552 | 260,729 | 53,636,679 | 2.636028 | 45.34 |
| Total | 102,084,940 | 3,575,565,824 | 8,963,802 | 3,686,614,566 | 124.404789 | **2,476.66** |

For comparison, restricting the allocation to the original historical sample
gives Repository $2,231.821377, Paper $197.689257, and Other $45.335758,
which reconcile to the earlier $2,474.846392 API-equivalent total. Today's
additional $1.809348 goes solely to Paper. Token totals include the unpriced
action review; the dollar total excludes it, consistently with the prior
pricing audit. Numbers of sessions represented in each bucket overlap for
mixed sessions and must not be summed as unique conversation counts.

Each signed usage increment belongs to exactly one reviewed source-line
segment; a repeated cumulative snapshot contributes no new usage. The entire
request's context cost follows the current task, including cached earlier
proof context reused during a writing task. This is a cost allocation, not a
semantic attribution of the content of every input token. Completed-turn
duration is assigned at its completion record, just as for the episode windows;
a turn straddling a boundary therefore goes to its ending segment. A task
combining code and manuscript edits is assigned its dominant purpose rather
than split by lines of output. These conventions make the partition complete
and reproducible, while the labels and boundary choices remain approximate.

The bucket script checks token totals and message/tool/turn counts for every
historical conversation against the frozen audit, checks each priced
historical conversation against the earlier dollar equivalent, and checks the
additional snapshot's final counters and source hash. The three buckets sum
to the full extended sample without double counting, despite six conversations
contributing to both Repository and Paper.

### Validation performed

- Regenerated all exports from the pinned repositories and retained rollouts;
  checked per-session token subset and total invariants.
- Reconciled all 140 exported final totals with the independent session-state
  database; checked the two remaining goal rows against the corresponding
  retained goal events.
- Checked the cited human requests, `status.md` recovery plan, and cleanup
  diffs directly, including the restoration/preservation of the tail theorem.
- Built both manuscript formats with LaTeX, keeping validation output in
  temporary directories so the existing generated artifacts are untouched.
- Repriced 134 conversations using exact decimal arithmetic, checked source
  hashes and per-session reconciliation to the frozen token inventory, and
  confirmed that the 52 surcharged updates match per-request usage fields.
- Partitioned all 140 historical conversations plus today's fixed prefix by
  reviewed purpose, checked all historical totals against the preceding
  exports, and verified that the extended three-bucket totals reconcile.
