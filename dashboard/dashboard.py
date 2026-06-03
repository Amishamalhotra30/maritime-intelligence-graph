import json
from collections import defaultdict
import matplotlib.pyplot as plt


# ====================================
# REGION MAPPING
# ====================================

REGIONS = {

    # Middle East
    "JEDDAH": "MIDDLE EAST",
    "BUSHEHR": "MIDDLE EAST",
    "BIK": "MIDDLE EAST",
    "DOHA": "MIDDLE EAST",
    "SOHAR": "MIDDLE EAST",

    # North Africa
    "GABES": "NORTH AFRICA",
    "CASABLANCA": "NORTH AFRICA",
    "BEJAIA": "NORTH AFRICA",

    # Far East
    "XIAMEN": "FAR EAST",
    "VUNG ANG": "FAR EAST",

    # Europe
    "BILBAO": "EUROPE",
    "ISKENDERUN": "EUROPE"
}


def get_region(port):

    if not port:
        return "UNKNOWN"

    return REGIONS.get(
        port.upper(),
        "UNKNOWN"
    )


# ====================================
# LOAD DATA
# ====================================

with open("data/cargoes.json", "r") as f:
    cargoes = json.load(f)

with open("data/vessels.json", "r") as f:
    vessels = json.load(f)


# ====================================
# KPI METRICS
# ====================================

cargo_count = len(cargoes)

vessel_count = len(vessels)

broker_count = len(
    set(
        cargo["broker"]
        for cargo in cargoes
        if cargo["broker"]
    )
)

# ====================================
# TOP BROKER
# ====================================

broker_activity = defaultdict(int)

for cargo in cargoes:

    broker = cargo.get("broker")

    if broker:
        broker_activity[broker] += 1


if broker_activity:

    top_broker = max(
        broker_activity,
        key=broker_activity.get
    )

else:

    top_broker = "NONE"


# ====================================
# OPPORTUNITY SCORES
# ====================================

region_scores = defaultdict(int)

# Cargo demand

for cargo in cargoes:

    region = get_region(
        cargo["loading_port"]
    )

    region_scores[region] += 10

# Vessel supply

for vessel in vessels:

    region = get_region(
        vessel["open_port"]
    )

    region_scores[region] -= 5


regions = list(
    region_scores.keys()
)

scores = list(
    region_scores.values()
)


# ====================================
# DASHBOARD
# ====================================
# ====================================
# DASHBOARD
# ====================================

fig, ax = plt.subplots(
    figsize=(12, 7)
)

# Leave room for KPI row
plt.subplots_adjust(top=0.78)

bars = ax.bar(
    regions,
    scores
)

# Value labels

for bar in bars:

    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.5,
        str(height),
        ha="center"
    )

# Title

ax.set_title(
    "Maritime Intelligence Graph Dashboard",
    fontsize=16,
    pad=20
)

ax.set_ylabel(
    "Opportunity Score"
)

ax.set_xlabel(
    "Region"
)

# KPI PANEL

fig.text(
    0.08,
    0.93,
    f"Cargoes: {cargo_count}",
    fontsize=11,
    weight="bold"
)

fig.text(
    0.28,
    0.93,
    f"Open Vessels: {vessel_count}",
    fontsize=11,
    weight="bold"
)

fig.text(
    0.50,
    0.93,
    f"Brokers: {broker_count}",
    fontsize=11,
    weight="bold"
)

fig.text(
    0.68,
    0.93,
    f"Top Broker: {top_broker}",
    fontsize=11,
    weight="bold"
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.savefig(
    "dashboard/dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDashboard generated successfully!")