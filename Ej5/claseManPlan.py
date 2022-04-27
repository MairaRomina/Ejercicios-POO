import csv
from clasePlanAhorro import Plan
from os import system

class Manejador:
    __lista = []
    
    def __init__(self):
        self.__lista = []
        
    def __str__ (self):
        s = " "
        for plan in self.__lista:
            s += str( plan ) + '\n'
        return s
    
    def test (self):
        archivo = open( 'planes.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                codigo = int( fila[0] )
                modelo = fila[1]
                version = fila[2]
                precio = int( fila[3] )
                cantC = int( fila[4] )
                unPlan = Plan( codigo, modelo, version, precio, cantC )
                self.__lista.append( unPlan )
        archivo.close()
       
    def actualizar (self): #opcion1
        for i in range( len( self.__lista ) ):
            print('----------> Plan ',i+1)
            print('Codigo: {} - Modelo: {} - Version: {}'.format( self.__lista[i].getCodigo(), self.__lista[i].getModelo(), self.__lista[i].getVersion() ))
            valor = int(input('Ingresa el nuevo valor del plan: '))
            self.__lista[i].setPrecio( valor )
        system('cls')
        print('***Valores actualizados correctamente ***')
        
    #valor cuota = (importe vehículo/ cantidad de cuotas) + importe vehículo * 0.10
    
    def mostrarValor (self): #opcion2
        precio = int(input('Ingrese un valor: '))
        bandera = 0
        for i in range( len( self.__lista ) ):
            valor = (self.__lista[i].getPrecio() // self.__lista[i].getCantCuotas()) + self.__lista[i].getPrecio() * 0.10
            print('valores',valor)
            if valor <= precio:
                bandera += 1
                print('-----> Plan valor: ',valor)
                print('Codigo: {} - Modelo: {} - Version: {}'.format( self.__lista[i].getCodigo(), self.__lista[i].getModelo(), self.__lista[i].getVersion() )) 
            
        if bandera == 0:
            system('cls')
            print('No se encontro un valor menor al valor ingresado, lo sentimos.')    
            
    '''Mostrar el monto que se debe haber pagado para licitar el vehículo 
    (cantidad de cuotas para licitar * importe de la cuota).''' 
    
    def mostrarMonto (self): #opcion3
          for i in range( len( self.__lista ) ):
              valorC = (self.__lista[i].getPrecio() // self.__lista[i].getCantCuotas()) + self.__lista[i].getPrecio() * 0.10
              monto = self.__lista[i].getCuotaLicitar() * valorC
              print('monto', monto)
              
    def modificar (self):
        codigo = int(input('Ingrese el codigo de un plan: '))
        b = 0
        for i in range( len( self.__lista ) ):
            if codigo == self.__lista[i].getCodigo():
                valor = int(input('Ingrese nuevo valor para las cuotas a licitar: '))
                Plan.cuotaLicitar = valor
                print('*** Valor actualizado ***')
                b += 1
        if b == 0:
            system('cls')
            print('Codigo ingresado incorrecto')
            
    