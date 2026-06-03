import json

from rapidfuzz import fuzz


with open("data/cargoes.json") as f:
    cargoes = json.load(f)

print("\n===== DUPLICATE DETECTION =====\n")

for i in range(len(cargoes)):

    for j in range(i + 1, len(cargoes)):

        c1 = cargoes[i]
        c2 = cargoes[j]

        score = fuzz.token_sort_ratio(

            f"{c1['cargo_name']} "
            f"{c1['loading_port']} "
            f"{c1['discharge_port']}",

            f"{c2['cargo_name']} "
            f"{c2['loading_port']} "
            f"{c2['discharge_port']}"
        )

        if score > 80:

            print("Possible Duplicate")

            print(
                c1["cargo_name"],
                "<->",
                c2["cargo_name"]
            )

            print(
                "Similarity:",
                score
            )

            print("-" * 40)