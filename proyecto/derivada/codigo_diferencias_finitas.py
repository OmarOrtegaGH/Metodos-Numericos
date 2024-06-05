import numpy as np
import matplotlib.pyplot as plt

# Derivada hacia adelante
def calc_fd(f,x,h):
    fd = (f(x+h) - f(x))/h
    return fd

# Derivada central
def calc_cd(f,x,h):
    cd = (f(x+h/2) - f(x-h/2))/h
    return cd

def diferencias_finitas(f, fprime, x, h):
    an = fprime(x) # Para la solución analítica evaluamos la expresión de la derivada en el valor de x
    fd = calc_fd(f,x,h) # Calculamos el valor de la derivada hacia adelante para cada valor de h en hs
    cd = calc_cd(f,x,h) # Calculamos el valor de la derivada central para cada valor de h en hs

    # Calculamos los errores absolutos para cada método
    fd_error = abs(fd - an)
    cd_error = abs(cd - an)

    return an, fd, fd_error, cd, cd_error
