import typer
import pandas as pd

file = pd.read_csv("./data/out.csv", low_memory=False, na_values='NaN', keep_default_na=False)

def main():
    while True :
        print("Buscar por número: ")
        nombre = input()
        search(nombre)
    print("Toca para cerrar")


def search(nro):
    table = file.loc[file["nro"] == nro].head()
    table = table[["sector", "localidad", "nombre", "teléfono"]]
    print(table.to_markdown())

if __name__ == "__main__":
    typer.run(main)