## PARA INSTALAR LA LIBRERÍA matplotlib DEBEN IR A HERRAMIENTAS->Manage packages... Y EN LA BARRA DE
## BÚSQUEDA COLOCAR EL NOMBRE DE LA LIBRERÍA Y PRESIONAR ENTER. LUEGO, PRESIONAR EL BOTÓN INSTALAR.

import matplotlib.pyplot as plt

x = range(50)
y = []
for val in x:
    y.append(val**3-val)

plt.plot(x,y)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Grafico ejemplo')
plt.show()
