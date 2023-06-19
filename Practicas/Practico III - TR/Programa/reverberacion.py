# modulo: reverberacion.py

import math

# frecuencias disponibles en Hertz
frecuencias = [125, 250, 500, 1000, 2000, 4000]

# función para cargar coeficientes de un archivo de texto en una matríz
def cargar_coeficientes(nomArchivo):    
    try:        
        coefs = []
        arch = open(nomArchivo,"r")
                       
        for linea in arch:
            
            linea = linea.rstrip()
            
            lista = linea.split(";")
            
            #nomMaterial;c125Hz;c250Hz;c500Hz;c1kHz;c2kHz;c4kHz
            nomMaterial = lista[0]
            c125Hz = float(lista[1])
            c250Hz = float(lista[2])
            c500Hz = float(lista[3])
            c1kHz = float(lista[4])
            c2kHz = float(lista[5])
            c4kHz = float(lista[6])
            #nomMaterial;c125Hz;c250Hz;c500Hz;c1kHz;c2kHz;c4kHz
            coefs.append([nomMaterial,c125Hz,c250Hz,c500Hz,c1kHz,c2kHz,c4kHz])
            
        arch.close()
            
        return coefs
    
    except IOError:
        print("Error al abrir el archivo %s"%(nomArchivo))
        return None
        
        
# función para mostrar el listado de materiales disponibles
def mostrar_materiales():
    
    coefs = cargar_coeficientes("bd_materiales.txt")
    
    if coefs != None:
        
                
        print("Cod - Materiales")
        print("__________")
        
        for cod in range(len(coefs)):
            
            print("%3d - %s"%(cod+1,coefs[cod][0]))
            
            
# funcion para agregar un nuevo material y sus coeficientes a la base de datos (archivo)
def agregar_material():
    
    print("Ingresar material y coeficientes de absorción")
    nomMaterial = input("Nombre material: ")
    lista_coefs = []
    
    # recorro las posibles frecuencias
    for frec in frecuencias:
        
        coef = input("Coeficiente %d[Hz]: "%frec)
        # agrego a lista de coeficientes por frecuencia
        lista_coefs.append(coef)
    
    # creo la cadena separada por ; para agregar al archivo
    cadena_coefs=";".join(lista_coefs)
    
    try:
        
        arch = open("bd_materiales.txt","a")
        arch.write("%s;%s\n"%(nomMaterial,cadena_coefs))
        arch.close()
    except IOError:
        print("Error al abrir el archivo %s"%("bd_materiales.txt"))
        
   
# funcion para obtener determinado coeficiente de acuerdo a código de material y frecuencia
def mostrar_coeficiente(codigo,frecuencia):
    
    # siempre cargar los coeficientes del archivo:
    coefs = cargar_coeficientes("bd_materiales.txt")
    
    if coefs != None:
        
        # si la frecuencia buscada no se encuentra entre
        # las frecuencias disponibles
        if frecuencia not in frecuencias:
            
            print("Frecuencia %d no permitida"%(frecuencia))
            return
        
        # si la frecuencia está entre las permitidas
        # se busca hasta encontrarla
        for i in range(len(frecuencias)):
            if frecuencia == frecuencias[i]:
                columna = i
                break
        
        fila = codigo - 1    # la fila correspondiente al material esta en base 0
        columna = columna +1 # a la columna hay que sumarle 1 porque la primera
                             # es el nombre del material
        
        if fila >= len(coefs):
            print("No existe material con Código %d"%(codigo))
            return
        
        # si todo esta bien, devolvemos la posición de la matríz:
        return coefs[fila][columna]


##### GTP REVERBERACIÓN #####
#TR SABINE
def TR_sabine(V,S,a_total):
    TR60_sabine = (0.161*V)/(S*a_total)
    return TR60_sabine
#TR Eyring-Norris
def TR_eyring_norris(V,S,a_total):
    TR60_eyring_norris = (0.161*V)/(-S*(math.log10(1-a_total)))
    return TR60_eyring_norris



        



