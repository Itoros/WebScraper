
from DataManager import read_file, save_file
from Parser.Ahumada import Ahumada

from Parser.Salcobrand import Salcobrand




def main():

    remedios = read_file("/Users/Jose/Desktop/UAI/Algebra lineal/Visual/lyp/WebScraper-main/princios_activos.txt")
    lista_vacia = []

    lista_csv = Salcobrand(remedios, lista_vacia)

    lista_csv_final = Ahumada(remedios, lista_csv)

    save_file(lista_csv_final)

if __name__ == "__main__":
    main()
