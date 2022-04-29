class Viajero:
    __numViajero: int
    __dni: str
    __nombre: str
    __apellido: str
    __millasAcum: int
    
    def __init__(self, numViajero, dni, nombre, apellido, millasAcum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum
        
    def __str__(self):
        return ('Numero viajero: {} - Dni: {} - Nombre y Apellido: {} {} - Millas: {}'.format(self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millasAcum))
        
    def getIdentificador (self):
        return self.__numViajero
    
    def getcantidadMillas (self):
        return self.__millasAcum
    
    # def acumMillas (self, acum):
    #     if type( acum ) == int: 
    #         self.__millasAcum += acum
    #         print('Valor actualizado, cantidad de millas actuales: ', self.__millasAcum)
    #         return self.__millasAcum
    #     else:
    #         print('Error de tipo en acumular millas')
            
    def __gt__ (self, otro): #sobrecarga por izquierda mayor que
        if type( otro ) == Viajero:
            return self.__millasAcum > otro.__millasAcum   

    def __ge__ (self, otro):
        if type( otro ) == int:
            return self.__millasAcum >= otro    

    def __sub__ (self, otro): #canjea millas
        if type( otro ) == int:
            resta = self.__millasAcum - otro 
            return  Viajero(self.__numViajero, self.__dni, self.__nombre, self.__apellido, resta)    
        
    # def canjearMillas (self):
    #     cant = int(input('Ingrese la cantidad de millas que desea canjear: '))
    #     if type( cant ) == int:
    #         if self.__millasAcum >= cant:
    #             self.__millasAcum -= cant
    #             print('Valor actualizado, cantidad de millas actuales: ', self.__millasAcum)  
    #         else:
    #             print('Error en la operacion')
    #     else:
    #         print('Error de tipo en canjear millas')
    #     return self.__millasAcum

    def __add__ (self, otro): #acumula millas
        if type( otro ) == int:
            suma = otro + self.__millasAcum
            return Viajero(self.__numViajero, self.__dni, self.__nombre, self.__apellido, suma) 
        else: 
            print('Error de tipo en add')
