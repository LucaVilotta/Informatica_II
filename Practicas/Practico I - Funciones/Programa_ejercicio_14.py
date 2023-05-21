from Modulo_ejercicio_14 import *

####Programa para aplicar el módulo del ejercicio 14:

##Generamos una matriz cuadrada aleatorea y la guardamos en una variable para aplicar a las demás funciones
matriz_programa = matriz_aleatoria(4, 4)

##La imprimo por consola para ver la matriz a usar en las funciones y poder corroborar el correcto funcionamiento de las mismas
for fila in matriz_programa:
    print(" ".join("{:3}".format(num) for num in fila))
print()

##Verificamos si es simétrica con la función es_simetrica (agrego un pirnt)
print("Verificamos si es simétrica con la función es_simetrica:")
es_simetrica(matriz_programa)
print()

##Corroboramos si un valor dado existe en la matriz con la función buscar_valor, en esta caso elegí el número 7
print("Corroboramos si el valor 7 existe en la matriz con la función buscar_valor:")
buscar_valor(matriz_programa,7)
print()

##Mostramos el máximo valor de cada fila en un solo mensaje con la función mostrar_max_fila
print("Mostramos el máximo valor de cada fila en un solo mensaje:")
mostrar_max_fila(matriz_programa)
print()

##Genera una matriz que tendrá tantas filas como valores mayores al valor ingresado fueron encontrados
#Las filas tendrán la forma [i,j] donde i y j son los índices del valor de la matrz que superó al valor ingresado
#i son las filas y j el indice del valor dento de esa fila
#El número elegido esta vez es el 5
print("Genera una matriz que tendrá tantas filas como valores mayores al valor ingresado fueron encontrados y devuelve \nuna matriz con los índices del valor en cada fila:")
buscar_indices(matriz_programa,5)
print()

####FIN DEL PROGRAMA
print("FIN DEL PROGRAMA")