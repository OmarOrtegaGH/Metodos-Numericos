import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Se define una función compute cs que calcula los coeficientes del spline cúbico
def computecs(dataxs,datays):
    # la variable n es el número de puntos de datos, acorde a los puntos en x establecidos
    n = dataxs.size
    
    # Se crea una matriz de dimensiones (n-2, n-2) inicializada en ceros. Esta será nuestra matriz triagonal
    A = np.zeros((n-2, n-2))
    # LLenamos las diagonales de la matriz triagonal, (central, superior e inferior)
    np.fill_diagonal(A, 2*(dataxs[2:]-dataxs[:-2]))
    np.fill_diagonal(A[1:,:], dataxs[2:-1]-dataxs[1:-2])
    np.fill_diagonal(A[:,1:], dataxs[2:-1]-dataxs[1:-2])
    
    # Se calculan las pendientes  de los segmentos de línea entre los puntos de datos consecutivos.
    b1 = (datays[2:]-datays[1:-1])/(dataxs[2:]-dataxs[1:-1])
    b2 = (datays[1:-1]-datays[:-2])/(dataxs[1:-1]-dataxs[:-2])
    # Por la segunda derivada, se multiplica por 6 para obtener el vector bs
    bs = 6*(b1 - b2)
    
    # Se inicializa un vector cs de longitud n en ceros
    cs = np.zeros(n)
    # Se resuelve el sistema de ecuaciones lineales A*cs = bs para obtener los coeficientes del spline cúbico.
    cs[1:-1] = np.linalg.solve(A, bs)
    return cs

# Interpolación spline cúbico
def splineinterp(dataxs,datays,cs,x):
    # Indice del primer valor de los datos en x mayor que x
    k = np.argmax(dataxs>x)
    # Se obtienen los valores de x, y y z en los indices correspondientes
    xk = dataxs[k]; xk1 = dataxs[k-1]
    yk = datays[k]; yk1 = datays[k-1]
    ck = cs[k]; ck1 = cs[k-1]
    
    # Se calcula el valor interpolado en x utilizando la fórmula del spline cúbico.
    val = yk1*(xk-x)/(xk-xk1) + yk*(x-xk1)/(xk-xk1)
    val -= ck1*((xk-x)*(xk-xk1) - (xk-x)**3/(xk-xk1))/6
    val -= ck*((x-xk1)*(xk-xk1) - (x-xk1)**3/(xk-xk1))/6
    return val

# Puntos
x = np.array([2, 3, 4, 5, 6])
y = np.array([2, 6, 5, 5, 6])

# Se calculan los coeficientes del spline cúbico
cs = computecs(x, y)

# Se interpola en un punto específico
x_val = 0.95
pofx = splineinterp(x, y, cs, x_val)
print(x_val, pofx)

# Resultados
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for i in range(len(x)-1):
    xi = np.linspace(x[i], x[i+1], 100)
    yi = [splineinterp(x, y, cs, x_val) for x_val in xi]
    plt.plot(xi, yi, colors[i % len(colors)])

# Graficar los puntos de datos originales
plt.plot(x, y, 'o', label='datos originales')
plt.legend()
plt.show()