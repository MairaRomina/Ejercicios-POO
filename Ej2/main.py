from claseManViajero import Manejador
from claseMenu import Menu
from os import system

from claseViajero import Viajero

def test (self):
    unViajero = Viajero( 12, 30265789, 'balmaceda', 'raul', 456 )
    dosViajero = Viajero( 13, 54789654, 'hojeda', 'marcelo', 100 )
    tresViajero = Viajero( 14, 56123456, 'zapata', 'ruben', 789 )
    cuatroViajero = Viajero( 15, 32456123, 'flores', 'lorenzo', 321 )
    lista = Manejador()
    lista = [ unViajero, dosViajero, tresViajero, cuatroViajero ]
    
    


if __name__ == '__main__':
    listaManejador = Manejador()  #lista con los viajeros que estaban en el csv
    listaManejador.cargarArchivo() #carga la lista con el archivo csv
    
    menu  = Menu() #crea una instancia de tipo Menu
    
    test()
    
    print(listaManejador)
    
    # numV = int( input('Ingrese el numero de viajero: ') )
    # indice = listaManejador.buscarIndice( numV )
    # print(indice)
    
    salir = False
    op = 0
    while not salir: #verifica que la opcion no sea salir
        
        
        numV = int( input('Ingrese el numero de viajero: ') )
        objetoV = listaManejador.buscarIndice( numV )
        
        
        print('-------------------- MENU --------------------')
        print('1. Consultar cantidad de millas')
        print('2. Acumular millas')
        print('3. Canjear millas')
        print('4. Salir')
        
        correcto = False
        while (not correcto): #verifica que la opcion sea un numero entre el 1 y el 5
            try: 
                op = int( input('ingrese una opcion: ') )
                correcto = True
            except ValueError: 
                print('Error, introduce un numero entero')
        if op == 1:
            menu.opcion( op, objetoV )
            system('pause')
            system("cls")
        elif op == 2:
            menu.opcion( op, objetoV )
            system('pause')
            system("cls")
        elif op == 3:
            menu.opcion( op, objetoV )
            system('pause')
            system("cls")
        elif op == 4:
            salir = True
            system("cls")
        else: 
            print('Elige un numero entre el 1 y el 4')
    else:
        print('Adios')
    
    
    