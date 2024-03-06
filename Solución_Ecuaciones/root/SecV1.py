#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Método secante V1
import numpy as np
expr = input("Introduce tu función: ")
f = lambda x: eval(expr)
p0 = eval(input("Introduce el valor inicial p0: "))
p1 = eval(input("Introduce el valor inicial p1: "))
TOL = float(input("Introduce la tolerancia: "))
N0 = int(input("Introduce el número máximo de iteraciones: "))

def secv1(f,p0,p1,TOL,N0):
    i=2
    q0 = f(p0)
    q1 = f(p1)
    while i<=N0:
        p = p1-q1*(p1-p0)/(q1-q0)
        if abs(p-p1)<TOL:
            print(f"el procedimiento fue exitoso y la raiz es: {p}")
            break
        i+=1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    else:
        print("se alcanzó el número máximo de iteraciones")

# Llamada a la función
secv1(f, p0, p1, TOL, N0)


# In[ ]:




