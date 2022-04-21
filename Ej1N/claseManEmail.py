import csv
from claseEmail import Email

class Manejador:
    __lista = []
    
    def __init__(self):
        self.__lista = []
    
    def __str__(self):
        s = ""
        for email in self.__lista:
            s += str( email ) + '\n'
        return s
        
    def agregarEmail (self, unEmail):
        self.__lista.append( unEmail )
    
    def crearCuentaCsv (self):
        archivo = open( 'RegCorreo.csv', 'r' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                if fila[0].find('@') != -1:
                    aux = fila[0].split('@')
                    idC = aux[0]
                    if aux[1].find('.') != -1:
                        domTipoDom = aux[1].split('.')
                        dom = domTipoDom[0]
                        tipoDom = domTipoDom[1]
                        password = fila[1]
                        unEmail = Email( idC, dom, tipoDom, password )
                        self.agregarEmail( unEmail )
                        print('*Correo creado con exito!*')
                    else:
                        print('Error al crear correo, no posee dom o tipo dominio ---->', fila[0])
                        
                else:
                    print('Error al crear correo, no posee @ o idCuenta ---->', fila[0])
    
    def verifcarCuenta (self, mail, password):
        if type( mail ) == str and type( password ) == str:
            if mail.find('@') != -1:
                aux = mail.split('@')
                idC = aux[0]
                if aux[1].find('.') != -1:
                    domTipoDom = aux[1].split('.')
                    dom = domTipoDom[0]
                    tipoDom = domTipoDom[1]
                    otroEmail = Email( idC, dom, tipoDom, password )
                    return otroEmail
                else:
                    print('Error al crear correo, no posee dom o tipo dominio ---->', mail)
            else:
                print('Error al crear correo, no posee @ o idCuenta ---->', mail)
        else:
            print('Error de tipo en verificar cuenta')
    
    def buscarIdCuenta (self, nombre):
        if type( nombre ) == str:
            cont = 0
            for indice, email in enumerate( self.__lista ):
                if email.getID() == nombre:
                    cont += 1
            return cont 
        else: 
            print('Error de tipo en buscar id cuenta')