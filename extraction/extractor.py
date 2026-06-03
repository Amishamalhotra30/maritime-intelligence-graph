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


def extract_tonnage(text):

    result = {
        "vessel_name": None,
        "vessel_size": None,
        "open_port": None,
        "open_date": None
    }

    # --------------------------------
    # Vessel Name
    # --------------------------------

    vessel_patterns = [

        r"M\/V\s+([A-Z\s]+?)\s+DWT",

        r"MV\s+([A-Z\s]+?)\s+DWT",

        r"MV\s+([A-Z\s]+?)\s*\(",

        r"MV\s+([A-Z\s]+?)\/",

        r"([A-Z\s]+?)\s*\(\d+K"
    ]

    for pattern in vessel_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            result["vessel_name"] = normalize_text(
                match.group(1)
                .replace("MV ", "")
                .replace("M/V ", "")
            )

            break

    # --------------------------------
    # Vessel Size
    # --------------------------------

    size_patterns = [

        r"DWT\s+(\d+)",

        r"\((\d+)K",

        r"\/(\d+)K\/",

        r"\/(\d+)K",

        r"(\d{5,6})\s*DWT"
    ]

    for pattern in size_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            result["vessel_size"] = (
                match.group(1)
                .strip()
            )

            break

    # --------------------------------
    # Open Port
    # --------------------------------

    port_patterns = [

        # TRUE FRIEND/51K/09 - BEJAIA , 1ST JUNE
        r"\/\d+K\/.*?-\s*([A-Z ]+?)\s*,",

        # OPEN XIAMEN, CHINA O/A
        r"OPEN\s+([A-Z ]+?),\s*[A-Z ]+\s+O\/A",

        # OPEN VUNG ANG, VIETNAM 08-12 JUNE
        r"OPEN\s+([A-Z ]+?),\s*[A-Z ]+\s+\d",

        # OPEN 25 MAY GABES, TUNISIA
        r"OPEN\s+\d+\s+[A-Z]+\s+([A-Z ]+?),",

        # OPEN CASABLANCA O/A
        r"OPEN\s+([A-Z ]+?)\s+O\/A",

        # fallback
        r"-\s*([A-Z ]+?)\s*,"
    ]

    for pattern in port_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            result["open_port"] = normalize_text(
                match.group(1)
            )

            break

    # --------------------------------
    # Open Date
    # --------------------------------

    date_patterns = [

        # TRUE FRIEND , 1ST JUNE
        r",\s*(\d+(?:ST|ND|RD|TH)?\s+[A-Z]+)",

        # O/A 2ND JUNE 2026
        r"O\/A\s+([^\n]+)",

        # 08-12 JUNE
        r"(\d+\-\d+\s+[A-Z]+)"
    ]

    for pattern in date_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            result["open_date"] = normalize_text(
                match.group(1)
            )

            break

    return result