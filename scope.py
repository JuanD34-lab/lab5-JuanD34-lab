# variables globales inicializadas en none

global_int = None
golabal_str = None

def set_globals(some_int, some_str):
    """
    Almacena un entero y una cadena en las variables globales.
    Entrada:
        some_int: entero
        some_str: cadena de texto
    salida:
        ninguna
    """
    global global_int, global_str
    global_int = some_int
    global_str = some_str

def get_globals():
    """
    Recupera los valores de las variables globales.
    Entrada:
        Ninguna
    salida:
        Tupla (int_value, str_value)
    """
    return (global_int, global_str)