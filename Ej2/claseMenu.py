from os import system
from claseViajero import Viajero

class Menu:
    __op: int
    
    def __init__(self):
        self.__op = None
    
    def getOpcion (self):
        return self.__op
    
    def opcion (self, op, instanciaViajero):
        if (type( instanciaViajero ) == Viajero) and (type(op) == int):
            if op == 1:
                self.opcion1( instanciaViajero )
            elif op == 2: 
                print('Opcion 2')
                self.opcion2( instanciaViajero )
            elif op == 3:
                print('Opcion 3')
                self.opcion3( instanciaViajero )
        else:
            self.salir()
            print('Error de tipo en el menu')
                
    def opcion1 (self, objV):
        system('cls')
        print('**** Consultar Millas ****')
        cant = objV.cantidadTotalMillas()
        print('Cantidad actual de millas: ', cant)
        
    def opcion2 (self, objV):
        system('cls')
        print('**** Acumular Millas ****')
        objV.acumMillas()
        #print('Resultado en el menu', res )
    
    def opcion3 (self, objV):
        system('cls')
        print('**** Canjear Millas ****')
        objV.canjearMillas()
        #print('Resultado en el menu', res)
        
    def salir (self):
        print('Salir')