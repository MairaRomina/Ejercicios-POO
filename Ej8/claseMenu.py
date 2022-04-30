from claseConjunto import Conjunto
#from os import system

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.salir,
        }

    def opcion (self, op, A, B):
        func = self.__switcher.get( op, lambda: print('Opcion no valida') )
        if op == '1' or op == '2' or op == '3':
            func( A, B )
        else:
            func()
                
    def opcion1 (self, A, B): #union de 2 conjutos opcion1
        print('----------------- Union -----------------')
        print( A + B )

    def opcion2 (self, A, B): #diferencia entre 2 conjuntos opcion2
        print('----------------- Diferencia -----------------')
        print( A - B )

    def opcion3 (self, A, B): #verificar si son iguales o diferentes 2 conjutos opcion3
        print('----------------- Igualdad -----------------')
        print( A == B )
        
    def salir (self):
        print('Salir')