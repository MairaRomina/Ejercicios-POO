from claseManCama import ManejadorCama
from claseManMed import ManejadorMed


if __name__ == '__main__':
    arregloCama = ManejadorCama( 3 )
    listaMedicamento = ManejadorMed()
    
    arregloCama.test() #punto 1
    listaMedicamento.test() #punto 2
    
    print(arregloCama)
    print(listaMedicamento)
    
    #punto 3
    nom = input('Ingrese el nombre y apellido del paciente para darle el alta: ')
    idC = arregloCama.darAlta( nom )
    listaMedicamento.mostrar( idC )
    print(arregloCama)
    
    #punto 4
    diag = input('Ingrese un diagnostico para buscar pacientes con ese diagnostico: ')
    arregloCama.buscar( diag )
    