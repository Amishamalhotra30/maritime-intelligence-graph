import json
from collections import defaultdict

import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from intelligence.region_mapper import get_region


with open("data/cargoes.json") as f:
    cargoes = json.load(f)

with open("data/vessels.json") as f:
    vessels = json.load(f)


cargo_count = defaultdict(int)
vessel_count = defaultdict(int)

for cargo in cargoes:

    region = get_region(
        cargo["loading_port"]
    )

    cargo_count[region] += 1


for vessel in vessels:

    region = get_region(
        vessel["open_port"]
    )

    vessel_count[region] += 1


print("\n===== OPPORTUNITY DASHBOARD =====\n")

for region in set(
    list(cargo_count.keys())
    +
    list(vessel_count.keys())
):

    score = (
        cargo_count[region] * 10
        -
        vessel_count[region] * 5
    )

    print(
        region,
        "=",
        score
    )