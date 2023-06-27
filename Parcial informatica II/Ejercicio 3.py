## Parcial informática II ejercicio 3:
def ordenados(lista):
    for i in range(len(lista) - 1): #Itero la lista menos el ultimo elemento
        if lista[i] > lista[i + 1]: #Comparo cada elemento actual de la iteración con el siguiente, si el siguiente es mayor retorno falso
            return False
    return True

## Si no se visualiza correctamente por el espaciado también lo subí a github: https://github.com/LucaVilotta/Informatica_II/tree/main/Parcial%20informatica%20II
