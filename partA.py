import pandas as pd
import json

# Read CSV files
molecules = pd.read_csv("molecules.csv")
properties = pd.read_csv("properties.csv")
safety = pd.read_csv("safety.csv")

# Merge tables using molecule_id
df = molecules.merge(properties, on="molecule_id")
df = df.merge(safety, on="molecule_id")

# Build JSON structure
records = []

for _, row in df.iterrows():
    item = {
        "molecule_id": row["molecule_id"],
        "name": row["name"],
        "formula": row["formula"],
        "class": row["class"],
        "carbon_number": int(row["carbon_number"]),
        "notes": row["notes"],

        "properties": {
            "molar_mass_g_mol": float(row["molar_mass_g_mol"]),
            "phase_25C": row["phase_25C"]
        },

        "safety": {
            "flammable": row["flammable"],
            "signal_word": row["signal_word"],
            "hazard_category": row["hazard_category"]
        }
    }

    records.append(item)

# Save JSON file
with open("molecules.json", "w") as f:
    json.dump(records, f, indent=4)

print("molecules.json created successfully!")