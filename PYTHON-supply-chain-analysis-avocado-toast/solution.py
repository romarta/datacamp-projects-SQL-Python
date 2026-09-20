import pandas as pd

# table headers
head_tabel = ['code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins', 'origins_tags']

# load csv with categories in txt
avocado = pd.read_csv("data/avocado.csv", sep="\t")
avocado_categories = pd.read_csv("data/relevant_avocado_categories.txt", header=None)[0].tolist()
avocado2 = avocado[head_tabel]
avocado3 = avocado2[avocado2['categories_tags'].str.contains("|".join(avocado_categories), na=False)]

olive_oil = pd.read_csv("data/olive_oil.csv", sep="\t")
olive_oil_categories = pd.read_csv("data/relevant_olive_oil_categories.txt", header=None)[0].tolist()
olive_oil2 = olive_oil[head_tabel]
olive_oil3 = olive_oil2[olive_oil2['categories_tags'].str.contains("|".join(olive_oil_categories), na=False)]

sourdough = pd.read_csv("data/sourdough.csv", sep="\t")
sourdough_categories = pd.read_csv("data/relevant_sourdough_categories.txt", header=None)[0].tolist()
sourdough2 = sourdough[head_tabel]
sourdough3 = sourdough2[sourdough2['categories_tags'].str.contains("|".join(sourdough_categories), na=False)]

# data filtering
avocado_uk = avocado3[avocado3['countries'] == 'United Kingdom']
top_avocado_origin = avocado_uk['origins_tags'].value_counts().sort_values(ascending=False).index[0]

olive_oil_uk =  olive_oil3[olive_oil3['countries'] == 'United Kingdom']
top_olive_oil_origin = olive_oil_uk['origins_tags'].value_counts().sort_values(ascending=False).index[0]

sourdough_uk =  sourdough3[sourdough3['countries'] == 'United Kingdom']
top_sourdough_origin = sourdough_uk['origins_tags'].value_counts().sort_values(ascending=False).index[0]

# function for removing extra characters
def zamiana (zmienna):
    return zmienna.replace("en:", "").replace("-", " ")

# results
top_avocado_origin = zamiana(top_avocado_origin)
top_olive_oil_origin = zamiana(top_olive_oil_origin)
top_sourdough_origin = zamiana(top_sourdough_origin)
