import json
from collections import defaultdict

from intelligence.region_mapper import PORT_TO_REGION


with open("data/cargoes.json") as f:
    cargoes = json.load(f)

with open("data/vessels.json") as f:
    vessels = json.load(f)


cargo_count = defaultdict(int)
broker_count = defaultdict(set)
vessel_count = defaultdict(int)


# Cargoes

for cargo in cargoes:

    region = PORT_TO_REGION.get(
        cargo["loading_port"],
        "UNKNOWN"
    )

    cargo_count[region] += 1

    if cargo.get("broker"):

        broker_count[region].add(
            cargo["broker"]
        )


# Vessels

for vessel in vessels:

    region = PORT_TO_REGION.get(
        vessel["open_port"],
        "UNKNOWN"
    )

    vessel_count[region] += 1


print("\n===== OPPORTUNITY SCORES =====\n")

all_regions = set(
    list(cargo_count.keys()) +
    list(vessel_count.keys())
)

for region in all_regions:

    score = (
        cargo_count[region] * 10
        -
        vessel_count[region] * 5
        +
        len(broker_count[region]) * 20
    )

    print("Region:", region)

    print(
        "Cargoes:",
        cargo_count[region]
    )

    print(
        "Vessels:",
        vessel_count[region]
    )

    print(
        "Brokers:",
        len(broker_count[region])
    )

    print(
        "Opportunity Score:",
        score
    )

    print("-" * 50)