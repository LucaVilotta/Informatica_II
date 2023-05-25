def wc(nomArch,opcion):
    ##Try: 
    try:
        ## Abro el arhcivo
        arch = open(nomArchivo,'r',encoding='utf-8')
        #Contador para saber el número de linea
        contador_l = 0
        #Contador para saber el número de caracteres
        contador_c = 0
        #Variables op 3:
        palabrasList = []
        palabrasString = ''
        ## Op1
        #Iterar lineas y sumar al contador
        for linea in arch:
            #Contador op 1:
            contador_l+=1
            
            
        ##Op2
            for c in linea:
                if c!=" " and c!="\n":
                    contador_c+=1
        ##Op3 
                    palabrasString += c
                else:
                    palabrasList.append(palabrasString)
                    palabrasString = ''
        # Si hay palabras después del último espacio o salto de línea en el archivo
        if palabrasString != '':
            palabrasList.append(palabrasString)
        #Variable que almacena la cantidad de palabras del archivo
        cantidad_p = len(palabrasList)
        ##Op4
        #Lista con las variables con la info requerida en cada opcion
        lista_info = [contador_l,contador_c,cantidad_p]
            
        ##Prints segun la Op:
        if opcion=="1":
            print(contador_l)
        elif opcion =="c":
            print(contador_c)
        elif opcion=="w":
            print(cantidad_p)
        elif opcion =='':
            print(lista_info)
        ## Cierro el archivo
        arch.close()
    except IOError:
        print("Error al abrir algun archivo")
## PROGRAMA PRINCIPAL
nomArchivo = input('Ingrese la ruta del archivo: ')
opcion = input('Ingrese la opción: ')
wc(nomArchivo,opcion)
