import matplotlib.pyplot as plt
import numpy as np

# Definimos los rangos de x para las rectas
x = np.linspace(-10, 10, 400)

# Definimos las funciones
y1 = x + 10
y2 = -x + 3

# Graficamos las rectas
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='y = x + 10')
plt.plot(x, y2, label='y = -x + 3')

# Graficamos el punto de intersección
plt.scatter(-3.5, 6.5, color='red', zorder=5)
plt.text(-3.5, 6.5, ' (-3.5, 6.5)', fontsize=12, verticalalignment='bottom')

# Configuramos la gráfica
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title('Intersección de las rectas y = x + 10 y y = -x + 3')
plt.xlabel('x')
plt.ylabel('y')

# Mostramos la gráfica
plt.show()
