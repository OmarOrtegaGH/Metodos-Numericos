import numpy as np

def f(x):
    # Aquí va la función
    pass
# Utilizamos el método de bisección para encontrar la raíz de la ecuación implícita (y(i+1) - y(i) - h*f(x(i+1), y(i+1)) = 0)
def biseccion(f, a, b, x, y, h, tol=1e-6): # función, intervalo a,b donde se busca la raiz, valor de x donde se evalua, valor anterior de y, tolerancia
    c = a # Inicializamos el valor medio en a
    while ((b-a) >= tol): # Aseguramos la tolerancia definida
        c = (a+b)/2  # Método de bisección, se actualiza el valor de c
        if (c - y - h*f(x, c) == 0.0): # Verificamos si se ha encontrado una raíz de la ecuación
            break # Si es asi, se rompe el bucle
        elif ((c - y - h*f(x, c))*(a - y - h*f(x, a)) < 0): # Cambio de signos
            b = c # Se actualiza el valor a b
        else:
            a = c # El valor se actualiza a a
    return c # Return raiz encontrada

def euler_atras(f, a, b, n, y0): # función para el método
    h = (b-a)/(n-1) # tamaño del peso
    x = np.linspace(a, b, n) # x será un arreglo de n números equi espaciados entre a y b
    y = np.zeros(n) # y será un arreglo de ceros donde se irán almacenando los resultados
    y[0] = y0 # iniciamos en y0

    for i in range(n-1): # se ejecuta un ciclo n-1 veces porque este método ocupa el valor de y(i+1) para calcular y(i)
        # Se calcula el valor de la y siguiente
        # La función bisección recibe como entrada la función, el valor de y actual, el valor de y en el paso siguiente, el valor de x siguiente
        # el ahora valor actual de y y el tamaño del paso
        y[i+1] = biseccion(f, y[i], y[i] + h*f(x[i], y[i]), x[i+1], y[i], h)

    return x, y # return, los arreglos que contienen los valores  de x y y

def run_euler_atras():
    x, y = euler_atras(f, a, b, n, y0) # llamada de la función
