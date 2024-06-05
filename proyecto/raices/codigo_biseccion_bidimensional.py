import numpy as np

def biseccion_bidimensional():
    # Pedimos al usuario que introduzca sus funciones
    expr1 = input("Introduce tu primera función f(x, y): ")
    expr2 = input("Introduce tu segunda función g(x, y): ")

    # Convertimos las expresiones del usuario en funciones de numpy
    f = lambda x, y: eval(expr1)
    g = lambda x, y: eval(expr2)

    # Pedimos al usuario que introduzca los intervalos, la tolerancia y el número máximo de iteraciones
    a = float(input("Introduce el límite inferior del intervalo para x: "))
    b = float(input("Introduce el límite superior del intervalo para x: "))
    c = float(input("Introduce el límite inferior del intervalo para y: "))
    d = float(input("Introduce el límite superior del intervalo para y: "))
    tol = float(input("Introduce la tolerancia: "))
    n0 = int(input("Introduce el número máximo de iteraciones: "))

    i = 0
    while ((b-a)/2 >= tol or (d-c)/2 >= tol) and (i < n0): # comparamos la longitud de los intervalos con la tolerancia y verificamos que no se exceda el número máximo de iteraciones
        m = (a+b)/2 # encontramos el valor medio en x
        n = (c+d)/2 # encontramos el valor medio en y
        if f(m, n) == 0 and g(m, n) == 0: # si se encuentran ya las raices, el ciclo se detiene
            break
        elif np.sign(f(a, n)) != np.sign(f(m, n)): # verificamos los signos en x
            b = m
        else:
            a = m
        if np.sign(g(m, c)) != np.sign(g(m, n)): # verificamos los signos en y
            d = n
        else:
            c = n
        i += 1
    if i == n0:
        print("Se llegó al número máximo de iteraciones")
    else:
        print (f"Las raíces de las funciones son x = {m}, y = {n}")
    print (f"se hicieron {i} iteraciones")
