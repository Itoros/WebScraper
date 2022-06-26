
import sys

from Parser.Ahumada import Ahumada
from Parser.CruzVerde import CruzVerde
from Parser.Salcobrand import Salcobrand


def main():

    paracetamol = "paracetamol"

    #Ahumada(paracetamol)
    CruzVerde(paracetamol)
    Salcobrand(paracetamol)

if __name__ == "__main__":
    main()
