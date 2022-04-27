class Plan:
    __codigo = int
    __modelo = str
    __version = str
    __precio = int
    __cantCuotas = int
    cuotaLicitar = 15 #variable de clase
    
    def __init__(self, codigo, modelo, version, precio, cuotas):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__precio = precio
        self.__cantCuotas = cuotas
                
    @classmethod
    def getCuotaLicitar (cls):
        return cls.cuotaLicitar  
    
    # @classmethod
    # def setCuotaLicitar (cls):
    #     valor = input('ingrese nuevo valor para las cuotas licitadas: ')
    #     cls.cuotaLicitar =   valor        
                
    def __str__ (self): 
        return '{} {} {} {} {} {} '.format(self.__codigo, self.__modelo, self.__version, self.__precio, self.__cantCuotas, self.getCuotaLicitar())
    
    def getCodigo (self):
        return self.__codigo
    
    def getModelo (self):
        return self.__modelo
    
    def getVersion (self):
        return self.__version
    
    def setPrecio(self, valor):
        if type( valor ) == int:
            self.__precio = valor
        else:
            print('Error de tipo en plan ahorro')
    
    def getCantCuotas (self):
        return self.__cantCuotas
    
    def getPrecio (self):
        return self.__precio