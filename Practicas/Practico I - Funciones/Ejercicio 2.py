## Imports
from math import pi

## Declaración de la función
def grados_a_radianes(grado):
    radianes = grado*(pi/180)
    return radianes

## Uso de la funcion
grado = float(input("Ingrese ángulo a convertir en radianes: "))
print("El ángulo de %.2f grados equivale a %.2f rad"%(grado, grados_a_radianes(grado)))