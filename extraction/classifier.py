def classify_email(email_text):

    text = email_text.upper()

    # ------------------------
    # TC Cargo
    # ------------------------

    tc_keywords = [

        "TCT",
        "DELIVERY",
        "REDELIVERY",
        "REDEL",
        "DURATION"
    ]

    tc_score = sum(
        keyword in text
        for keyword in tc_keywords
    )

    if tc_score >= 2:
        return "TC"

    # ------------------------
    # VC Cargo
    # ------------------------

    vc_keywords = [

        "LOAD PORT",
        "DISCHARGE PORT",
        "POL",
        "POD",
        "LAYCAN"
    ]

    vc_score = sum(
        keyword in text
        for keyword in vc_keywords
    )

    if vc_score >= 2:
        return "VC"

    # ------------------------
    # Tonnage
    # ------------------------

    tonnage_keywords = [

        "OPEN",
        "DWT",
        "VESSEL",
        "MV"
    ]

    tonnage_score = sum(
        keyword in text
        for keyword in tonnage_keywords
    )

    if tonnage_score >= 2:
        return "TONNAGE"

    return "UNKNOWN"