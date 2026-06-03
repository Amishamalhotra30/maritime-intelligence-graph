import json
from collections import defaultdict

from intelligence.region_mapper import PORT_TO_REGION


with open("data/cargoes.json") as f:
    cargoes = json.load(f)


profiles = defaultdict(lambda: {
    "cargoes": [],
    "load_regions": [],
    "discharge_regions": []
})


for cargo in cargoes:

    broker = cargo.get("broker")

    if not broker:
        continue

    profiles[broker]["cargoes"].append(
        cargo["cargo_name"]
    )

    profiles[broker]["load_regions"].append(
        PORT_TO_REGION.get(
            cargo["loading_port"],
            "UNKNOWN"
        )
    )

    profiles[broker]["discharge_regions"].append(
        PORT_TO_REGION.get(
            cargo["discharge_port"],
            "UNKNOWN"
        )
    )


print("\n===== BROKER PROFILES =====\n")

for broker, data in profiles.items():

    print("Broker:", broker)

    print(
        "Preferred Cargoes:",
        ", ".join(set(data["cargoes"]))
    )

    print(
        "Load Regions:",
        ", ".join(set(data["load_regions"]))
    )

    print(
        "Discharge Regions:",
        ", ".join(set(data["discharge_regions"]))
    )

    print(
        "Activity Score:",
        len(data["cargoes"])
    )

    print("-" * 50)