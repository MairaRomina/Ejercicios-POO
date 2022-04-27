from claseManPlan import Manejador
from claseMenu import Menu

if __name__ == '__main__':
    #primer cosa que tengo que hacer es actualizar el valor del auto
    listaPlan = Manejador()
    listaPlan.test()
    print( listaPlan )
    
    menu = Menu()
    
    salir = False
    while not salir:
        print('-------------------- MENU --------------------')
        print('1. Actualizar el valor del vahiculo')
        print('2. Mostrar por precio menor al ingresado')
        print('3. Mostrar monto que debe ser pagado')
        print('4. Modificar cuotas para licitar')
        print('5. Salir')
        
        op = input('Opcion: ')
        salir = menu.opcion( op, listaPlan )
        print( listaPlan )
    else:
        print('Adios!')