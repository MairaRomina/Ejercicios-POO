import csv
from claseViajero import Viajero

class Manejador:
    __lista = []
    
    def __init__(self):
        self.__lista = []
        
    def __str__(self):      #muestra informacion de la lista
        s = ""
        for viajero in self.__lista:
            s += str( viajero ) + '\n'
        return s
        
    def agregarViajero (self, viajero):
        self.__lista.append(viajero)
        
    def cargarArchivo (self):
        archivo = open( 'registroViajeros.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                ide = int(fila[0])
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas = int(fila[4])
                unViajero = Viajero( ide, dni, nombre, apellido, millas )
                self.agregarViajero( unViajero )
        archivo.close()

    def buscarIndice(self, numero):
        if type( numero ) == int:
            for indice, viajero in enumerate( self.__lista ):
                if viajero.getIdentificador() == numero:
                    #print('manejador ',indice)
                    objeto = self.buscarViajero(indice)
                    return objeto
        else:
            print('Error de tipo en buscar viajero')        
            
    def buscarViajero (self, indice):
        viajero = self.__lista[ indice ]
        return viajero