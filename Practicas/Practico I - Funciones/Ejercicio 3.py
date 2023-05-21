## Declaración de la función
def es_mayuscula(cadena):
    return 65<=ord(cadena[0])<=90
        
## Uso de la funcion
cadena = input("Ingrese una cadena: ")

##Prints de salida
if es_mayuscula(cadena):
    print("La cadena empieza por mayúscula")
else:
    print("La cadena empieza por minúscula")
