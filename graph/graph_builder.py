import networkx as nx

def build_graph(vessels, cargoes):

    G = nx.Graph()

    # VESSELS
    for vessel in vessels:

        vessel_name = vessel.get("vessel_name")
        port = vessel.get("open_port")

        if vessel_name:
            G.add_node(vessel_name, type="VESSEL")

        if port:
            G.add_node(port, type="PORT")

        if vessel_name and port:
            G.add_edge(
                vessel_name,
                port,
                relation="OPEN_AT"
            )

    # CARGOES
    for cargo in cargoes:

        cargo_name = cargo.get("cargo_name")
        load_port = cargo.get("loading_port")
        discharge_port = cargo.get("discharge_port")

        if cargo_name:
            G.add_node(cargo_name, type="CARGO")

        if load_port:
            G.add_node(load_port, type="PORT")

        if discharge_port:
            G.add_node(discharge_port, type="PORT")

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

    return G