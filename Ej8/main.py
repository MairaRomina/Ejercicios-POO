from claseConjunto import Conjunto
from claseMenu import Menu

if __name__ == '__main__':
    A = Conjunto( [1,2,3,4] )
    B = Conjunto( [3,6,9,1] )
    
    menu = Menu()
    
    salir = True
    while salir:
        print('-------------------- MENU --------------------')
        print('1. Union')
        print('2. Diferencia')
        print('3. Comparacion')
        print('4. Salir')
        
        op = input('Opcion: ')
        menu.opcion( op, A, B )
        #print( listaViajero )
    # else:
    #     print('Adios!')