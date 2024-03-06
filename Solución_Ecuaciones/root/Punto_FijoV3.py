#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np

# Pedimos al usuario la entrada de la función
expr = input("Introduce tu función: ")

# definimos una función y luego la convertimos en una expresión de python
g = lambda x: eval(expr)

p0 = eval(input("Introduce el valor inicial p0: "))
TOL = float(input("Introduce la tolerancia: "))
n0 = int(input("Introduce el número máximo de iteraciones: "))

def puntofijo(g,p0,TOL,n0):
    
    i = 1 # Determinamos un contador para las iteraciones
    while i <= n0: # Mientras que el contador no llegue al número maximo de iteraciones permitidas definidas hará el proceso
        p = g(p0) # Determinamos p = g(p0). Calculamos (pi.) es decir, la aproximación actual de la raíz
        if abs(p-p0) < TOL: # Encontramos una solución lo suficientemente aceptable para la tolerancia dada
            print(f"La raíz es {p} (el procedimiento fue exitoso).") # imprimimos el resultado
            break
        i += 1 # Actualizamos el contador de iteraciones
        p0 = p # Actualizamos (p0) ya que ahora esa será nuestra solución

if i > n0:
    print(f"El método falló después de {n0} iteraciones (El procedimiento no fue exitoso)")

print(f"después de {i} iteraciones:")
puntofijo(g,p0,TOL,n0)


# In[ ]:




