import json


with open("data/vessels.json", "r") as f:
    vessels = json.load(f)

with open("data/cargoes.json", "r") as f:
    cargoes = json.load(f)

print("\n===== OPPORTUNITY REPORT =====\n")

for cargo in cargoes:

    load_port = cargo.get("loading_port")

    matching_vessels = []

    for vessel in vessels:

        if vessel.get("open_port") == load_port:
            matching_vessels.append(
                vessel["vessel_name"]
            )

    print(f"Cargo       : {cargo['cargo_name']}")
    print(f"Load Port   : {load_port}")
    print(f"Discharge   : {cargo['discharge_port']}")

    if matching_vessels:

        print(
            f"Match Found : {', '.join(matching_vessels)}"
        )

    else:

        print(
            "Match Found : NONE"
        )

        print(
            "Opportunity : HIGH PRIORITY"
        )

    print("-" * 40)