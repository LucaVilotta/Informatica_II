## Declaración de la función
def cant_dias(año):
    if int(año/400) == float(año/400):
        return print("El %d tiene 366 días"%(año))
    else:
        return print("El %d tiene 365 días"%(año))
## Uso de la funcion
año = int(input("Ingrese el año: "))
cant_dias(año)