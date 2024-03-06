#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

# Método de Bisección
# Pedimos al usuario que introduzca su función
expr = input("Introduce tu función: ")

# Convertimos la expresión del usuario en una función de numpy
f = lambda x: eval(expr)

# Pedimos al usuario que introduzca los intervalos, la tolerancia y el número máximo de iteraciones
a = float(input("Introduce el límite inferior del intervalo: "))
b = float(input("Introduce el límite superior del intervalo: "))
tol = float(input("Introduce la tolerancia: "))
n0 = int(input("Introduce el número máximo de iteraciones: "))

def biseccion(f,a, b, tol, n0):
    # Verificamos que la función cambie de signo, este método lo requiere
    if f(a) * f(b) > 0.0:
        print("No es posible realizar este método con los datos dados")
        return

    # Método de bisección
    i = 0
    while ((b-a)/2 >= tol) and (i < n0): # comparamos la longitud de los intervalos con la tolerancia y verificamos que no se exceda el número máximo de iteraciones
        m= (a+b)/2 # encontramos el valor medio
        if f(m) == 0: # si se encuentra ya la raiz, el ciclo se detiene
            break
        elif f(m)*f(a) < 0: # verificamos los signos
            b = m
        else:
            a = m
        i += 1
    if i == n0:
        print("Se llegó al número máximo de iteraciones")
    else:
        print (f"La raíz de la función es {m}")
    print (f"se hicieron {i} iteraciones")

# Llamamos a la función bisección con los valores proporcionados por el usuario
biseccion(f,a, b, tol, n0)


# In[ ]:




