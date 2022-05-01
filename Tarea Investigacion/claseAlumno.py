class Alumno: #clase que instancia los objetos de tipo Alumno
    __nombre = str  #atributos de la clase
    __registro = int
    __notaFinal = float
    
    def __init__ (self, nom, reg, nota): #costructor de la clase
        self.__nombre = nom
        self.__registro = reg
        self.__notaFinal = nota
        
    def __str__ (self): #metodo que permite imprimir los objetos con formato
        return ('Nombre: {} Registro: {} Nota Final: {}'.format( self.__nombre, self.__registro, self.__notaFinal ))
    
    def getNombre (self): #se retorna el atributo nombre del objeto solicitado
        return self.__nombre
    
    def getRegistro (self): #se retorna el atributo registro del objeto solicitado
        return self.__registro
    
    def getNota (self): #se retorna el atributo nota del objeto solicitado
        return self.__notaFinal
    
    def ordenar (lista): #metodo que ordena la lista de mayor a menor
        list.sort( lista, key = lambda Alumno: Alumno.__notaFinal, reverse = True )
        #se coloca key para indicarle el el atributo por el que debe ordenar
        #se coloca reverse = True para que ordene de mayor a menor
        #si este atributo reverse no se colocase, el metodo sort() por defecto ordena de menor a mayor
