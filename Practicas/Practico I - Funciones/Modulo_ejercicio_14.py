#### MÓDULO DE FUNCIONES PARA EL PROGRAMA DE MATRICES
### IMPORTS
from random import randint


## Función para corroborar si la matriz es cuadrada y, de serlo, corroborar si es simétrica
def es_simetrica(mat):
    # Verificar si la matriz es cuadrada
    if len(mat) != len(mat[0]):
        print("La matriz no es cuadrada")
        return False
    
    # Verificar si la matriz es simétrica
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            if mat[i][j] != mat[j][i]:
                print("La matriz es cuadrada pero no es simétrica")
                return False
    
    print("La matriz es simétrica")
    return True

## Función para corroborar si el número ingresado se encuentra en la matriz
def buscar_valor(mat, num):
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            if mat[i][j] == num:
                print("El número se encuentra en la matriz")
                return True
    print("No se encontró el numero en la matriz")
    return False

## Función para generar una matriz aleatorea
def matriz_aleatoria(fil, col):
    mat = []
    for i in range(fil):
        fila = []
        for j in range(col):
            fila.append(randint(0, 9))
        mat.append(fila)
    return mat

## Muestra el máximo valor de cada fila en un solo mensaje
def mostrar_max_fila(mat):
    for i in range(len(mat)):
        num2 = -1
        for j in range(len(mat[0])):
            num1 = mat[i][j]
            if num1>=num2:
                num2 = num1
        print("Máximo fila %d: %d"%(i+1,num2))
        
## Genera una matriz que tendrá tantas filas como valores mayores al valor ingresado fuero encontrados
def buscar_indices(mat, val):
    mat_indices = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] > val:
                mat_indices.append([i,j])
    print(mat_indices)
    return mat_indices
    

        
        






            