# intelligence/region_mapper.py

PORT_TO_REGION = {

    # -------------------
    # Middle East
    # -------------------
    "JEDDAH": "MIDDLE EAST",
    "BUSHEHR": "MIDDLE EAST",
    "DOHA": "MIDDLE EAST",
    "SOHAR": "MIDDLE EAST",

    # -------------------
    # India
    # -------------------
    "KANDLA": "INDIA",
    "CHENNAI": "INDIA",

    # -------------------
    # North Africa
    # -------------------
    "GABES": "NORTH AFRICA",
    "CASABLANCA": "NORTH AFRICA",
    "BEJAIA": "NORTH AFRICA",

    # -------------------
    # Far East
    # -------------------
    "XIAMEN": "FAR EAST",
    "VUNG ANG": "FAR EAST",
    "GUANGZHOU": "FAR EAST",
    "MANILA": "FAR EAST",

    # -------------------
    # Europe
    # -------------------
    "BILBAO": "EUROPE",
    "ISKENDERUN": "EUROPE",

    # -------------------
    # Unknown / Not Mapped Yet
    # -------------------
    "BIK": "UNKNOWN"
}


def get_region(port):

    if not port:
        return "UNKNOWN"

    return PORT_TO_REGION.get(
        port.upper().strip(),
        "UNKNOWN"
    )