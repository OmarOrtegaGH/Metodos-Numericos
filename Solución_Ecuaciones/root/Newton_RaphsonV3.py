#!/usr/bin/env python
# coding: utf-8

# In[4]:


# newton.py
import numpy as np
print("Método de Newton, para introducir funciones de numpy escribir primero np.")
def newton():
    # Pedimos al usuario que introduzca su función y su derivada
    expr = input("Introduce tu función: ")
    df_expr = input("Introduce la derivada de tu función: ")

    # Convertimos las expresiones del usuario en funciones de numpy
    # lambda x define una función anonima que toma x argumento,
    # y eval() evalúa el texto introducido por el usuario como una expresión de Python
    f = lambda x: eval(expr)
    df = lambda x: eval(df_expr)

    # Pedimos al usuario que introduzca el valor inicial, la tolerancia y el número máximo de iteraciones
    p0 = eval(input("Introduce el valor inicial p0: "))
    TOL = float(input("Introduce la tolerancia: "))
    N0 = int(input("Introduce el número máximo de iteraciones: "))

    i = 1 # Contador de iteraciones
    while (i <= N0):
        p = p0 - f(p0) / df(p0) # Aplicamos el método de Newton
        if abs(p - p0) < TOL: # Si la diferencia es menor que la tolerancia, hemos encontrado la raíz
            print(f"El procedimiento fue exitoso y la raíz obtenida es {p} después de {i} iteraciones")
            return
        i += 1 # Actualizamos el contador de iteraciones
        p0 = p # Actualizamos el valor de p0 para la siguiente iteración
    # Si llegamos a este punto, el método no encontró una raíz en el número máximo de iteraciones
    if i == N0:
        print("El algoritmo llegó al número máximo de iteraciones definido")


# In[ ]:




