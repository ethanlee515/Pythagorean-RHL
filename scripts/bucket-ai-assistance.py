#!/usr/bin/env python3
"""Apply reviewable purpose labels to the frozen usage audit and today's snapshot.

Mixed sessions are divided at explicitly reviewed source-line boundaries. Every
record belongs to one segment. Costs use the same frozen rates as the repricing
script; original historical exports are never changed.
"""

import argparse
import bisect
import collections
import csv
from decimal import Decimal
import hashlib
import json
from pathlib import Path


TOKEN_KEYS = ("input_tokens", "cached_input_tokens", "output_tokens",
              "reasoning_output_tokens", "total_tokens")
COUNT_KEYS = ("counter_updates", "counter_decreases", "completed_turns",
              "reported_duration_ms", "request_records", "automatic_goal_records",
              "context_or_control_records", "tool_calls", "compactions")
ZERO = Decimal(0)


def request_kind(body):
    body = body.strip()
    if body.startswith('<codex_internal_context source="goal">'):
        return "automatic_goal_records"
    if body.startswith(("<environment_context>", "<recommended_plugins>",
                        "# AGENTS.md", "<external_codex_apps_open_page>", "<turn_aborted>")):
        return "context_or_control_records"
    return "request_records"


def money(value):
    return str(value.quantize(Decimal("0.000001")))


def write_csv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    parser.add_argument("--data", type=Path,
                        default=Path(__file__).resolve().parents[1] / "ai-assistance-data")
    args = parser.parse_args()
    data = args.data
    rules = json.loads((data / "bucket-rules.json").read_text())
    snapshot = json.loads((data / "bucket-snapshot.json").read_text())
    pricing = json.loads((data / "api-pricing.json").read_text())
    baseline = list(csv.DictReader((data / "sessions.csv").open()))
    sessions = baseline + snapshot["additional_sessions"]
    ids = {s["session_id"] for s in sessions}
    assert len(ids) == len(sessions)
    assert set(rules["paper_sessions"]) <= ids
    assert set(rules["other_sessions"]) <= ids
    assert set(rules["phase_changes"]) <= ids
    session_map = {s["session_id"]: s for s in sessions}
    previous_prices = {s["session_id"]: Decimal(s["usd"]) for s in
                       csv.DictReader((data / "api-cost-by-session.csv").open())}

    def default_label(session):
        sid = session["session_id"]
        if sid in rules["paper_sessions"]:
            return "paper", "Manuscript, exposition, review, LaTeX/excerpts, or AI-assistance documentation."
        if sid in rules["other_sessions"]:
            return "other", rules["other_sessions"][sid]
        label = rules["default_by_scope"][session["scope"]]
        return label, rules["definitions"][label]

    def price(usage, model, long_context):
        rates = pricing["models"][model]
        a = Decimal(pricing["long_context_input_multiplier"]) if long_context else Decimal(1)
        b = Decimal(pricing["long_context_output_multiplier"]) if long_context else Decimal(1)
        return (a * ((usage["input_tokens"] - usage["cached_input_tokens"]) * Decimal(rates["input"])
                     + usage["cached_input_tokens"] * Decimal(rates["cached_input"]))
                + b * usage["output_tokens"] * Decimal(rates["output"])) / Decimal(1000000)

    segments, session_rows = [], []
    for session in sessions:
        sid = session["session_id"]
        period = "historical" if sid in {s["session_id"] for s in baseline} else "audit_today"
        path = args.codex_home / session["rollout"]
        label, reason = default_label(session)
        with path.open("rb") as stream:
            meta = json.loads(stream.readline())["payload"]
        assert meta["id"] == sid
        if session["kind"] == "guardian":
            parent = meta.get("parent_thread_id")
            assert parent in session_map, sid
            label, _ = default_label(session_map[parent])
            reason = "Automatic action review inherits the parent conversation's initial purpose; retained tokens are unpriced."
        changes = {1: dict(from_line=1, bucket=label, reason=reason)}
        changes.update({c["from_line"]: c for c in rules["phase_changes"].get(sid, [])})
        boundaries = sorted(changes)
        rows = []
        for start in boundaries:
            change = changes[start]
            rows.append(dict(session_id=sid, period=period, scope=session["scope"], kind=session["kind"],
                             bucket=change["bucket"], from_line_inclusive=start, to_line_exclusive=0,
                             reason=change["reason"],
                             **{k: 0 for k in (*TOKEN_KEYS, *COUNT_KEYS)},
                             unpriced_tokens=0, usd=ZERO))
        digest = hashlib.sha256()
        previous, model, line_count, first_event, last_event = {}, None, 0, "", ""
        limit = int(session.get("through_line", 0))
        with path.open("rb") as stream:
            for line_number, raw in enumerate(stream, 1):
                if limit and line_number > limit:
                    break
                digest.update(raw)
                line_count = line_number
                event = json.loads(raw)
                payload = event.get("payload", {})
                if line_number == 1:
                    continue
                first_event = first_event or event["timestamp"]
                last_event = event["timestamp"]
                row = rows[bisect.bisect_right(boundaries, line_number) - 1]
                etype, ptype = event["type"], payload.get("type")
                if etype == "turn_context":
                    model = payload.get("model", model)
                if etype == "compacted":
                    row["compactions"] += 1
                if etype == "response_item":
                    if ptype in ("function_call", "custom_tool_call", "web_search_call"):
                        row["tool_calls"] += 1
                    if ptype == "message" and payload.get("role") == "user":
                        body = "\n".join(x.get("text", "") for x in payload.get("content", []))
                        row[request_kind(body)] += 1
                if etype != "event_msg":
                    continue
                if ptype == "task_complete":
                    row["completed_turns"] += 1
                    row["reported_duration_ms"] += payload.get("duration_ms") or 0
                if ptype != "token_count" or not payload.get("info"):
                    continue
                info = payload["info"]
                current = info["total_token_usage"]
                delta = {k: current.get(k, 0) - previous.get(k, 0) for k in TOKEN_KEYS}
                previous = current
                if not any(delta.values()):
                    continue
                assert current.get("cache_write_input_tokens", 0) == 0, sid
                for key in TOKEN_KEYS:
                    row[key] += delta[key]
                row["counter_updates"] += 1
                row["counter_decreases"] += int(delta["total_tokens"] < 0)
                if model in pricing["unpriced_models"]:
                    row["unpriced_tokens"] += delta["total_tokens"]
                    continue
                assert model in pricing["models"], (sid, model)
                last = info["last_token_usage"]
                is_long = last["input_tokens"] > pricing["long_context_threshold_input_tokens"]
                if model == "gpt-5.5":
                    assert not is_long, "This fixed sample must not activate session-wide repricing"
                if is_long:
                    assert delta["total_tokens"] == last["total_tokens"], (sid, line_number)
                row["usd"] += price(delta, model, is_long)
        assert digest.hexdigest() == session["sha256"], (sid, "source hash")
        assert not limit or line_count == limit
        assert boundaries[-1] <= line_count, (sid, "classification boundary")
        for i, row in enumerate(rows):
            row["to_line_exclusive"] = boundaries[i + 1] if i + 1 < len(rows) else line_count + 1
        totals = {key: sum(r[key] for r in rows) for key in (*TOKEN_KEYS, *COUNT_KEYS)}
        for key in TOKEN_KEYS:
            assert totals[key] == previous.get(key, 0) == int(session[key]), (sid, key)
        if period == "historical":
            for key in ("completed_turns", "reported_duration_ms", "request_records", "automatic_goal_records",
                        "context_or_control_records", "tool_calls", "compactions"):
                assert totals[key] == int(session[key]), (sid, key)
        cost = sum((r["usd"] for r in rows), ZERO)
        if sid in previous_prices:
            assert abs(cost - previous_prices[sid]) <= Decimal("0.000001"), sid
        segments.extend(rows)
        session_rows.append(dict(session_id=sid, period=period, scope=session["scope"], kind=session["kind"],
                                 buckets=";".join(sorted({r["bucket"] for r in rows})),
                                 segments=len(rows), first_event_utc=first_event, last_event_utc=last_event,
                                 **totals, unpriced_tokens=sum(r["unpriced_tokens"] for r in rows), usd=cost))

    aggregates = []
    for period in ("historical", "audit_today", "all"):
        for bucket in rules["definitions"]:
            selected = [r for r in segments if r["bucket"] == bucket
                        and (period == "all" or r["period"] == period)]
            totals = {k: sum(r[k] for r in selected) for k in (*TOKEN_KEYS, *COUNT_KEYS, "unpriced_tokens")}
            aggregates.append(dict(period=period, bucket=bucket,
                                   sessions_represented=len({r["session_id"] for r in selected}), **totals,
                                   uncached_input_tokens=totals["input_tokens"] - totals["cached_input_tokens"],
                                   reported_hours=str((Decimal(totals["reported_duration_ms"]) / Decimal(3600000)).quantize(Decimal("0.000001"))),
                                   usd=money(sum((r["usd"] for r in selected), ZERO))))
    for collection in (segments, session_rows):
        for row in collection:
            row["usd"] = money(row["usd"])
    write_csv(data / "purpose-segments.csv", segments)
    write_csv(data / "purpose-sessions.csv", session_rows)
    write_csv(data / "purpose-totals.csv", aggregates)
    result = dict(snapshot_through_utc=snapshot["snapshot_through_utc"],
                  historical_session_count=len(baseline), additional_session_count=len(snapshot["additional_sessions"]),
                  purpose_definitions=rules["definitions"], aggregates=aggregates,
                  limitations=["Approximate task-purpose labels, not file-level effort attribution.",
                               "Usage increments follow the reviewed source-line boundaries, including repeated earlier context.",
                               "Completed-turn duration is assigned by completion event; no human-labor inference.",
                               "Mixed tasks take their dominant purpose; working proof sketches remain repository work.",
                               "Today's ongoing discussion is included only through the frozen prefix; later usage is excluded.",
                               "Automatic review inherits its parent purpose and remains explicitly unpriced."])
    (data / "purpose-summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
