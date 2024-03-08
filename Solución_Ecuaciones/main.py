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
    print ("4. Secante Versión 1")
    print ("5. Secante Versión 2")
    opción = int(input("opción: "))

    if opción == 1:
        BisecciónV3.biseccion()
    elif opción == 2:
        Newton_RaphsonV3.newton()
    elif opción == 3:
        Punto_FijoV3.puntofijo()
    elif opción == 4:
        SecV1.secv1()
    elif opción == 5:
        SecV2.secv2()

main()


