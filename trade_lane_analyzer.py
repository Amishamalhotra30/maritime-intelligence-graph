import json
from collections import defaultdict

from intelligence.region_mapper import PORT_TO_REGION


with open("data/cargoes.json", "r") as f:
    cargoes = json.load(f)


trade_lanes = defaultdict(list)

for cargo in cargoes:

    load_region = PORT_TO_REGION.get(
        cargo["loading_port"],
        "UNKNOWN"
    )

    discharge_region = PORT_TO_REGION.get(
        cargo["discharge_port"],
        "UNKNOWN"
    )

    lane = f"{load_region} -> {discharge_region}"

    trade_lanes[lane].append(
        cargo["cargo_name"]
    )


print("\n===== TRADE LANE ANALYSIS =====\n")

for lane, cargo_list in trade_lanes.items():

    print("Trade Lane:", lane)

    print(
        "Cargoes:",
        ", ".join(cargo_list)
    )

    print(
        "Cargo Count:",
        len(cargo_list)
    )

    print("-" * 50)