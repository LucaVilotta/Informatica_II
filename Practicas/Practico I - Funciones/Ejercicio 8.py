
## Declaración de la función
def sumatoria(a,b):
    suma=0
    for i in range(a,b+1):
        suma += i
    return suma
## Uso de la funcion
a=int(input("Ingrese un número: "))
b=int(input("Ingrese otro número: "))
print(sumatoria(a,b))
