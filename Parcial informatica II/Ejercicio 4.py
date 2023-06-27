## Parcial informática II ejercicio 4:
def potencia(nomArchivo):
    try:
        arch = open(nomArchivo,'r',encoding='utf-8') #abro el archivo
        N = 0 #contador para la cantidad de "muestras" de la señal
        sumatoria_amplitudes = 0
        for linea in arch:
            if linea[-1] == '\n':  # Verificar si el último carácter es un salto de línea
                linea = linea[:-1]  # Eliminar el último carácter (salto de línea)
            sumatoria_amplitudes += float(linea)
            N += 1
        potencia = (1/(N*2))*((sumatoria_amplitudes)**2)
        print(potencia)
        return potencia
        arch.close() #cierro el archivo
    except IOError:
        print("Error al abrir algun archivo")
        
potencia("C:\\Users\\Computadora\\Desktop\\Informatica II\\Parcial informatica II\\Ejercicio 4 archivo.txt")
    