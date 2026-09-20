# Avocado Toast Supply Chain Analysis

Python project analyzing the supply chain of key avocado toast ingredients sold in the United Kingdom using data from the Open Food Facts database.

## Objective

Identify the most common country of origin for three key ingredients:

- avocado
- olive oil
- sourdough bread

The analysis:

- selects relevant product information from each dataset
- filters products using ingredient-specific category tags
- limits the analysis to products available in the United Kingdom
- identifies the most frequent country of origin for each ingredient
- cleans origin names by removing prefixes and special characters

The final results are stored in:

- top_avocado_origin
- top_olive_oil_origin
- top_sourdough_origin

## Files
- notebook.ipynb - project notebook with the Python analysis
- data/avocado.csv - avocado product data
- data/olive_oil.csv - olive oil product data
- data/sourdough.csv - sourdough bread product data
- data/relevant_avocado_categories.txt - relevant avocado category tags
- data/relevant_olive_oil_categories.txt - relevant olive oil category tags
- data/relevant_sourdough_categories.txt - relevant sourdough category tags
- solution.py - final Python script with the complete analysis

## Data Source

Data is provided by the Open Food Facts database.