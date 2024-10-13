import os
import Validate

def get_string (message: str, message_error: str, message_error_largo= '' ,min= 1, max= 100) -> str:
    os.system('cls')
    dato = input(message).strip() #strip limpia espacioes del principio y final
    
    while Validate.solo_strings(dato) == False or dato == '':
        dato = input(message_error).strip()
    
    while len(dato) < min or len(dato) > max:
        dato = input(message_error_largo).strip()
    
    return dato

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> float | None:
    for intento in range(reintentos):
        try:
            numero = float(input(mensaje))
            if Validate.validate_number(numero, minimo, maximo):
                return numero
            else:
                print(mensaje_error)
        except ValueError:
            print(mensaje_error)
    return None

def get_string(longitud: int) -> str | None:
    while True:
        cadena = input(f"Introduce una cadena de longitud {longitud}: ")
        if Validate.validate_length(cadena, longitud):
            return cadena
        else:
            print(f"Error: La cadena debe tener exactamente {longitud} caracteres. Inténtalo de nuevo.")
