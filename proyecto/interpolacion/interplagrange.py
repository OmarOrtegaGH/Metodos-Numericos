import numpy as np 
# Función para calcular los polinomios base de Lagrange
def legendre(dataxs, x):
    n = dataxs.size  # Obtenemos el número de puntos de datos
    l = np.ones(n)  # Inicializamos un vector de unos del tamaño de los puntos de datos
    # Iteramos sobre cada punto de datos
    for k in range(n):
        # Iteramos nuevamente sobre los puntos de datos
        for j in range(n):
            if j == k:  # Si los índices son iguales, saltamos la iteración
                continue
            # Calculamos el polinomio base de Lagrange para el punto k
            l[k] *= ((x - dataxs[j]) / (dataxs[k] - dataxs[j]))
    return l  # Devolvemos los polinomios base de Lagrange

# Función para calcular el valor interpolado
def general(dataxs, datays, l, x):
    # Buscamos si x está en los puntos de datos originales
    k = np.where(x == dataxs)[0]
    if k.size == 0:  # Si x no está en los puntos de datos originales
        val = np.sum(datays * l)  # Calculamos el valor interpolado
    else:  # Si x está en los puntos de datos originales
        val = datays[k[0]]  # El valor interpolado es el valor correspondiente de y
    return val  # Devolvemos el valor interpolado

# Función para realizar la interpolación
def interpolate(func, dataxs):
    datays = func(dataxs)  # Calculamos los valores de y para los puntos de datos
    # Calculamos los polinomios base de Lagrange para todos los puntos de datos
    l_values = [legendre(dataxs, x) for x in dataxs]
    # Calculamos los valores interpolados para todos los puntos de datos
    pofx_values = [general(dataxs, datays, l, x) for l, x in zip(l_values, dataxs)]
    return pofx_values  # Devolvemos los valores interpolados

