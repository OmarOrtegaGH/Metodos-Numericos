#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np

# Definimos la función a la que queremos encontrarle la raíz
def f(x):
    return np.cos(x)-x

# Definimos la derivada de dicha función
def df(x):
    return -np.sin(x)-1

# Definimos los parámetros que necesitamos para usar el método
def newton(p0, TOL, N0):
    i = 1 #inicializamos  un contador para las iteraciones
    while (i <= N0): #mientras el número de iteraciones no supere el máximo de iteraciones definido, hará el siguiente proceso
        p = p0 - f(p0) / df(p0) #Aplicamos el método de newton
        if abs(p - p0) < TOL: # Si la diferencia es menor que la tolerancia, encontramos una raíz
            print(f"El procedimiento fue exitoso y la raíz obtenida es {p}")
            return
        i += 1 # actualizamos el contador con cada iteración
        p0 = p # actualizamos p0 para cada iteración
    if i == N0: # si las iteraciones llegan al máximo definido entonces:
        print("El algoritmo llegó al número máximo de iteraciones definido")
# Llamamos a nuestra función
newton(np.pi/4, 0.0001, 100)


# In[ ]:




