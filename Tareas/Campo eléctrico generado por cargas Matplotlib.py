#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import matplotlib.pyplot as plt

# Definimos las cargas con su posición y magnitud en coulombs [((qx, qy), q)...]
cargas_eléctricas = [((0, 0), 5), ((0, 1), -5), ((1, 0), 5), ((1, 1), -5)]

# Generamos una malla de datos, es decir nuestro espacio como una cuadrícula de puntos

# Dimensión y coordenadas x de cada punto
x = np.linspace(-10, 10, 100)
# Dimensión y coordenadas y de cada punto
y = np.linspace(-10, 10, 100)
# La función np.meshgrid es para generar la malla de datos
# X y Y serán arrays que representan las coordenadas x y y de cada punto en la cuadrícula
X, Y = np.meshgrid(x, y)

# Iniciamos los campos elétricos en cero para realizar y empezar ahi las sumas de los campos eléctricos
# Usamos la función np.zeros_like porque necesitamos que los arrays Ex y Ey sean de la misma dimensión que X, Y
Ex = np.zeros_like (X)
Ey = np.zeros_like (Y)

# Definimos la constante k, constante de Coulomb que relaciona variables eléctricas
k = 8.99e9

# Calculamos el campo electrico en cada carga eléctrica y sumamos

# Hacemos un ciclo for que recorre para cada carga de la lista, su posición y magnitud y hace las siguientes operaciones
for (qx, qy), q in cargas_eléctricas:
# Calculamos las componentes x y y del vector distancia desde la carga a cada punto en la cuadrícula.
# Restamos X, qx y Y, qy para obtener las coordenadas del vector distancia
    rx = X - qx
    ry = Y - qy
# Calculamos la magnitud de dicho vector como se calcula la magnitud de cualquier vector
    rm= np.sqrt(rx**2 + ry**2)
# Aplicamos la fórmula para E siendo el campo eléctrico
    Ex += k * q * rx / rm**3
    Ey += k * q * ry / rm**3

# Graficamos el campo eléctrico

# creamos un marco y sus ejes
fig, ax = plt.subplots(figsize=(10, 10))
# ponemos un titulo en el eje x
ax.set_title('Campo Eléctrico')
# graficamos usando streamplot que crea un gráfico de líneas de corriente que representan un campo vectorial.
plt.streamplot(X, Y, Ex, Ey, color='b', linewidth=0.5, density=1.5)


# In[ ]:




