import json
from collections import defaultdict

with open("data/cargoes.json") as f:
    cargoes = json.load(f)

# New incoming cargo
new_cargo = {
    "cargo_name": "STEEL",
    "loading_port": "JEDDAH",
    "discharge_port": "BILBAO"
}

broker_scores = defaultdict(int)

for cargo in cargoes:

    broker = cargo.get("broker")

    if not broker:
        continue

    if cargo["loading_port"] == new_cargo["loading_port"]:
        broker_scores[broker] += 30

    if cargo["discharge_port"] == new_cargo["discharge_port"]:
        broker_scores[broker] += 30

    if cargo["cargo_name"] == new_cargo["cargo_name"]:
        broker_scores[broker] += 40

print("\n===== BROKER RECOMMENDATION =====\n")

for broker, score in sorted(
    broker_scores.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{broker}: {score}")