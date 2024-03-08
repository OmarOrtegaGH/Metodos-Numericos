#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Método secante V1
import numpy as np
# Definimos una función para el método
def secv1():
    expr = input("Introduce tu función: ") # Expresión introducida por el usuario
    f = lambda x: eval(expr) # Convertimos la entrada del usuario en código del programa
    # Parámetros necesarios
    p0 = eval(input("Introduce el valor inicial p0: "))
    p1 = eval(input("Introduce el valor inicial p1: "))
    TOL = float(input("Introduce la tolerancia: "))
    N0 = int(input("Introduce el número máximo de iteraciones: "))

    i=2 # Iniciamos el contador de iteraciones
    q0 = f(p0)
    q1 = f(p1)
    while i<=N0: # mientras que las iteraciones no lleguen al límite definido, se hará el método
        p = p1-q1*(p1-p0)/(q1-q0)
        if abs(p-p1)<TOL:
            print(f"el procedimiento fue exitoso haciendo {i} iteraciones y la raiz es: {p}")
            break
        # Actualizamos las iteraciones y las variables    
        i+=1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    else:
        print("se alcanzó el número máximo de iteraciones")
        return p
secv1()    

