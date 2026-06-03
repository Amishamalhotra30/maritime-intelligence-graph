import os

from extraction.classifier import classify_email
from extraction.extractor import extract_tonnage
from extraction.cargo_extractor import extract_vc_cargo
from extraction.tc_extractor import extract_tc_cargo
print("\n===== MARITIME INTELLIGENCE PIPELINE =====\n")

email_folder = "data/emails"

for file in os.listdir(email_folder):

    path = os.path.join(
        email_folder,
        file
    )

    with open(
        path,
        encoding="utf-8"
    ) as f:

        text = f.read()

    category = classify_email(text)

    print(f"\nFILE: {file}")
    print(f"TYPE: {category}")

    if category == "TONNAGE":

        data = extract_tonnage(text)

    elif category == "VC":

        data = extract_vc_cargo(text)
    
    elif category == "TC":

        data = extract_tc_cargo(text)

    else:

        data = {}

    print(data)

print("\nPipeline Completed")