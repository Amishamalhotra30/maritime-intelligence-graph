from extraction.extractor import extract_tonnage
from save_entities import save_vessel


email = """
MV SHENG AN HAI DWT 56564 OPEN XIAMEN, CHINA O/A 2ND JUNE 2026
"""

data = extract_tonnage(email)

print(data)

save_vessel(data)

print("Saved successfully!")