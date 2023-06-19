from reverberacion import *
#Programa para cálculo de tiempo de reverberación (considera aberturas)

print("Cálculo de tiempo de reverberación (TR60) en sala\n")

# variables a sumar:

S = 0.0 # superficie total
a_total = 0.0 # absorción total

# Frecuecia
frecuencia = int(input("Ingrese la frecuencia emitida en hz: "))

# Mostramos los materiales

mostrar_materiales()

while True:
    
    # ingresamos cada superficie sin distinción (techo, pared, piso)
    # junto a su coeficiente de absorción
    
    sup = float(input("Ingrese superficie [m2]: "))
    material = int(input("Ingrese el código del material: "))
    a   = mostrar_coeficiente(material,frecuencia)
    
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
    
    a_total += sup*a # sumamos el producto (a_i*S_i) al total
    S += sup # sumamos la superficie al total
    
    op = input("Desea ingresar otra superficie? (s/n) ")
    
    if op.lower() == "n":
        break
    
# calculo final de a_total:
a_total /= S

# con este algoritmo no podemos calcular el volumen automáticamente:
V = float(input("Ingrese volumen total de la sala [m3]: "))

# TR dependiendo de a_total
if a_total < 0.3:
    TR60 = TR_sabine(V,S,a_total)
elif a_total > 0.3:
    TR60 = TR_sabine(V,S,a_total)

# mostrar resultados:
print("Volumen = %.2f[m3]"%(V))
print("Superficie = %.2f[m2]"%(S))
print("Absorción total = %.2f"%(a_total))
print("TR60 = %.4f[s]"%(TR60))