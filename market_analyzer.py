import json

from intelligence.region_mapper import get_region


with open("data/vessels.json") as f:
    vessels = json.load(f)

with open("data/cargoes.json") as f:
    cargoes = json.load(f)


regions = {}


# Cargoes

for cargo in cargoes:

    region = get_region(
        cargo["loading_port"]
    )

    if region not in regions:

        regions[region] = {
            "cargoes": 0,
            "vessels": 0
        }

    regions[region]["cargoes"] += 1


# Vessels

for vessel in vessels:

    region = get_region(
        vessel["open_port"]
    )

    if region not in regions:

        regions[region] = {
            "cargoes": 0,
            "vessels": 0
        }

    regions[region]["vessels"] += 1


print("\n===== MARKET ANALYSIS =====\n")

for region, data in regions.items():

    score = data["cargoes"] - data["vessels"]

    print(f"Region : {region}")
    print(f"Cargoes : {data['cargoes']}")
    print(f"Vessels : {data['vessels']}")

    if score > 0:
        print("Opportunity : HIGH")

    elif score == 0:
        print("Opportunity : BALANCED")

    else:
        print("Opportunity : EXCESS TONNAGE")

    print("-" * 40)