def mostrar_linea(nomArchivo,nLinea):
    ## Booleanos para el while y los condicionales
    #Booleano para saber si existe la linea ingresada
        existeLinea = False
    #Booleano para saber si existe la linea ingresada
        existeArchivo = False
    ##  While para que el ciclo se repita hasta que se ingrese una ruta válida y una línea válida
        while (not existeLinea) and (not existeArchivo):
            ##Try: 
            try:
                ## Abro el arhcivo
                arch = open(nomArchivo,'r',encoding='utf-8')
                #Contador para saber el número de linea
                contador = 1
                ## Iteración de las líneas
                for linea in arch:
                    if contador == nLinea:
                        print(linea)
                        # Booleano de existencia de la línea en true
                        existeLinea = True
                    contador+=1
                #Condción por si no existe la linea ingresada
                if not existeLinea:
                    print("La línea ingresada no existe en el archivo")
                ## Cierro el archivo
                arch.close()
                # Booleano de existencia del archivo en true
                existeArchivo = True
            except IOError:
                print("Error al abrir algun archivo")


## PROGRAMA PRINCIPAL
nomArchivo = input('Ingrese la ruta del archivo: ')
nLinea = int(input('Ingrese el número de línea: '))
mostrar_linea(nomArchivo,nLinea)
