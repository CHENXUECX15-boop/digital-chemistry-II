import pandas as pd
import json
import networkx as nx
import matplotlib.pyplot as plt

# Read files
molecules = pd.read_csv("molecules.csv")
rxn = pd.read_csv("rxn.csv")
rxn_detail = pd.read_csv("rxn-detail.csv")

# Merge reaction tables
df = rxn.merge(rxn_detail, on="reaction_id")

# -----------------------------
# Build JSON structure
# -----------------------------
nodes = []
for _, row in molecules.iterrows():
    nodes.append({
        "id": row["molecule_id"],
        "label": row["name"]
    })

edges = []
for _, row in df.iterrows():
    edges.append({
        "id": row["reaction_id"],
        "source": row["source_id"],
        "target": row["target_id"],
        "reaction_type": row["reaction_type"],
        "equation": row["equation"],
        "yield_percent": row["yield_percent"],
        "temperature_C": row["temperature_C"]
    })

network = {
    "nodes": nodes,
    "edges": edges
}

# Save JSON
with open("rxn-net.json", "w") as f:
    json.dump(network, f, indent=4)

print("rxn-net.json created!")

# -----------------------------
# Draw Graph
# -----------------------------
G = nx.DiGraph()

# Add nodes
for n in nodes:
    G.add_node(n["id"], label=n["label"])

# Add edges
for e in edges:
    G.add_edge(e["source"], e["target"], label=e["reaction_type"])

plt.figure(figsize=(12,8))
pos = nx.spring_layout(G, seed=42)

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=2000)

# Draw labels
labels = nx.get_node_attributes(G, "label")
nx.draw_networkx_labels(G, pos, labels)

# Draw edges
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='->', arrowsize=20)

# Edge labels
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Reaction Network")
plt.axis("off")
plt.tight_layout()
plt.savefig("rxn-net.png", dpi=300)
plt.show()