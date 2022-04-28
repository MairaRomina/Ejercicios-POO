from claseManViajero import Manejador
from claseMenu import Menu

if __name__ == '__main__':
    listaViajero = Manejador()
    listaViajero.test()
    #print( listaViajero )
    
    menu = Menu()
    
    salir = True
    while salir:
        print('-------------------- MENU --------------------')
        print('1. Consultar cantidad de millas')
        print('2. Acumular millas')
        print('3. Canjear millas')
        print('4. Salir')
        
        op = input('Opcion: ')
        menu.opcion( op, listaViajero )
        print( listaViajero )
    # else:
    #     print('Adios!')