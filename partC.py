import json

# Load reaction network
with open("rxn-net.json", "r") as f:
    data = json.load(f)

# -----------------------------------
# Build molecule ID -> name dictionary
# -----------------------------------
name_map = {}

for node in data["nodes"]:
    name_map[node["id"]] = node["label"]

# -----------------------------------
# Query: find all oxidation reactions
# -----------------------------------
results = []

for edge in data["edges"]:
    if edge["reaction_type"].lower() == "oxidation":

        item = {
            "id": edge["id"],
            "source": edge["source"],
            "source_name": name_map.get(edge["source"], edge["source"]),
            "target": edge["target"],
            "target_name": name_map.get(edge["target"], edge["target"]),
            "reaction_type": edge["reaction_type"],
            "equation": edge["equation"],
            "yield_percent": edge["yield_percent"],
            "temperature_C": edge["temperature_C"]
        }

        results.append(item)

# -----------------------------------
# Save JSON file
# -----------------------------------
with open("oxidation-results.json", "w") as f:
    json.dump(results, f, indent=4)

# -----------------------------------
# Print results
# -----------------------------------
print("=" * 60)
print("Oxidation Reactions in Reaction Network")
print("=" * 60)

if len(results) == 0:
    print("No oxidation reactions found.")

else:
    for r in results:
        print(f"Reaction ID   : {r['id']}")
        print(f"Conversion    : {r['source_name']} -> {r['target_name']}")
        print(f"Equation      : {r['equation']}")
        print(f"Yield (%)     : {r['yield_percent']}")
        print(f"Temperature   : {r['temperature_C']} °C")
        print("-" * 60)

print(f"Total oxidation reactions found: {len(results)}")
print("Saved file: oxidation-results.json")