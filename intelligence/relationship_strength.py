import json
from collections import defaultdict

with open("data/cargoes.json") as f:
    cargoes = json.load(f)

broker_cargo = defaultdict(int)
broker_route = defaultdict(int)

for cargo in cargoes:

    broker = cargo.get("broker")

    if not broker:
        continue

    cargo_type = cargo.get("cargo_name")

    route = (
        cargo.get("loading_port"),
        cargo.get("discharge_port")
    )

    broker_cargo[(broker, cargo_type)] += 1
    broker_route[(broker, route)] += 1

print("\n===== RELATIONSHIP STRENGTH =====\n")

for (broker, cargo_type), count in broker_cargo.items():

    print(
        f"{broker} ↔ {cargo_type} : {count}"
    )

print("\n----- ROUTES -----\n")

for (broker, route), count in broker_route.items():

    print(
        f"{broker} ↔ {route[0]} -> {route[1]} : {count}"
    )