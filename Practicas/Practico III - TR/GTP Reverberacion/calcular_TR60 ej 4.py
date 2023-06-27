from reverberacion import *
#Programa para cálculo de tiempo de reverberación (considera aberturas)

print("Cálculo de tiempo de reverberación (TR60) en sala\n")

# variables a sumar:

S = 0.0 # superficie total
a_total = 0.0 # absorción total
matriz_a = [[]]
lista_a_total = [0,0,0,0,0,0] # lista inicializada con la cantidad de frecuencias disponibles
lista_TR = [] # lista de TR por frecuencia
contador_material = 0
contador_frecuencias = 0 
# Mostramos los materiales

mostrar_materiales()

while True:
    
    # ingresamos cada superficie sin distinción (techo, pared, piso)
    # junto a su coeficiente de absorción
    
    sup = float(input("Ingrese superficie [m2]: "))
    material = int(input("Ingrese el código del material: "))
    
    #For para iterar las frecuencias y guardarlo en una matriz donde las filas son cada material nuevo ingresado y...
    #...las columnas el coef de abs por frecuencia de ese material
    for frecuencia in frecuencias: 
        a   = mostrar_coeficiente(material,frecuencia)
        matriz_a[contador_material].append(a)
        
    
    tiene_abertura = input("Posee la superficie aberturas? (s/n): ")
    
    if tiene_abertura == "s":
        while True:
            sup_aber = float(input("Ingrese superficie de abertura [m2]: "))
            
            while sup - sup_aber < 0: 
            # si la superficie de la abertura es más grande que la pared...
                print("La superficie de la abertura no puede ser mayor que la de la pared")
                sup_aber = float(input("Reingrese superficie de abertura [m2]: "))
            
            abs_aber = float(input("Ingrese coeficiente de abertura [m2]: "))
            
            sup -= sup_aber #a la superficie le resto la abertura
            
            for cab in range(len(frecuencias)): 
                lista_a_total[cab] += sup_aber*abs_aber
            
            op_aber = input("Desea ingresar otra abertura a esa superficie? (s/n): ")
            
            if op_aber.lower() == "n":
                break
    
    # Nuevamente itero las frecuencias para obtener el coef de abs de ese material y guardo un a_total por frecuencia en la lista_a_total
    for c in range(len(frecuencias)): 
        lista_a_total[c] += sup*matriz_a[contador_material][c] # sumamos el producto (a_i*S_i) al total
    S += sup # sumamos la superficie al total
    
    op = input("Desea ingresar otra superficie? (s/n) ")
    
    if op.lower() == "n":
        break
    
    contador_material += 1 #incrementamos el contador para iterar la matriz_a
    matriz_a.append([])
    
# calculo final de a_total:
for c2 in range(len(frecuencias)): 
    lista_a_total[c2] /= S

# con este algoritmo no podemos calcular el volumen automáticamente:
V = float(input("Ingrese volumen total de la sala [m3]: "))

# TR dependiendo de cada a_total
for c3 in range(len(frecuencias)):
    if lista_a_total[c3] < 0.3:
        TR60 = TR_sabine(V,S,lista_a_total[c3])
    elif lista_a_total[c3] > 0.3:
        TR60 = TR_sabine(V,S,lista_a_total[c3])
    lista_TR.append(TR60) # lo agrego a una lista de TR
        

# mostrar resultados:
print("Volumen = %.2f[m3]"%(V))
print("Superficie = %.2f[m2]"%(S))


print("TR60 por frecuencia = ",  end="")
print(lista_TR)
