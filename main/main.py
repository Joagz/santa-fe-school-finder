import typer
from load_initial_data import get_file
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
CSV_PATH = os.getenv("CSV_PATH")

file = pd.read_csv(CSV_PATH, low_memory=False, na_values='NaN', keep_default_na=False)

def main():
    while True :
        print("Buscar por número: ")
        nombre = input()
        search(nombre)
    print("Toca para cerrar")


def search(nro):
    file = get_file()

    table = file.loc[file["nro"] == nro].head()
    table = table.loc["sector","departamento", "localidad", "nombre", "teléfono", "mail"]
    print(table.to_markdown())

if __name__ == "__main__":
    typer.run(main)