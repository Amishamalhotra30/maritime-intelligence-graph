import json


def save_cargo(cargo_data):

    try:
        with open("data/cargoes.json", "r") as f:
            cargoes = json.load(f)

    except:
        cargoes = []

    cargoes.append(cargo_data)

    with open("data/cargoes.json", "w") as f:
        json.dump(
            cargoes,
            f,
            indent=4
        )