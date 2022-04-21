import csv
from claseRegistro import Registro

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def __str__ (self):
        s = ""
        for registro in self.__lista:
            s += str( registro ) + '\n'
        return s

    def agregarRegistro (self, unRegistro):
        self.__lista.append( unRegistro )

    def test (self):
        archivo = open( 'Enero.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                #dia = fila[0]
                #hora = fila[1]
                temp = fila[2]
                hum = fila[3]
                pre = fila[4]
                unRegistro = Registro( temp, hum, pre )
                self.agregarRegistro( unRegistro )
        archivo.close()