from claseManEmail import Manejador
from os import system


if __name__ == '__main__':
    nombre = input('Ingrese su nombre: ')
    mail = input('Ingrese su email: ')
    contraseña = input('Ingrese su contraseña: ')
    
    mLista = Manejador()
    otroEmail = mLista.verifcarCuenta( mail, contraseña )
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format( nombre, otroEmail.retornaEmail() ))
    system('Pause')
    system('cls')
    
    #lista con los correos cargados a partir del csv
    print('---------------- Muestra creacion de cuentas de correo ----------------')
    mLista.crearCuentaCsv()
    system('Pause')
    system('cls')
    print('---------------- Lista Correos ----------------')
    print( mLista )
    
    idC = input('Ingrese el identificador de cuenta que desee buscar: ')
    print('Se encontro {} veces en el archivo'.format( mLista.buscarIdCuenta( idC ) ))
    