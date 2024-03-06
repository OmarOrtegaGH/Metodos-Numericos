#!/usr/bin/env python
# coding: utf-8

# In[5]:


# main.py
from met_num import BisecciónV3, Newton_Raphson_V3, Puunto_Fijo_V3

def main():
    print("Escoge un método para resolver ecuaciones:")
    print("1. Bisección")
    print("2. Newton")
    print("3. Punto fijo")
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        # Llama a la función biseccion
        biseccion()
    elif opcion == 2:
        # Llama a la función newton
        newton()
    elif opcion == 3:
        # Llama a la función punto_fijo
        punto_fijo()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()


# In[ ]:




