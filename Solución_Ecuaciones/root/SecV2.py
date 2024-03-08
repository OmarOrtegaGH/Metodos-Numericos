#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np

# Método de secante v2
def secv2():
# Pedimos al usuario que introduzca su función
    expr = input("Introduce tu función: ")

# Convertimos la expresión del usuario en una función de numpy
    f = lambda x: eval(expr)

# Pedimos al usuario que introduzca los intervalos, la tolerancia y el número máximo de iteraciones
    a = float(input("Introduce el límite inferior del intervalo: "))
    b = float(input("Introduce el límite superior del intervalo: "))
    tol = float(input("Introduce la tolerancia: "))
    n0 = int(input("Introduce el número máximo de iteraciones: "))

    # Verificamos que la función cambie de signo, este método lo requiere
    if f(a) * f(b) > 0.0:
        print("No es posible realizar este método con los datos dados")
        return

    # Método de secante versión 2
    i = 2
    if f(a) > 0:
        p0 = b
        q0 = f(a)
        q1 = f(b)
    elif f(a) < 0:
        p0 = a
        q0 = b
        q1 = f(a)
    while ((b-a)/2 >= tol) and (i < n0): # comparamos la longitud de los intervalos con la tolerancia y verificamos que no se exceda el número máximo de iteraciones
        if f(a) > 0:
            p = p0-(q1/(q1-q0))*(q0-a)
        elif f(a) < 0:
            p = p0 - (q1/(q0-q1))*(b-p0)
        if abs(p-p0) < tol:
            print(f"procedimiento completado satisfactoriamente después de {i} iteraciones, la raíz es {p}")
            return
        i += 1
        p0 = p
        q1 = f(p)
    if i == n0:
        print("Se llegó al número máximo de iteraciones")    
    print (f"se hicieron {i} iteraciones")

# In[ ]:




