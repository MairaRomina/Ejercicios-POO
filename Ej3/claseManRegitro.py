import csv
from claseRegistro import Registro

import csv
from claseRegistro import Registro

class Manejador:
    __lista = []

    def __init__(self, D, H):
        self.__lista = [ [ 0 for i in range( H )] for j in range( D ) ] #creacion y inicializacion con 0 de la lista bidimencional

    def __str__ (self):   #modifico la funcion str para mostrar bien la lista
        s = ""
        for fila in range(len(self.__lista)):
            for columna in range(len(self.__lista[fila])):
                s += str( self.__lista[fila][columna] ) + '\n'
        return s
    
    def test (self): #carga la lista con las instacias de registro
        archivo = open( 'Enero.csv' )
        reader = csv.reader( archivo, delimiter = ',' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                dia = int( fila[0] )
                hora = int( fila[1] )
                temp = int( fila[2] )
                hum = int( fila[3] )
                pre = int( fila[4] )
                unRegistro = Registro( temp, hum, pre )
                self.__lista[dia-1][hora] = unRegistro
        archivo.close()   
        
    def maximo (self): #opcion1
        tempM = 0
        humM = 0
        preM = 0
        for dia in range( len( self.__lista ) ):
            for hora in range( 24 ):
                if tempM < self.__lista[dia][hora].getTemperatura():
                    tempM = self.__lista[dia][hora].getTemperatura()
                    diaT = dia + 1
                    horaT = hora
                if humM < self.__lista[dia][hora].getHumedad():
                    humM = self.__lista[dia][hora].getHumedad()
                    diaH = dia + 1
                    horaH = hora
                if preM < self.__lista[dia][hora].getPresion():
                    preM = self.__lista[dia][hora].getPresion()
                    diaP = dia + 1
                    horaP = hora
        print('------------- Temperatura -------------')
        print('Dia {:2} hora {:2} - temperatura mayor: {:4}'. format( diaT, horaT, tempM ))
        
        print('------------- Humedad -------------')
        print('Dia {:2} hora {:2} - humedad mayor: {:4}'. format( diaH, horaH, humM ))
        
        print('------------- Presion -------------')
        print('Dia {:2} hora {:2} - presion mayor: {:4}'. format( diaP, horaP, preM ))
    
    def minimo (self): #opcion1
        tempM = 9999999
        humM = 9999999
        preM = 9999999
        for dia in range( len( self.__lista ) ):
            for hora in range( 24 ):
                if tempM > self.__lista[dia][hora].getTemperatura():
                    tempM = self.__lista[dia][hora].getTemperatura()
                    diaT = dia + 1
                    horaT = hora
                if humM > self.__lista[dia][hora].getHumedad():
                    humM = self.__lista[dia][hora].getHumedad()
                    diaH = dia + 1
                    horaH = hora
                if preM > self.__lista[dia][hora].getPresion():
                    preM = self.__lista[dia][hora].getPresion()
                    diaP = dia + 1
                    horaP = hora
        print('------------- Temperatura -------------')
        print('Dia {} hora {} - temperatura menor: {}'. format( diaT, horaT, tempM ))
        
        print('------------- Humedad -------------')
        print('Dia {} hora {} - humedad menor: {}'. format( diaH, horaH, humM ))
        
        print('------------- Presion -------------')
        print('Dia {} hora {} - presion menor: {}'. format( diaP, horaP, preM ))
    
    def promedioTemperatura (self): #opcion2
        listaProm = [ 0 for i in range( 24 )]
        
        for dia in range( len( self.__lista) ):
            for hora in range( 24 ):
                listaProm[hora] += self.__lista[dia][hora].getTemperatura()

        for i in range( 24 ):
            print('Hora {:2}:00 tuvo un promedio: {:6}'.format( i, listaProm[i]/2 ))
            
    def mostrar (self): #opcion3
        dia = int(input('Ingrese un dia: '))
        print('{:2}    {:4}   {:6}   {:8}'.format('Hora', 'Temperatura', 'Humedad', 'Presion'))
        for hora in range( 24 ):
             print('{:2}:00    {:4}   {:10}   {:8}'.format( hora, self.__lista[dia-1][hora].getTemperatura(), self.__lista[dia-1][hora].getHumedad(), self.__lista[dia-1][hora].getPresion()))
