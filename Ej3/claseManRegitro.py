import csv
from claseRegistro import Registro

class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def __str__ (self):   #modifico la funcion str para mostrar bien la lista
        s = ""
        for fila in range(len(self.__lista)):
            for columna in range(len(self.__lista[fila])):
                s += str( self.__lista[fila][columna] ) + '\n'
        return s

    def agregarRegistro (self): #crea la lista bidimencional con None
        dia = 2
        hora = 24
        self.__lista =[[None] * hora ] * dia #dia(fila) x hora(columna)
        print( self.__lista ) 
        

    def test (self): #carga la lista con el archivo csv
        archivo = open( 'Enero.csv' )
        reader = csv.reader( archivo, delimiter = ',' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera #saltea la cabecera
            else:
                dia = int(fila[0])
                hora = int(fila[1])
                temp = int(fila[2])
                hum = int(fila[3])
                pre = int(fila[4])
                self.__lista[dia-1][hora] = Registro( temp, hum, pre )
        archivo.close()


    def mostrarDH (self): #opcion 1
        for fila in range( len( self.__lista ) ):
            print('---------------------- Para el dia {} ----------------------: '.format( fila + 1 ))

            for columna in range( len( self.__lista[ fila ] ) ):
                print('La hora registrada es {} y sus datos fueron: '.format( columna ))
                print( self.__lista[fila - 1][columna - 1] )

    def promedioTemp (self): #opcion 2 
        #2dias x 24 horas --- dia1 + dia2 +dia3
        dia = len( self.__lista )
        print('cantidad de dias', dia)
        hora = 24
        prom = 0
        for columna in range( hora ):
            for fila in range( dia ):
                prom += self.__lista[fila][columna].getTemperatura()
            print('Promedio de la temperatura para el dia {} fue {}'.format( dia, prom / dia ))   #{:10} cadena {:.2f} float    

    def listar (self): #opcion 3
        print('opcion 3 en el manejador')
