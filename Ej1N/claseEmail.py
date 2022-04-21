class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contraseña = ''
    
    def __init__(self, idCuenta = None, dominio = None, tipoDominio = None, contraseña = None):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña
        
    def __str__(self):  
        return "%s %s %s %s " % (self.__idCuenta, self.__dominio, self.__tipoDominio, self.__contraseña)
    
    def retornaEmail (self):
        return '' + self.__idCuenta + '@' + self.__dominio + '.' + self.__tipoDominio
    
    def getDominio (self):
        return self.__dominio 
    
    def getID (self):
        return self.__idCuenta
    
    def cambiarContraseña (self):
        password = input('Ingrese su contraseña actual :')
        
        if self.__contraseña == password:
            nueva = input('Ingrese su nueva contraseña: ')
            self.__contraseña = nueva
            print('Contraseña actualizada')
        else:
            print('Contraseña incorrecta')
            
    