def list_shift(lista, valor):
    """
    modifica la lista sumando 'valor' a cada elemento de la lista.
    Entrada:
        lista: lista de flotantes
         valor: flotante a sumar
    salida:
        ninguna (la lista se modifica en su lugar)
        """
    for i in range(len(lista)):
        lista[i] += valor

def calc_average(lista):
    """
    calcula el promedio de los elementos de la lista de flotantes.
    Entrada:
        lista: lista de flotantes (no vacía)
    Salida:
        flotante con la media aritmética 
    """
    return sum(lista) / len(lista)
def print_normalized(lista):
    """
    Imprime cada elemento de la lista de flotantes.
    Entrada:
        lista: lista de flotantes
    salida:
        ninguna (solo imprime)
    """
    print(lista)
    
    