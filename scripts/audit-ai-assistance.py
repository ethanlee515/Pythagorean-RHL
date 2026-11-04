#!/usr/bin/env python3
"""Export project-specific historical measurements without exporting chat contents.

Uses only the Python standard library, local Codex rollouts, and read-only Git
commands. See ../AI-ASSISTANCE-NOTES.md for interpretation and limitations.
"""

import argparse
import collections
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess


# These conversations started outside the artifact's working directory. The
# explicit allowlist avoids attributing other projects in ~/research to this one.
EXTRA_CORE = {
    "019f8cc3-ed82-7a63-bc09-dd8a951d35be",  # Rework manuscript for CSF.
    "019f9d79-ce2a-77c3-91ec-b14b43663950",  # SSProve syntax/semantics appendix.
}
UPSTREAM = {
    "019f08b2-5513-72b0-a1bf-333aba0a3a89",  # Build MathComp Analysis.
    "019f0d88-9bad-7a11-a47b-83f787281f86",  # Stage reusable lemmas.
    "019f0dba-e231-7613-bb0d-e5c17c5310ba",  # Review staged proofs.
    "019f0e0d-a421-73f2-bc79-a0e2facd08ea",  # Graft lemmas upstream.
    "019f9234-aa03-74d0-bc5b-52c6936002f1",  # Upstream reviewer feedback.
}
TOKEN_KEYS = (
    "input_tokens", "cached_input_tokens", "output_tokens",
    "reasoning_output_tokens", "total_tokens",
)
EPISODES = (
    ("heap-dependent-sequencing", "019e7e45-2c84-7be3-b63b-53b78a7be1b6", "", ""),
    ("hidden-mixture-review", "019e9fbc-8458-7c13-8389-403a7a23eba0", "", ""),
    ("missing-mass-review", "019ebce8-0a3b-7593-9573-7fd944a290ec", "", ""),
    ("completion-repair", "019ebeb6-6c18-7300-b084-bcd7a98117a1", "", ""),
    ("application-before-chart-objection", "019f4224-099b-7d53-879f-23e05ef54fd2",
     "", "2026-07-09T15:27:33.160Z"),
    ("chart-repair-to-finish-commit", "019f4224-099b-7d53-879f-23e05ef54fd2",
     "2026-07-09T15:27:33.160Z", "2026-07-10T04:48:51Z"),
    ("july-13-pruning", "019f59ec-6e13-78a3-9898-59b771ae41c8", "", ""),
)


def instant(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def request_kind(body):
    body = body.strip()
    if body.startswith('<codex_internal_context source="goal">'):
        return "automatic_goal"
    if body.startswith(("<environment_context>", "<recommended_plugins>",
                        "# AGENTS.md", "<external_codex_apps_open_page>",
                        "<turn_aborted>")):
        return "context_or_control"
    return "request_record"


def merge_seconds(intervals):
    merged = []
    for start, end in sorted(intervals):
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(end, merged[-1][1])
    return sum((b - a).total_seconds() for a, b in merged)


def write_csv(path, rows):
    if not rows:
        return
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True)


def git_records(repo, ref, label):
    # Normal Git rename detection: file moves do not count as wholesale deletion.
    log = git(repo, "log", "--no-merges", "--reverse", "--numstat", "-M", "-z",
              "--format=%x1e%H%x1f%aI%x1f%cI%x1f%s%x1f%B%x1d", ref)
    rows = []
    for record in log.split("\x1e")[1:]:
        header, nums = record.split("\x1d", 1)
        sha, author_date, commit_date, subject, body = header.split("\x1f", 4)
        added = deleted = selected_added = selected_deleted = 0
        entries = iter(nums.split("\0"))
        for entry in entries:
            line = entry.lstrip("\n")
            parts = line.split("\t", 2)
            if len(parts) != 3 or not parts[0].isdigit():
                continue
            a, d, path = int(parts[0]), int(parts[1]), parts[2]
            if not path:
                # With -z, renames use: a\td\t\0old-path\0new-path\0.
                # Select by the actual destination, not Git's display braces.
                next(entries)
                path = next(entries)
            added += a
            deleted += d
            selected = (path.startswith("theories/") and path.endswith(".v")) \
                if label == "artifact" else path.endswith(".tex")
            if selected:
                selected_added += a
                selected_deleted += d
        rows.append(dict(repository=label, commit=sha, author_date=author_date,
                         committer_date=commit_date, subject=subject,
                         codex_footer=int("co-authored-by: codex" in body.lower()),
                         copilot_footer=int("co-authored-by: copilot" in body.lower()),
                         all_added=added, all_deleted=deleted,
                         selected_added=selected_added, selected_deleted=selected_deleted))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    parser.add_argument("--before", default="2026-11-04T00:00:00Z")
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "ai-assistance-data")
    parser.add_argument("--artifact-ref", default="4b8625d")
    parser.add_argument("--manuscript-ref", default="e6035b2")
    args = parser.parse_args()
    cutoff = instant(args.before)
    sessions, turns, goals, requests, unmatched, counters = [], [], [], [], [], {}
    intervals = collections.defaultdict(list)
    scanned = 0
    paths = sorted([*(args.codex_home / "sessions").rglob("*.jsonl"),
                    *(args.codex_home / "archived_sessions").rglob("*.jsonl")])
    seen = set()
    for path in paths:
        with path.open() as stream:
            first = json.loads(next(stream))
            if first["type"] != "session_meta":
                raise ValueError(f"Missing session metadata: {path}")
            meta = first["payload"]
            scanned += 1
            sid = meta["id"]
            cwd = meta.get("cwd", "").lower().rstrip("/")
            in_workspace = cwd in ("/home/ethan/research/mending",
                                   "/home/ethan/research/mending/pythagorean-rhl")
            scope = "core" if in_workspace or sid in EXTRA_CORE else "upstream"
            if not (in_workspace or sid in EXTRA_CORE or sid in UPSTREAM):
                continue
            if instant(meta["timestamp"]) >= cutoff:
                continue
            if sid in seen:
                raise ValueError(f"Duplicate session ID: {sid}")
            seen.add(sid)
            source = meta.get("source", "")
            kind = "user" if isinstance(source, str) else "subagent"
            if "guardian" in json.dumps(source):
                kind = "guardian"
            row = dict(session_id=sid, scope=scope, kind=kind,
                       rollout=str(path.relative_to(args.codex_home)),
                       sha256="", metadata_start_utc=meta["timestamp"],
                       first_event_utc="", last_event_utc="", models="",
                       request_records=0, automatic_goal_records=0,
                       context_or_control_records=0, compactions=0,
                       tool_calls=0, completed_turns=0, unmatched_starts=0,
                       reported_duration_ms=0, counter_decreases=0,
                       repeated_counters=0, **{key: 0 for key in TOKEN_KEYS})
            models, starts, counts = set(), {}, []
            previous_total = None
            for line_number, line in enumerate(stream, 2):
                event = json.loads(line)
                timestamp = event["timestamp"]
                if instant(timestamp) >= cutoff:
                    continue
                payload = event.get("payload", {})
                etype, ptype = event["type"], payload.get("type")
                row["first_event_utc"] = row["first_event_utc"] or timestamp
                row["last_event_utc"] = timestamp
                if etype == "turn_context" and payload.get("model"):
                    models.add(payload["model"])
                if etype == "compacted":
                    row["compactions"] += 1
                if etype == "response_item":
                    if ptype in ("function_call", "custom_tool_call", "web_search_call"):
                        row["tool_calls"] += 1
                    if ptype == "message" and payload.get("role") == "user":
                        body = "\n".join(c.get("text", "") for c in payload.get("content", []))
                        category = request_kind(body)
                        key = {"automatic_goal": "automatic_goal_records",
                               "request_record": "request_records",
                               "context_or_control": "context_or_control_records"}[category]
                        row[key] += 1
                        requests.append(dict(session_id=sid, scope=scope, kind=kind,
                                             line=line_number, timestamp_utc=timestamp,
                                             category=category,
                                             content_sha256=hashlib.sha256(body.encode()).hexdigest()))
                if etype != "event_msg":
                    continue
                if ptype == "task_started":
                    starts[payload.get("turn_id")] = (timestamp, line_number)
                if ptype == "task_complete":
                    turn_id = payload.get("turn_id")
                    start, start_line = starts.pop(turn_id, ("", ""))
                    duration = payload.get("duration_ms") or 0
                    turns.append(dict(session_id=sid, scope=scope, kind=kind,
                                      turn_id=turn_id, start_utc=start, end_utc=timestamp,
                                      start_line=start_line, end_line=line_number,
                                      reported_duration_ms=duration))
                    row["completed_turns"] += 1
                    row["reported_duration_ms"] += duration
                    if start:
                        intervals[scope, kind].append((instant(start), instant(timestamp)))
                if ptype == "thread_goal_updated":
                    goal = payload["goal"]
                    goals.append(dict(session_id=sid, line=line_number, timestamp_utc=timestamp,
                                      created_at=goal.get("createdAt"),
                                      status=goal.get("status"),
                                      goal_tokens_used=goal.get("tokensUsed", 0),
                                      goal_time_used_seconds=goal.get("timeUsedSeconds", 0)))
                if ptype == "token_count" and payload.get("info"):
                    usage = payload["info"]["total_token_usage"]
                    total = usage["total_tokens"]
                    if previous_total is not None:
                        row["counter_decreases"] += int(total < previous_total)
                        row["repeated_counters"] += int(total == previous_total)
                    previous_total = total
                    counts.append((timestamp, line_number, usage))
                    # The last cumulative snapshot is authoritative for this export.
                    # In particular, a decrease is NOT treated as a counter reset.
                    for key in TOKEN_KEYS:
                        row[key] = usage.get(key, 0)
            row["models"] = ";".join(sorted(models))
            row["unmatched_starts"] = len(starts)
            for turn_id, (start, start_line) in starts.items():
                unmatched.append(dict(session_id=sid, scope=scope, kind=kind,
                                      turn_id=turn_id, start_utc=start, start_line=start_line))
            assert row["total_tokens"] == row["input_tokens"] + row["output_tokens"], sid
            assert 0 <= row["cached_input_tokens"] <= row["input_tokens"], sid
            assert 0 <= row["reasoning_output_tokens"] <= row["output_tokens"], sid
            with path.open("rb") as raw:
                row["sha256"] = hashlib.file_digest(raw, "sha256").hexdigest()
            sessions.append(row)
            counters[sid] = counts

    sessions.sort(key=lambda r: r["first_event_utc"])
    aggregates = []
    for scope, kind in sorted({(r["scope"], r["kind"]) for r in sessions}):
        selected = [r for r in sessions if (r["scope"], r["kind"]) == (scope, kind)]
        sums = {k: sum(r[k] for r in selected) for k in (
            *TOKEN_KEYS, "request_records", "automatic_goal_records",
            "context_or_control_records", "compactions", "tool_calls",
            "completed_turns", "unmatched_starts", "reported_duration_ms",
            "counter_decreases", "repeated_counters")}
        aggregates.append(dict(scope=scope, kind=kind, sessions=len(selected), **sums,
                               uncached_input_tokens=sums["input_tokens"] - sums["cached_input_tokens"],
                               paired_turn_union_seconds=merge_seconds(intervals[scope, kind])))

    monthly = []
    for scope, kind, month in sorted({(r["scope"], r["kind"], r["first_event_utc"][:7])
                                      for r in sessions}):
        selected = [r for r in sessions if (r["scope"], r["kind"], r["first_event_utc"][:7])
                    == (scope, kind, month)]
        monthly.append(dict(scope=scope, kind=kind, session_first_event_month_utc=month,
                            sessions=len(selected), **{k: sum(r[k] for r in selected)
                                                      for k in TOKEN_KEYS}))

    episodes = []
    for name, sid, start, end in EPISODES:
        counts = counters[sid]
        end_dt = instant(end) if end else cutoff
        start_dt = instant(start) if start else dt.datetime.min.replace(tzinfo=dt.timezone.utc)
        before = [x for x in counts if instant(x[0]) < start_dt]
        through = [x for x in counts if instant(x[0]) < end_dt]
        base = before[-1][2] if before else {}
        last = through[-1][2] if through else {}
        matching = [r for r in turns if r["session_id"] == sid
                    and start_dt <= instant(r["end_utc"]) < end_dt]
        episodes.append(dict(episode=name, session_id=sid, start_inclusive_utc=start,
                             end_exclusive_utc=end, baseline_counter_line=before[-1][1] if before else 0,
                             final_counter_line=through[-1][1] if through else 0,
                             completed_turns=len(matching),
                             reported_duration_ms=sum(r["reported_duration_ms"] for r in matching),
                             **{k: last.get(k, 0) - base.get(k, 0) for k in TOKEN_KEYS}))

    manuscript = Path(__file__).resolve().parents[1]
    commits = git_records(manuscript.parent, args.artifact_ref, "artifact") \
        + git_records(manuscript, args.manuscript_ref, "manuscript")
    git_summary = []
    for label, repo, ref in (("artifact", manuscript.parent, args.artifact_ref),
                              ("manuscript", manuscript, args.manuscript_ref)):
        selected = [r for r in commits if r["repository"] == label]
        git_summary.append(dict(repository=label, head=git(repo, "rev-parse", ref).strip(),
                                reachable_commits=int(git(repo, "rev-list", "--count", ref)),
                                nonmerge_commits=len(selected),
                                **{k: sum(r[k] for r in selected) for k in (
                                    "codex_footer", "copilot_footer", "all_added", "all_deleted",
                                    "selected_added", "selected_deleted")}))

    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    for filename, rows in (("sessions.csv", sessions), ("turns.csv", turns),
                           ("goal-events.csv", goals), ("monthly.csv", monthly),
                           ("episodes.csv", episodes), ("commits.csv", commits),
                           ("user-records.csv", requests), ("unmatched-starts.csv", unmatched)):
        write_csv(output / filename, rows)
    summary = dict(before_exclusive_utc=args.before, scanned_rollout_files=scanned,
                   selected_rollout_files=len(sessions), aggregates=aggregates,
                   git=git_summary)
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
