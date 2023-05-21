def mostrar(nomArchivo):
    ##Try: 
    try:
        ## Abro el arhcivo
        arch = open(nomArchivo,'r',encoding='utf-8')
        ## Lo itero para mostrar su contenido por pantalla
        for linea in arch:
            print(linea)
        ## Cierro el archivo
        arch.close()
    except IOError:
        print("Error al abrir algun archivo")


## PROGRAMA PRINCIPAL
nomArchivo = input('Ingrese la ruta del archivo: ')
mostrar(nomArchivo)
