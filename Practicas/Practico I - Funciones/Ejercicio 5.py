## Declaración de la función
def solo_letras(cadena):
    tiene = True
    for caracter in cadena:
        if (65>ord(caracter) or 90<ord(caracter)<97 or ord(caracter)>122) and (caracter!=" "):
            return False
    return tiene
## Uso de la funcion
cadena_p=input("Ingrese una cadena: ")
print(solo_letras(cadena_p))
