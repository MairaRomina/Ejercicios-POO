from claseManPlan import Manejador
from claseManPlan import Plan
from os import system

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.salir
        }

    def opcion (self, op, objetoLista):
        func = self.__switcher.get( op, lambda: print('Opcion no valida') )
        if op == '1' or op == '2' or op == '3' or op == '4':
            func( objetoLista )
        else:
            func()

    def opcion1 (self, objetoLista):  
        if type( objetoLista ) == Manejador:
            system('cls')
            print('************************* Actualizacion *************************')
            objetoLista.actualizar()
            system('pause')
            system('cls')
        else:
            print('Error de tipo en menu')
        
    def opcion2 (self, objetoLista): 
        if type( objetoLista ) == Manejador:
            system('cls')
            print('************************* Mostrar valor de cuota inferior al ingresado *************************')
            objetoLista.mostrarValor()
            system('pause')
            system('cls')
        else:
            print('Error de tipo en menu')
        
    def opcion3 (self, objetoLista): 
        if type( objetoLista ) == Manejador:
            system('cls')
            print('************************* Mostrar monto para licitar vehiculo *************************')
            objetoLista.mostrarMonto()
            system('pause')
            system('cls')
        else:
            print('Error de tipo en menu')
    
    def opcion4 (self, objetoLista):
        if type( objetoLista ) == Manejador:
            system('cls')
            print('************************* Mosdificar cantidad de cuotas a licitar *************************')
            objetoLista.modificar()
            system('pause')
            system('cls')
        else:
            print('Error de tipo en menu')
        
    def salir (self):
        #system('clear') linux
        system('cls')
        print('Usted salio del programa')
        return True