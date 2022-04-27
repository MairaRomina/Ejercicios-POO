from claseManRegitro import Manejador
from os import system

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.salir
        }

    def opcion (self, op, objetoLista):
        func = self.__switcher.get( op, lambda: print('Opcion no valida') )
        if op == '1' or op == '2' or op == '3':
            func( objetoLista )
        else:
            func()

    def opcion1 (self, objetoLista):  #mostrar variables por c/dia y hora
        if type( objetoLista ) == Manejador:
            system('cls')
            print('************************* Maximo y Minimo *************************')
            print('------> MAXIMO:')
            objetoLista.maximo()
            print('\n------> MINIMO:')
            objetoLista.minimo()
            system('pause') #raw_input("Press enter to continue") linux
            system('cls')
            #system('clear') linux
        else:
            print('Error de tipo en menu')

    def opcion2 (self, objetoLista): #muestra la temperatura promedio
        if type( objetoLista ) == Manejador:
            system('cls')
            print('************************* Promedio Temperatura Mensual Por Hora *************************')
            objetoLista.promedioTemperatura()
            system('pause') #raw_input("Press enter to continue") linux
            system('cls')
            #system('clear') linux
        else:
            print('Error de tipo en menu')

    def opcion3 (self, objetoLista): #dado un dia muestra por hora variables
        if type( objetoLista ) == Manejador:
            system('cls')
            print('************************* Mostrar Variables *************************')
            objetoLista.mostrar()
        else:
            print('Error de tipo en menu')

    def salir (self):
        #system('clear') linux
        system('cls')
        print('Usted salio del programa')
        return False
        
