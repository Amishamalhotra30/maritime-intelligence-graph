import json
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

# ----------------------
# Cargoes
# ----------------------

with open("data/cargoes.json") as f:
    cargoes = json.load(f)

for cargo in cargoes:

    broker = cargo.get("broker")
    cargo_name = cargo.get("cargo_name")
    load_port = cargo.get("loading_port")
    discharge_port = cargo.get("discharge_port")

    if broker:

        G.add_edge(
            broker,
            cargo_name,
            relation="OFFERS"
        )

    if cargo_name and load_port:

        G.add_edge(
            cargo_name,
            load_port,
            relation="LOADS_AT"
        )

    if cargo_name and discharge_port:

        G.add_edge(
            cargo_name,
            discharge_port,
            relation="DISCHARGES_AT"
        )

# ----------------------
# Vessels
# ----------------------

with open("data/vessels.json") as f:
    vessels = json.load(f)

for vessel in vessels:

    vessel_name = vessel.get("vessel_name")
    open_port = vessel.get("open_port")

    if vessel_name and open_port:

        G.add_edge(
            vessel_name,
            open_port,
            relation="OPEN_AT"
        )

# ----------------------
# Draw
# ----------------------

plt.figure(figsize=(14, 10))

pos = nx.spring_layout(
    G,
    k=2,
    seed=42
)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    font_size=8
)

edge_labels = nx.get_edge_attributes(
    G,
    "relation"
)

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=7
)

plt.show()