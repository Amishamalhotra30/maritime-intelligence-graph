import re


def normalize_text(value):

    if not value:
        return None

    return (
        value.replace("\n", " ")
        .replace("  ", " ")
        .strip()
        .upper()
    )


def extract_broker(text):

    patterns = [

        r"MCD\s+([A-Z ]+)",

        r"ATT\.\s*CHARTERING\s*DESK.*?\n.*?([A-Z ]+)",

        r"A/C\s+([A-Z ]+)",

        r"ACC\s+([A-Z ]+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:

            return normalize_text(
                match.group(1)
            )

    return None


def extract_cargo_name(text):

    patterns = [

        # Cargo:30,000 mts of Urea in bulk
        r"Cargo:\s*[\d,\-]+\s*mts?\s*of\s*([A-Z ]+?)\s+in\s+bulk",

        # 20-30,000 mts iron slag in bulk
        r"[\d,\-]+\s*mts?\s+([A-Z ]+?)\s+in\s+bulk",

        # 20 000 mt HRC
        r"[\d,\s]+\s*mt\s+([A-Z0-9]+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            return normalize_text(
                match.group(1)
            )

    return None


def extract_vc_cargo(text):

    result = {
        "broker": None,
        "cargo_name": None,
        "loading_port": None,
        "discharge_port": None,
        "laycan": None
    }

    # -----------------------
    # Broker
    # -----------------------

    result["broker"] = extract_broker(text)

    # -----------------------
    # Cargo Name
    # -----------------------

    result["cargo_name"] = extract_cargo_name(text)

    # -----------------------
    # Loading Port
    # -----------------------

    load_match = re.search(
        r"(?:LOAD PORT|POL)\s*:\s*([A-Z\s]+)",
        text,
        re.IGNORECASE
    )

    if load_match:

        result["loading_port"] = normalize_text(
            load_match.group(1).split("\n")[0]
        )

    else:

        route_match = re.search(
            r"([A-Z ]+)\s*/\s*([A-Z ]+)",
            text,
            re.IGNORECASE
        )

        if route_match:

            result["loading_port"] = normalize_text(
                route_match.group(1)
            )

    # -----------------------
    # Discharge Port
    # -----------------------

    discharge_match = re.search(
        r"(?:DISCHARGE PORT|POD)\s*:\s*([A-Z\s]+)",
        text,
        re.IGNORECASE
    )

    if discharge_match:

        result["discharge_port"] = normalize_text(
            discharge_match.group(1).split("\n")[0]
        )

    else:

        route_match = re.search(
            r"([A-Z ]+)\s*/\s*([A-Z ]+)",
            text,
            re.IGNORECASE
        )

        if route_match:

            result["discharge_port"] = normalize_text(
                route_match.group(2)
            )

    # -----------------------
    # Laycan
    # -----------------------

    laycan_match = re.search(
        r"LAYCAN\s*:\s*([A-Z0-9\-\s]+)",
        text,
        re.IGNORECASE
    )

    if laycan_match:

        result["laycan"] = normalize_text(
            laycan_match.group(1).split("\n")[0]
        )

    else:

        date_match = re.search(
            r"(\d+\s+[A-Z]+\s*-\s*\d+\s+[A-Z]+)",
            text,
            re.IGNORECASE
        )

        if date_match:

            result["laycan"] = normalize_text(
                date_match.group(1)
            )

    return result