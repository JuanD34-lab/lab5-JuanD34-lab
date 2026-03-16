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
    