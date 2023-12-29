import pandas as pd
import os
from dotenv import load_dotenv
import re

load_dotenv()
CSV_PATH = os.getenv("CSV_PATH")

# Normalización de los datos
filepath = CSV_PATH
file = pd.read_csv(filepath, low_memory=False, na_values='NaN', keep_default_na=False)


def normalize_names(original_names):
    new_names = []
    for original in original_names:
        new_name = original.replace(" ", "_").lower()
        new_names.append({original: new_name})
    return new_names


for column in normalize_names(file.columns.values):
    file.rename(columns=column, inplace=True)

file = file.loc[:, "jurisdicción":"mail"]
file = file.loc[file["jurisdicción"] == "Santa Fe"]

pattern = r'\d+'

for i, row in file.iterrows():
    try:
        file.loc[i, 'nro'] = re.findall(pattern, row["nombre"])[0]
    except:
        continue


def get_file():
    return file
