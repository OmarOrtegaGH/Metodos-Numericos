#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Método de iteración de punto fijo, primera versión
import numpy as np
# Definimos una función cualquiera
def g(x):
    return np.sin(x) + x/2
# Definimos una función que contenga una aproximación inicial p0, una tolerancia TOL y un número máximo de iteraciones n0
def parámetros(p0, TOL, n0):
    i = 1 # Determinamos un contador para las iteraciones
    while i <= n0: # Mientras que el contador no llegue al número maximo de iteraciones permitidas definidas hará el proceso
        p = g(p0) # Determinamos p = g(p0). Calculamos (pi.) es decir, la aproximación actual de la raíz
        if abs(p-p0) < TOL: # Encontramos una solución lo suficientemente aceptable para la tolerancia dada
            print(f"La raíz es {p} (el procedimiento fue exitoso).") # imprimimos el resultado
            return
        i += 1 # Actualizamos el contador de iteraciones
        p0 = p # Actualizamos (p0) ya que ahora esa será nuestra solución
    print(f"El método falló después de {n0} iteraciones (El procedimiento no fue exitoso)")
# Definimos nuestros parámetros
p0 = 1.0  # Valor inicial
TOL = 1e-5  # Tolerancia
n0 = 1000  # Número máximo de iteraciones

parámetros(p0, TOL, n0) # llamamos a la función

