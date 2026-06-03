import json
import matplotlib.pyplot as plt
import networkx as nx

from graph.graph_builder import build_graph

with open("data/vessels.json", "r") as f:
    vessels = json.load(f)

with open("data/cargoes.json", "r") as f:
    cargoes = json.load(f)

G = build_graph(vessels, cargoes)

plt.figure(figsize=(18, 12))

pos = nx.spring_layout(
    G,
    seed=42,
    k=1.5,
    iterations=100
)

nx.draw_networkx_nodes(
    G,
    pos,
    node_size=3000
)

nx.draw_networkx_labels(
    G,
    pos,
    font_size=8,
    font_weight="bold"
)

nx.draw_networkx_edges(
    G,
    pos,
    width=2.5,
    arrows=True,
    arrowsize=20
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

plt.axis("off")

plt.tight_layout()

plt.savefig(
    "frontend/public/graph.png",
    bbox_inches="tight",
    dpi=300
)

plt.close()

print("Graph saved successfully!")

