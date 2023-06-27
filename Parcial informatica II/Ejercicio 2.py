## Parcial informática II ejercicio 2:

def calcula_TR60(recinto, V):
    try:
        arch = open(recinto,'r',encoding='utf-8') #abro el archivo
        #Variables a utilizar:
        superficie_total = 0
        a_total = 0
        #Listas a utilizar:
        materiales = [] #lista vacía de materiales
        superficies = [] #lista vacía de superficies
        coef_absorcion =  [] #lista vacía coef de abs


        for linea in arch: #lo itero
            
            if linea[-1] == '\n':  # Verificar si el último carácter es un salto de línea
                linea = linea[:-1]  # Eliminar el último carácter (salto de línea)
    
            partes = linea.split(";") #Separo en partes la linea usando de separador el ";" y guardo cada parte en una variable
            
            material = partes[0]
            superficie = partes[1]
            coef = partes[2]
            
            ##Superficie:
            superficie_total += float(superficie)
            ##Absorción total sumatoria:
            a_total += float(coef)
            
            #Agrego cada variable a su respectiva lista:  
            materiales.append(material)
            superficies.append(superficie)
            coef_absorcion.append(coef)
            
        
        #### Cálculo del TR60
        ##Absorción promedio:
        a_total /= superficie_total
        TR60_sabine = (0.161*V)/(superficie_total*a_total)
        
        print("El TR de la sala dada es %d"%(TR60_sabine))
        
        arch.close() #cierro el archivo
    except IOError:
        print("Error al abrir algun archivo")
        
calcula_TR60("C:\\Users\\Computadora\\Desktop\\Informatica II\\Parcial informatica II\\Ejercicio 2 archivo.txt", 32)

## Si no se visualiza correctamente por el espaciado también lo subí a github: https://github.com/LucaVilotta/Informatica_II/tree/main/Parcial%20informatica%20II
            
            
        