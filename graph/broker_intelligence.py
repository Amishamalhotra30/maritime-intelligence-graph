import json
from collections import defaultdict

with open("cargoes.json", "r") as f:
    cargoes = json.load(f)

broker_stats = defaultdict(int)

for cargo in cargoes:

    broker = cargo.get("broker")

    if broker:
        broker_stats[broker] += 1

print("\n===== BROKER ACTIVITY =====\n")

for broker, count in broker_stats.items():

    print(
        broker,
        "->",
        count,
        "cargo opportunities"
    )