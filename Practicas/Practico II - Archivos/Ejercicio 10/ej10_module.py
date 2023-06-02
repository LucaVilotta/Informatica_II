##### EJERCICIO 10 MÓDULO DE FUNCIONES ######

#### Funciones a utilizar

## Función para mostrar los productos disponibles:
def mostrar_productos():
    try:
        arch = open('productos.dat', 'r', encoding='utf-8')
        productos = []

        for linea in arch:
            if linea[-1] == '\n':
                linea = linea[:-1]
            
            # Dividir la línea en partes utilizando ';' como separador
            partes = linea.split(';')
            
            # Verificar si la línea tiene el formato correcto
            if len(partes) == 3:
                codigo = partes[0]
                nombre = partes[1]
                precio = partes[2]
                
                # Agregar el producto a la lista
                productos.append((codigo, nombre, precio))
        
        # Imprimir la lista de productos de forma ordenada
        for producto in productos:
            codigo, nombre, precio = producto
            print("Código: {:<10} | Nombre: {:<21} | Precio: {:>10}".format(codigo, nombre, precio))

        
        arch.close()
    except IOError:
        print("Error al abrir productos.dat")


## Funcion para verificar si existe el codigo ingresado
def existe_prod(codigo_in):
    try:
        arch = open('productos.dat', 'r', encoding='utf-8')
        # Dividir la línea en partes utilizando ';' como separador
        for linea in arch:
            partes = linea.split(';')
            codigo = partes[0]
            if codigo == codigo_in:
                existe = True
                print("El código EXISTE en el archivo productos.dat")
                return existe
        print("El código no existe en el archivo productos.dat")
        existe = False
        return existe
        arch.close()
    except IOError:
        print("Error al abrir el archivo productos.dat")


## Función para verificar la cantidad de stock del producto
def stock_disponible(codigo_in,stock_in):
    try:
        arch = open('stock.dat', 'r', encoding='utf-8')
        
        for linea in arch:
            if linea[-1] == '\n':
                linea = linea[:-1]
            # Dividir la línea en partes utilizando ';' como separador
            partes = linea.split(';')
            if len(partes) == 2:
                codigo = partes[0]
                stock = int(partes[1])        
            if codigo_in == codigo:
                disponible = stock > stock_in
                if disponible:
                    print("El stock alcanza para cubrir la venta")
                    return disponible
                else:
                    print("Stock insuficiente: hay %d unidades y se requieren %d para la venta"%(stock,stock_in))
                    return disponible
        arch.close()
    except IOError:
        print("Error al abrir stock.dat")


## Función para verificar la cantidad de stock del producto
def agregar_venta(codigo_producto,cantidad_vendida):
    try:
        arch = open('ventas.dat', 'a', encoding='utf-8')
        formato = codigo_producto.upper()+';'+str(cantidad_vendida)
        arch.write("%s\n"%(formato))
        print("Venta agregada con éxito")
        arch.close()
    except IOError:
        print("Error al abrir ventas.dat")


## Función para restar el stock vendido del archivo stock.dat
def restar_stock(codigo_in,cantidad_vendida):
    try:
        arch = open('stock.dat', 'r', encoding='utf-8')
        editado = []
        for linea in arch:
            if linea[-1] == '\n':
                linea = linea[:-1]
        # Dividir la línea en partes utilizando ';' como separador
            partes = linea.split(';')
            codigo = partes[0]
            stock = int(partes[1])
            if codigo == codigo_in:
                stock -= int(cantidad_vendida)
            linea_modif = "%s;%d\n"%(codigo,stock)
            editado.append(linea_modif)
        arch.close()
        arch_modif = open('stock.dat', 'w', encoding='utf-8')
        for elemento in editado:
            arch_modif.write("%s"%elemento)
        print("Stock actualizado")
        arch_modif.close()
    except IOError:
        print("Error al abrir stock.dat")


    

        
        
        


