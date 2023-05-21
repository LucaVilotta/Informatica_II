## Imports
from math import pi

## Declaración de la función
def area_circulo(radio):
    return pi*(radio**2)
    

## Uso de la funcion
radio = float(input("Ingrese el radio del círculo: "))
print("El área del círculo es %.2f"%(area_circulo(radio)))