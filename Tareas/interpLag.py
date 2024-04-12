#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# Definimos una función legendre que tiene como argumentos los datos en x y un valor de x cualquiera
def legendre(dataxs, x):
    # n guarda un número de puntos del tamaño de los datos en x que tengamos
    n = dataxs.size
    # l es un arreglo de unos, donde se guardarán los coeficientes de legendre y tiene el mismo tamaño que el número de puntos
    l = np.ones(n)
    # Ciclos for para la fórmula de los coeficientes de legendre
    for k in range(n):
        for j in range(n):
            # Condición, si j es igual a k, se lo salta
            if j == k:
                continue
            # Fórmula
            l[k] *= ((x - dataxs[j]) / (dataxs[k] - dataxs[j]))
    return l

# Se calcula el valor de la interpolación en un punto x
def general(dataxs, datays, l, x):
    # k será un arreglo con x en dataxs, 0 arreglo vacio
    # np.where devuelve un array con los índices de los elementos en dataxs que son iguales a x. Si x no está en dataxs,
    # np.where devuelve un array vacío.
    k = np.where(x == dataxs)[0]
    # Si x no está en dataxs entonces se calcula el valor del polinomio como el producto de datays por l
    if k.size == 0:
        val = np.sum(datays * l)
    # Si x está en dataxs entonces val es el valor correspondiente de datays
    else:
        val = datays[k[0]]
    return val

# Definimos una función
func = lambda x: 1/(1+25*x**2)

# Una función con los datos que necesitemos
def generatedata(n, f):
    # un arreglo de n puntos de -1 a 1
    dataxs = np.linspace(-1,1,n) 
    # y es igual a la función evaluada en los puntos en x
    datays = f(dataxs)
    
    return dataxs, datays

# Definimos 15 puntos y se evalua la función en los puntos
dataxs, datays = generatedata(30, func)
# Definimos x en 0.3
x = 0.3
#  calculamos los coeficientes de Lagrange para los puntos generados y el valor x.
l = legendre(dataxs, x)
# calculamos el valor de la interpolación de Lagrange en x.
pofx = general(dataxs, datays, l, x)
# Imprime el valor de x, el valor de la interpolación y la función en x
print(x, pofx, func(x))


# In[ ]:




