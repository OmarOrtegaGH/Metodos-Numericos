# Code
### Normalfit ###
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
    for k in range(n):
        A[:,k] = phi(n,k,dataxs)/datasigs
    bs = datays/datasigs
    cs = np.linalg.solve(A.T@A, A.T@bs)
    chisq = np.sum((bs - A@cs)**2)
    return cs, chisq

np.random.seed(45379)
dataxs = np.array([34,27,65,20,53,49,42,31,55,61])
datays = np.array([4.5,3,7,3.5,8,5,4,4,5.5,7.5])
datasigs = 0.5

for n in (2, 3):
    cs, chisq = normalfit(dataxs, datays, datasigs, n)
    print()
    print('El valor para \chi^2 es ', chisq)
    print('El valor para \chi^2 por grado de libertad es: ', chisq/(dataxs.size - cs.size))
    print('El valor de los parámetros c_i son ', cs)