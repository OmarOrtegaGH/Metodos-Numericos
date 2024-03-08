#!/usr/bin/env python
# coding: utf-8

# In[5]:


# main.py
from modulos import BisecciónV3, Newton_RaphsonV3, Punto_FijoV3
import numpy as np
def main():
    print("Escoge un método para resolver ecuaciones")
    print ("1. Bisección")
    print ("2. Newton Raphson")
    print ("3. Punto fijo")
    opción = int(input("opción: "))

    if opción == 1:
        BisecciónV3.biseccion()
    elif opción == 2:
        Newton_RaphsonV3.newton()
    elif opción == 3:
        Punto_FijoV3.puntofijo()    

main()


