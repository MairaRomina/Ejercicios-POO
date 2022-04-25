from claseManRegitro import Manejador
from claseMenu import Menu
from os import system


if __name__ == '__main__':
    listaRegistros = Manejador()
    listaRegistros.agregarRegistro()
    listaRegistros.test()
    print( listaRegistros ) #muestra la lista

    menu = Menu()

    op = 0
    while op != 4:
        print('--------------- Menu de opciones ---------------')
        print('1. Mostrar max y min por cada dia')
        print('2. Temperatura promedio por hora')
        print('1. Listar informacion por dia')
        print('4. Salir')
        op =  input('Opcion: ')
        menu.opcion( op, listaRegistros)

    else:
        system('clear')
        print('Adios')
