import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def f(x):
    # Aquí va la función
    pass

# Definimos una función euler que toma como argumentos:
def euler(f,a,b,n,y0): # Función, intervalo a,b donde se resuelve la ecuación, número de puntos y el valor de y0
    h = (b-a)/(n-1) # Se calcula el tamaño del paso h que se utilizará en el método
    xi = np.linspace(a,b,n) # generamos un array xi de n números igualmente espaciados entre a y b.
    yval = np.zeros(n) # Iniciamos un array en ceros para almacenar los valores de la solución en cada punto
    y = y0 # inicializamos y en y0
    for j,x in enumerate(xi): # ciclo que recorre j en cada valor de x en xi
        yval[j] = y # almacenamos el valor actual de y en un array de valores de y
        y = y + h*f(x, y) # Calculamos y actualizamos cada valor de y utilizando la fórmula
    return xi, yval # return los arreglos con los valores de x y los valores solución y

def run_euler():
    xi, yval = euler(f,a,b,n,y0) # Llamada de la función
