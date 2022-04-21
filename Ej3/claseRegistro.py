class Registro:
    __temperatura: int
    __humedad: int
    __presion: int

    def __init__ (self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion

    def __str__ (self):
        hora = 0
        print('En la hora {} se resgitraron'.format( hora ))
        return ('Temperatura {} - Humedad {} - Presion {}'.format( self.__temperatura, self.__humedad, self.__presion ))

    
