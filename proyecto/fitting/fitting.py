import numpy as np

def phi(n,k,x):
    if n==2:
        val = x**k
    elif n==3:
        val = x**k
    return val

def normalfit(dataxs,datays,datasigs,n):
    N = dataxs.size
    A = np.zeros((N,n))
    # Para cada columna, se calculan los valores de la función base phi(n,k,dataxs)
    #para todos los puntos de datos dataxs, y estos valores se dividen por los datasigs
    #correspondientes y se almacena el valor en las columnas
    for k in range(n):
        A[:,k] = phi(n,k,dataxs)/datasigs
    bs = datays/datasigs
    cs = np.linalg.solve(A.T@A, A.T@bs)
    chisq = np.sum((bs - A@cs)**2)
    return cs, chisq
