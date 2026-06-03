from extraction.cargo_extractor import extract_vc_cargo
from save_cargo import save_cargo


emails = [

"""
MCD LIDOMAR

Att. Chartering Desk

Good day

Jeddah / Bilbao

20 000 mt HRC max 28,5 mt

FIOS

4000 mt fhinc / CQD disch

25 June - 5 July try later

3,75% here
""",

"""
PLS OFFER FIRM FOR FOLL OUR CLOSE AND DIR CHRTRS

20-30,000 mts iron slag in bulk

POL: Bushehr

POD: Doha

10000/12000

LAYCAN: 25-30 July

3.75% TTL
""",

"""
Cargo:30,000 mts of Urea in bulk

POL: BIK

POD: Iskenderun

5000/5000

LAYCAN: 16-20 July

COMM:1.25% TTL
"""
]


for email in emails:

    cargo = extract_vc_cargo(email)

    print("\nExtracted:")
    print(cargo)

    save_cargo(cargo)

print("\nCargoes saved successfully!")