from claseManRegitro import Manejador
from claseMenu import Menu
from os import system


if __name__ == '__main__':
    D = 2 #para el caso de prueba utilice 2 dias 
    H = 24
    
    listaRegistros = Manejador( D, H ) #le doy al constructor valores para crear la lista bidimencional
    listaRegistros.test()
    #print(listaRegistros)
    
    menu = Menu()

    salir = True
    while salir:
        print('--------------- Menu de opciones ---------------')
        print('1. Mostrar max y min por cada dia')
        print('2. Temperatura promedio por hora')
        print('3. Listar informacion por dia')
        print('4. Salir')
        op =  input('Opcion: ')
        salir = menu.opcion( op, listaRegistros)
    else:    
        print('Adios!')  
