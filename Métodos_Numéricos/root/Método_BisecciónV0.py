#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Esta es la primera versión del código de bisección, la que fue mostrada en clase
import numpy as np

# Definimos la función
f = np.vectorize(lambda x: x**3 - x**2 - 1) #x^3-x^2-1

# Definimos el intervalo y la toleracia o error
a = -2
b = 2
tol = 0.01

# Verificamos que la función cambie de signo, este método lo requiere
if f(a) * f(b) > 0:
    print("No es posible realizar este método con los datos dados")

# Método de bisección
i = 0
while ((b-a)/2 >= tol): # comparamos la longitud de los intervalos con la tolerancia
    m= (a+b)/2 # encontramos el valor medio
    if f(m) == 0: # si se encuentra ya la raiz, el ciclo se detiene
        break
    if f(m)*f(a) < 0: # verificamos los signos
        b = m
    else:
        a = m
    i += 1
print (f"La raíz de la función es {m}")
print (f"se hicieron {i} iteraciones")


# In[ ]:




