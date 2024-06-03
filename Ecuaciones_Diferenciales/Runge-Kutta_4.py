# Método Runge-Kutta de cuarto orden (RK4)
import numpy as np
def rk4(f, a, b, n, y0):
    h = (b-a)/(n-1)
    x = np.linspace(a, b, n)
    y = np.zeros(n)
    y[0] = y0

    for i in range(n-1):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h/2, y[i] + k1/2)
        k3 = h * f(x[i] + h/2, y[i] + k2/2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6

    return x, y

xs, ys = rk4(f, a, b, n, y0)