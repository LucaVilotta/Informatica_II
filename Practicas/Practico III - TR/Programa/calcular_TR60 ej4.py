from reverberacion import *
#Programa para cálculo de tiempo de reverberación (considera aberturas)

print("Cálculo de tiempo de reverberación (TR60) en sala\n")

# variables a sumar:

S = 0.0 # superficie total
a_total = 0.0 # absorción total
a_total_list = [0,0,0,0,0,0] # absorción total lista
contador = 0 # contador

# Frecuecia


# Mostramos los materiales

mostrar_materiales()

while True:
    
    # ingresamos cada superficie sin distinción (techo, pared, piso)
    
    sup = float(input("Ingrese superficie [m2]: "))
    material = int(input("Ingrese el código del material: "))
    
    
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
            a_total += sup_aber*abs_aber
            
            op_aber = input("Desea ingresar otra abertura a esa superficie? (s/n): ")
            
            if op_aber.lower() == "n":
                break
    #For para calcular el a y el a_total dependiendo de la frecuecia y almacenarlos en una lista
    for frecuencia in frecuencias:
        a   = mostrar_coeficiente(material,frecuencia)
        a_total += sup*a # sumamos el producto (a_i*S_i) al total
        a_total_list[contador] += a_total
        contador += 1
    contador = 0
    S += sup # sumamos la superficie al total
    
    op = input("Desea ingresar otra superficie? (s/n) ")
    
    if op.lower() == "n":
        break
    
# calculo final de a_total:
for a_final in a_total_list:
    a_total_list[contador] /= S
    contador += 1
contador = 0

# con este algoritmo no podemos calcular el volumen automáticamente:
V = float(input("Ingrese volumen total de la sala [m3]: "))

# mostrar resultados:
print("Volumen = %.2f[m3]"%(V))
print("Superficie = %.2f[m2]"%(S))
for c in range(len(frecuencias)):
    print("La absorción total para la frecuencia de %f es = %.2f"%(frecuencias[c], a_total_list[c]))
# TR dependiendo de a_total
# ACÁ EL A TOTAL LO TENG QUE ITERAR DE LA LISTA PARA VER SI ->!CADA UNO!<- ES MAYOR O MENOR AL VALOR 0.3
if a_total < 0.3:
    for a_promedio in a_total_list:
        TR60 = TR_sabine(V,S,a_promedio)
        print("El TR60 para la frecuencia de %f es = %.4f[s]"%(frecuencias[contador],TR60))
        contador +=1
elif a_total > 0.3:
    contador = 0
    for a_promedio in a_total_list:
        TR60 = TR_sabine(V,S,a_promedio)
        print("El TR60 para la frecuencia de %f es = %.4f[s]"%(frecuencias[contador],TR60))
        contador +=1


