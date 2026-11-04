#!/usr/bin/env python3
"""Reprice the audited usage at a dated snapshot of Standard API token rates.

Reads the frozen session inventory and private rollouts, without changing the
usage audit. Outputs contain counters and computed costs, never chat contents.
"""

import argparse
import collections
import csv
from datetime import datetime
from decimal import Decimal
import hashlib
import json
from pathlib import Path


KEYS = ("input_tokens", "cached_input_tokens", "output_tokens", "total_tokens")
ZERO = Decimal(0)
MILLION = Decimal(1000000)


def timestamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


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
    pricing = json.loads((args.data / "api-pricing.json").read_text())
    cutoff = timestamp(json.loads((args.data / "summary.json").read_text())["before_exclusive_utc"])
    sessions = list(csv.DictReader((args.data / "sessions.csv").open()))
    grouped = collections.defaultdict(collections.Counter)
    costs = collections.defaultdict(lambda: ZERO)
    flat_costs = collections.defaultdict(lambda: ZERO)
    session_rows, unpriced, surcharged_sessions = [], [], set()

    def cost(usage, model, long_context=False):
        rates = pricing["models"][model]
        input_multiplier = Decimal(pricing["long_context_input_multiplier"]) if long_context else Decimal(1)
        output_multiplier = Decimal(pricing["long_context_output_multiplier"]) if long_context else Decimal(1)
        uncached = usage["input_tokens"] - usage["cached_input_tokens"]
        return ((uncached * Decimal(rates["input"])
                 + usage["cached_input_tokens"] * Decimal(rates["cached_input"])) * input_multiplier
                + usage["output_tokens"] * Decimal(rates["output"]) * output_multiplier) / MILLION

    for session in sessions:
        models = set(session["models"].split(";"))
        unknown = models - pricing["models"].keys()
        if unknown:
            assert unknown <= set(pricing["unpriced_models"]), unknown
            unpriced.append(dict(session_id=session["session_id"], scope=session["scope"],
                                 kind=session["kind"], models=session["models"],
                                 total_tokens=int(session["total_tokens"])))
            continue
        path = args.codex_home / session["rollout"]
        with path.open("rb") as stream:
            assert hashlib.file_digest(stream, "sha256").hexdigest() == session["sha256"], path
        previous, model, updates = {}, None, []
        with path.open() as stream:
            for line_number, line in enumerate(stream, 1):
                event = json.loads(line)
                if timestamp(event["timestamp"]) >= cutoff:
                    continue
                payload = event.get("payload", {})
                if event["type"] == "turn_context":
                    model = payload.get("model", model)
                if event["type"] != "event_msg" or payload.get("type") != "token_count" or not payload.get("info"):
                    continue
                info = payload["info"]
                current = info["total_token_usage"]
                assert current.get("cache_write_input_tokens", 0) == 0, "Cache writes require separate lifetime accounting"
                delta = {k: current.get(k, 0) - previous.get(k, 0) for k in KEYS}
                previous = current
                if not any(delta.values()):
                    continue
                assert model in pricing["models"], model
                last = info["last_token_usage"]
                long_context = last["input_tokens"] > pricing["long_context_threshold_input_tokens"]
                # Nonmonotone snapshots occur only in short-context GPT-5.5
                # sessions here. Reject ambiguous surcharge attribution.
                if long_context:
                    assert delta["total_tokens"] == last["total_tokens"], (session["session_id"], line_number)
                updates.append((model, long_context, delta))
        assert all(previous.get(k, 0) == int(session[k]) for k in KEYS), session["session_id"]
        long_session_models = {m for m, is_long, _ in updates
                               if is_long and pricing["models"][m]["long_context_scope"] == "session"}
        total, flat_total, accounted = ZERO, ZERO, collections.Counter()
        long_updates = 0
        for model, long_request, delta in updates:
            is_long = long_request or model in long_session_models
            key = (session["scope"], session["kind"], model)
            grouped[key].update(delta)
            grouped[key]["counter_updates"] += 1
            grouped[key]["long_context_updates"] += int(is_long)
            charged, flat = cost(delta, model, is_long), cost(delta, model)
            costs[key] += charged
            flat_costs[key] += flat
            total += charged
            flat_total += flat
            accounted.update(delta)
            long_updates += int(is_long)
        assert all(accounted[k] == int(session[k]) for k in KEYS), session["session_id"]
        if long_updates:
            surcharged_sessions.add(session["session_id"])
        session_rows.append(dict(session_id=session["session_id"], scope=session["scope"],
                                 kind=session["kind"], models=session["models"],
                                 long_context_updates=long_updates, usd=money(total),
                                 usd_without_long_context_premium=money(flat_total)))

    model_rows = []
    for key, usage in sorted(grouped.items()):
        scope, kind, model = key
        model_rows.append(dict(scope=scope, kind=kind, model=model, **dict(usage),
                               usd=money(costs[key]),
                               usd_without_long_context_premium=money(flat_costs[key])))
    aggregate_rows = []
    for scope, kind in sorted({k[:2] for k in costs}):
        keys = [k for k in costs if k[:2] == (scope, kind)]
        aggregate_rows.append(dict(scope=scope, kind=kind,
                                   usd=money(sum((costs[k] for k in keys), ZERO))))

    episode_rows = []
    session_map = {s["session_id"]: s for s in sessions}
    for episode in csv.DictReader((args.data / "episodes.csv").open()):
        model = session_map[episode["session_id"]]["models"]
        # Every selected recovery episode uses GPT-5.5 below the threshold.
        assert model == "gpt-5.5" and episode["session_id"] not in surcharged_sessions
        episode_rows.append(dict(episode=episode["episode"], session_id=episode["session_id"],
                                 model=model, usd=money(cost({k: int(episode[k]) for k in KEYS}, model))))

    write_csv(args.data / "api-cost-by-model.csv", model_rows)
    write_csv(args.data / "api-cost-by-session.csv", session_rows)
    write_csv(args.data / "api-cost-by-episode.csv", episode_rows)
    summary = dict(pricing_checked_on=pricing["checked_on"], currency=pricing["currency"],
                   processing_tier=pricing["processing_tier"], priced_sessions=len(session_rows),
                   aggregates=aggregate_rows, all_priced_usd=money(sum(costs.values(), ZERO)),
                   unpriced_sessions=unpriced, assumptions=pricing["assumptions"])
    (args.data / "api-cost-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
