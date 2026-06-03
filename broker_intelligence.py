import json
from collections import defaultdict


with open("data/cargoes.json") as f:
    cargoes = json.load(f)

broker_stats = defaultdict(list)

for cargo in cargoes:

    broker = cargo.get("broker")

    if broker:

        broker_stats[broker].append(
            cargo["cargo_name"]
        )

print("\n===== BROKER INTELLIGENCE =====\n")

for broker, cargos in broker_stats.items():

    print("Broker:", broker)

    print(
        "Cargo Types:",
        ", ".join(cargos)
    )

    print("-" * 40)