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


def extract_tc_cargo(text):

    result = {

        "account_name": None,
        "cargo_name": None,
        "delivery_port": None,
        "redelivery_port": None,
        "duration": None,
        "laycan": None
    }

    # ------------------------
    # Account
    # ------------------------

    acc_match = re.search(
        r"(?:ACC|A\/C)\s+([A-Z\s]+)",
        text,
        re.IGNORECASE
    )

    if acc_match:

        result["account_name"] = normalize_text(
            acc_match.group(1)
            .split("\n")[0]
        )

    # ------------------------
    # Cargo
    # ------------------------

    cargo_match = re.search(
        r"TCT\s+WITH\s+([A-Z ]+?)(?:\n|$)",
        text,
        re.IGNORECASE
    )

    if cargo_match:

        result["cargo_name"] = normalize_text(
            cargo_match.group(1)
        )

    # ------------------------
    # Delivery
    # ------------------------

    delivery_match = re.search(
        r"DELIVERY\s+([^\n]+)",
        text,
        re.IGNORECASE
    )

    if delivery_match:

        result["delivery_port"] = normalize_text(
            delivery_match.group(1)
        )

    # ------------------------
    # Redelivery
    # ------------------------

    redelivery_match = re.search(
        r"(?:REDELIVERY|REDEL)\s+([^\n]+)",
        text,
        re.IGNORECASE
    )

    if redelivery_match:

        result["redelivery_port"] = normalize_text(
            redelivery_match.group(1)
        )

    # ------------------------
    # Duration
    # ------------------------

    duration_match = re.search(
        r"DURATION\s+([^\n]+)",
        text,
        re.IGNORECASE
    )

    if duration_match:

        result["duration"] = normalize_text(
            duration_match.group(1)
        )

    # ------------------------
    # Laycan
    # ------------------------

    laycan_match = re.search(
        r"LAYCAN\s+([^\n]+)",
        text,
        re.IGNORECASE
    )

    if laycan_match:

        result["laycan"] = normalize_text(
            laycan_match.group(1)
        )

    return result