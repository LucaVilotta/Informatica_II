## Parcial informática II ejercicio 1:
## Diseñe la función procesa_lista(lis) que retorne el máximo, el mínimo y el promedio...
##...de la lista pasada como parámetro. Los valores calculados deben ser devueltos en una lista con la siguiente forma:...
##...[max,min,prom].




def procesa_lista(lista):
    # Variables a utilizar: 
    mayor_actual = 0
    menor_actual = 0
    sumatoria = 0
    cantidad_numeros = 0
    verif_menor_actual = 0
    
    # Iteración de la lista:
    for numero in lista: # for que itera la lista para guardar cada numero en la variable con este nombre:
        if numero > mayor_actual: # condicional para verificar si el numero en la variable es mayor al mayor actual
            mayor_actual = numero
        elif (numero < menor_actual) or verif_menor_actual == 0:# condicional para verificar si el numero en la variable es menor al menor actual, tambien se asegura que en la primer iteración entre a la variable
            menor_actual = numero
            verif_menor_actual = 1
        sumatoria += numero # sumatoria para el promedio
        cantidad_numeros += 1 # cantidad de numeros para el promedio
    
    promedio = sumatoria/cantidad_numeros # cálculo del promedio
    lista_procesada = [mayor_actual, menor_actual, promedio]
    print(lista_procesada)
    return lista_procesada

procesa_lista([2,3,3,5,7,10])
    
        
        
        
    