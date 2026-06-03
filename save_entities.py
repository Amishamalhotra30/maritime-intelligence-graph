import json


def save_vessel(vessel_data):

    try:
        with open("data/vessels.json", "r") as f:
            vessels = json.load(f)

    except:
        vessels = []

    vessels.append(vessel_data)

    with open("data/vessels.json", "w") as f:
        json.dump(
            vessels,
            f,
            indent=4
        )