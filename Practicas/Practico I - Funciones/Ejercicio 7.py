
## Declaración de la función
def tipo_triangulo(lado1,lado2,lado3):
    if lado1==lado2 and lado1==lado3:
        return "Equilátero"
    elif (lado1==lado2 and lado1!=lado3) or (lado3==lado1 and lado3!=lado1) or (lado3==lado2 and lado3!=lado1):
        return "Isóseles"
    else:
        return "Escaleno"
## Uso de la funcion
lado1=float(input("Ingrese el lado 1: "))
lado2=float(input("Ingrese el lado 2: "))
lado3=float(input("Ingrese el lado 3: "))

print(tipo_triangulo(lado1,lado2,lado3))