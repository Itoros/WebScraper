
from DataManager import read_file, save_file
from Parser.Ahumada import Ahumada

from Parser.Salcobrand import Salcobrand


def main():

    remedios = read_file("princios_activos.txt")
    lista_vacia = []

    lista_csv = Ahumada(remedios, lista_vacia)

    lista_csv_final = Salcobrand(remedios, lista_csv)

    save_file(lista_csv_final)

if __name__ == "__main__":
    main()
