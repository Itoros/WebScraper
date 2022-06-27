import csv

def read_file(archivo):

    with open(archivo, "r", encoding="utf8") as Busquedas_Remedios:
        lines = Busquedas_Remedios.read().split('\n')

    return lines


def save_file(lista_csv):

    with open('Medicamentos.csv', 'w', newline = '') as Medicamentos:
        writer = csv.writer(Medicamentos)
        writer.writerows([lista_csv])