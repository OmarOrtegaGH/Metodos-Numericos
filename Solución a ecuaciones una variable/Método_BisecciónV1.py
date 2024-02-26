#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Esta es la primera versión del código, es el algoritmo lógico con las correcciones hechas
# Definimos la función
def f(x):
    return x**3 - x**2 - 1

# Definimos una función para el método de bisección
def biseccion(a, b, tol, n0):
    # Verificamos que la función cambie de signo, este método lo requiere
    if f(a) * f(b) > 0:
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

# Llamamos a la función bisección con los intervalos, la tolerancia y el número máximo de iteraciones
biseccion(-2, 2, 0.01, 1000)



# In[ ]:




