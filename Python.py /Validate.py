import os

def solo_strings(string: str) -> bool:
    
    '''Recorre el string indice por indice y verifica que no tenga 
    numeros'''
    os.system('cls')
    
    for i in range(len(string)):
        if string[i] >= '0' and string[i] <= '9':
            return False
    return True 

def validate_number(numero, minimo, maximo):
    """Valida si un número está dentro de un rango."""
    return minimo <= numero <= maximo

def validate_length(cadena, longitud):
    """Valida si la longitud de la cadena es igual a la longitud esperada."""
    return len(cadena) == longitud
