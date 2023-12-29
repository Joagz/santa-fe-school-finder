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