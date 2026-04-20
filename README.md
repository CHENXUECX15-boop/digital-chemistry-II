# digital-chemistry-II

## Overview

This project converts separate CSV tables into structured JSON data and builds a reaction network for chemical compounds. It demonstrates how tabular chemical data can be linked, transformed, queried, and visualized using Python.

---

# Part A: Molecular Records

Three CSV files were provided:

* `molecules.csv`
* `properties.csv`
* `safety.csv`

These tables were linked using the shared key `molecule_id`.

For each compound, one structured JSON object was created in `molecules.json`.

Each record contains:

* identity information
* physical properties
* safety information

This shows how separate flat tables can be combined into reusable structured records.

---

# Part B: Reaction Network

Two reaction tables were used:

* `rxn.csv`
* `rxn-detail.csv`

These were linked using `reaction_id`.

A reaction network was generated and saved as:

* `rxn-net.json`
* `rxn-net.png`

## Network Structure

* compounds are represented as **nodes**
* reactions are represented as **directed edges**

Each edge stores:

* reaction type
* equation
* yield
* temperature

This allows chemical transformations to be represented as a graph.

---

# Part C: Simple Query

A Python script was created to search the reaction network.

The selected query was:

**Find all oxidation reactions**

The script loads `rxn-net.json`, filters all edges where:

`reaction_type = oxidation`

and prints:

* reaction ID
* reactant
* product
* equation
* yield
* temperature

A total of 11 oxidation reactions were found.

---

# Reflection

This assignment shows how structured data improves chemical information management.

Using IDs such as `molecule_id` and `reaction_id` makes it easy to connect multiple datasets consistently.

Compared with separate CSV files, JSON and graph structures are more flexible for searching, visualization, and future automation.

The workflow is reproducible and can be extended to larger reaction databases.
