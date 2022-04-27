class Plan:
    __codigo = int
    __modelo = str
    __version = str
    __precio = int
    __cantCuotas = 84 #atributo de clase
    __cuotaLicitar = 15 #atributo de clase
    
    def __init__(self, codigo, modelo, version, precio, cuotas):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__precio = precio
        self.__cantCuotas = cuotas
                
    @classmethod
    def getCuotaLicitar (cls):
        return cls.__cuotaLicitar  
    
    @classmethod
    def setCuotaLicitar (cls, valor):
        cls.__cuotaLicitar =   valor  
        
    @classmethod
    def getCantCuotas (cls):
        return cls.__cantCuotas      
                
    def __str__ (self): 
        return '{} {} {} {} {} {} '.format(self.__codigo, self.__modelo, self.__version, self.__precio, self.getCantCuotas(), self.getCuotaLicitar())
    
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
    
    def getPrecio (self):
        return self.__precio
