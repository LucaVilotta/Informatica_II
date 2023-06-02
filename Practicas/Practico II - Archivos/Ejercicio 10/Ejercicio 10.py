##### EJERCICIO 10 PROGRAMA PRINCIPAL ######

## IMPORTS
from ej10_module import *

## Código
# Print principal para mostrar los productos y sus códigos
print("PROGRAMA PARA REGISTRAR UNA VENTA: \n")
mostrar_productos()
print()
#Inputs
codigo = input("Ingrese el código del producto a vender: ")
cantidad = int(input("Ingrese la cantidad de producto que desea vender: "))
codigo = codigo.upper()

#while para verificar stock y la existencia del producto
while True:
    if not existe_prod(codigo):
        codigo = input("Porfavor ingrese un código existente: ")
    elif not stock_disponible(codigo,cantidad):
        cantidad = int(input("Ingrese una nueva cantidad: "))
    else:
        agregar_venta(codigo,cantidad)
        restar_stock(codigo,cantidad)
        break

##### FIN PROGRAMA PRINCIPAL ######