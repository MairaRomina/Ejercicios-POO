from claseManViajero import Manejador
from os import system

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.salir,
        }

    def opcion (self, op, objetoLista):
        func = self.__switcher.get( op, lambda: print('Opcion no valida') )
        if op == '1' or op == '2' or op == '3':
            func( objetoLista )
        else:
            func()
                
    def opcion1 (self, objV): #quien tiene mayor cantidad de millas
        system('cls')
        print('**** Comparar Millas ****')
        objV.comparar()
        
    def opcion2 (self, objV): #acumular millas
        system('cls')
        print('**** Acumular Millas ****')
        acum = int(input('Ingrese cantidad de millas recorridas que desea acumular: '))
        objV.acumMillas( acum )
    
    def opcion3 (self, objV): #canjear millas
        system('cls')
        print('**** Canjear Millas ****')
        objV.canjearMillas()
        #print('Resultado en el menu', res)
        
    def salir (self):
        print('Salir')