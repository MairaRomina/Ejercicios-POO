from claseAlumno import Alumno
from claseManAlumno import Manejador

if __name__ == '__main__': #linea donde comienza a ejecutar el programa
    lista = Manejador() #se crea una instancia de la clase Manejador
    a1 = Alumno( 'Luis Perez', '19587', 7.45 ) #se crea instancias de la clase Alumno
    a2 = Alumno( 'Alamino Jesica', '17578', 1.25 )
    a3 = Alumno( 'Javier Torres', '20489', 8.41 )
    
    lista.agregar( a1 ) #se agrega los objetos a la lista
    lista.agregar( a2 )
    lista.agregar( a3 )
    
    lista.ordenar() #ordena la lista por notas de mayor a menor nota
    print(lista) #se imprime la lista ordenada por pantalla
    
    lista.eliminar() #elimina las notas menores a 6.00
    print(lista) #se imprime la lista con las notas mayores a 6.00