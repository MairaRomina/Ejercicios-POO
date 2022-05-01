from claseAlumno import Alumno

class Manejador: #clase que maneja la lista de objetos
    __lista = [] #atributo lista
    
    def __init__ (self):
        self.__lista = [] #inicializacion de la lista
        
    def __str__ (self): #metodo que imprime la lista de objetos
        s = ""
        for alumno in self.__lista:
            s += str( alumno) + '\n'
        return s
    
    def agregar (self, unAlumno): #agrega un objeto Alumno al final de la lista
        self.__lista.append( unAlumno )

    def ordenar (self): #llama al metodo de la clase Alumno y le envia la lista para ordenar
        Alumno.ordenar( self.__lista )
        
    def eliminar (self): #metodo que elimina las notas menores a 6.00
        for i in range( len( self.__lista ) ):
            if self.__lista[i].getNota() < 6.00:
                self.__lista.remove( self.__lista[i] )
    