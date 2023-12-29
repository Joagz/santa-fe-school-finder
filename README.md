# Santa Fe School Finder CLI

Terminal app to find schools by their 'identifier' or number;

```python
import typer
from load_initial_data import get_file

def main():
    while True :
        print("Buscar por número: ")
        nombre = input()
        search(nombre)


def search(nro):
    file = get_file()

    table = file.loc[file["nro"] == nro].head()
    print(table.to_markdown())

if __name__ == "__main__":
    typer.run(main)
```

This simple file is in charge to find the school.

```python
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
```

This one takes the CSV file downloaded from the government's dataset, filters it and extracts each school number.

- To package the project run:
```
pyinstaller [main_file_path] --hidden-import tabulate

# (If you need to get the output file formatted)
pyinstaller [load_inital_data] --hidden-import tabulate

```
- (you must put "data" folder inside the "dist" folder to work the executables.)