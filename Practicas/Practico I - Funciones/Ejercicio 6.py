
## Declaración de la función
def raiz(N, a):
    return a**(1/N)
## Uso de la funcion
N = float(input("Ingrése el N: "))
a = float(input("Ingrese el a: "))
print("La raiz resultante es: %.2f"%(raiz(N,a)))

