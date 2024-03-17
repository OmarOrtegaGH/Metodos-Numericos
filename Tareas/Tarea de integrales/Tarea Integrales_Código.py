#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad, tplquad
# Tarea de integrales, ejercicio 1.a

# Las siguientes lineas de código son tomadas del ejemplo proporcionado
f1 = lambda x: x-1
f2_1 = lambda x: np.sqrt(2*x+6)
f2_2 = lambda x: -np.sqrt(2*x+6)

r = np.linspace(-4, 6, 2000)
r2 = np.linspace(-1, 5, 2000)
r3 = np.linspace(-3, -1, 2000)

plt.plot(r, f1(r), color ='blue')
plt.plot(r, f2_1(r), color ='black')
plt.plot(r, f2_2(r), color ='black')

plt.fill_between(r2, f2_1(r2), f1(r2),
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2)          # Transparency of the fill

plt.fill_between(r3, f2_1(r3), f2_2(r3),
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2)          # Transparency of the fill

plt.xlim(-3.5, 6)
plt.ylim(-4, 5)


# In[4]:


def integrand(y, x):
    return x*y
# Tarea de integrales, ejercicio 1.a

x_lower = -3
x_upper = -1
y_upper = lambda x: np.sqrt(2*x+6)
y_lower = lambda x: -np.sqrt(2*x+6)

val1, abserr = dblquad(integrand, x_lower, x_upper, y_lower, y_upper)

print('valor val1 ', val1)

x_lower = -1
x_upper = 5
y_upper = lambda x: np.sqrt(2*x+6)
y_lower = lambda x: x-1

val2, abserr = dblquad(integrand, x_lower, x_upper, y_lower, y_upper)

print('valor tot ', val1+val2)
abserr


# In[105]:


# Tarea de integrales, ejercicio 1.b
f1 = lambda x: x**4
f2 = lambda x: 3*x-x**2

r = np.linspace(-4, 4, 2000)

plt.plot(r, f1(r), color ='blue')
plt.plot(r, f2(r), color ='black')

plt.fill_between(r, f2(r), f1(r),
                 where=(f2(r) > f1(r)),
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2)          # Transparency of the fill


plt.xlim(-3.5, 6)
plt.ylim(-4, 5)


# In[26]:


# Tarea de integrales, ejercicio 1.b
def integrand(y, x):
    return x

x_lower = 0
x_upper = 1.2
y_upper = lambda x: 3*x-x**2
y_lower = lambda x: x**4

val, abserr = dblquad(integrand, x_lower, x_upper, y_lower, y_upper)


print('valor tot ', val)
abserr


# In[29]:


# Tarea de integrales, ejercicio 1.c
x = [0, 0, 1]
y = [0, 1, 1]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.fill(x, y, alpha=0.3, color='b')


# In[85]:


# Tarea de integrales, ejercicio 1.c
def integrand(x, y):
    return x * np.sqrt(y**2 - x**2)

y_lower = 0
y_upper = 1
x_lower = 0
x_upper = lambda y: y

val, abserr = dblquad(integrand, y_lower, y_upper, x_lower, x_upper)

print('valor total ', val)
abserr


# In[82]:


# Tarea de integrales, ejercicio 1.d
f1 = lambda x: np.sqrt(x)
f2 = lambda x: np.sqrt((3-x)/2)

r = np.linspace(-4, 6, 2000)
plt.plot(r, f1(r), color ='blue')
plt.plot(r, f2(r), color ='black')

plt.fill_between(r, 0, f1(r),
                 where = f1(r) < f2(r),
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2)          # Transparency of the fill

plt.fill_between(r, 0, f2(r),
                 where = f2(r) < f1(r),
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2)          # Transparency of the fill

plt.xlim(-3, 6)
plt.ylim(0, 3)


# In[84]:


# Tarea de integrales, ejercicio 1.d
def integrand(y, x):
    return y**2-x

x_lower = 0
x_upper = 3
y_upper = lambda x: np.sqrt((3-x)/2)
y_lower = lambda x: np.sqrt(x)

val, abserr = dblquad(integrand, x_lower, x_upper, y_lower, y_upper)


print('valor tot ', val)
abserr


# In[90]:


# Tarea de integrales, ejercicio 1.e

f1 = lambda x: x
f2 = lambda x: 0

r = np.linspace(0, 1, 2000)

plt.plot(r, f1(r), color ='blue')
plt.plot([0, 1], [f2(0), f2(1)], color ='black')

plt.fill_between(r, f2(r), f1(r),
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2)          # Transparency of the fill

plt.xlim(-0.5, 1.5)
plt.ylim(-0.5, 1.5)


# In[102]:


# Tarea de integrales, ejercicio 1.e
def integrand(x, y):
    return np.sqrt(4*x**2 - y**2) if 4*x**2 - y**2 >= 0 else 0

y_lower = 0
y_upper = 1
x_lower = 0
x_upper = lambda x: x

val, abserr = dblquad(integrand, y_lower, y_upper, x_lower, x_upper)

print('valor total ', val)
abserr


# In[103]:


# Tarea de integrales, ejercicio 1.f
def integrand(x, y, z):
    return 1 / (1 + x + y + z)**3

z_lower = 0
z_upper = lambda x, y: 1 - x - y
y_lower = 0
y_upper = lambda x: 1 - x
x_lower = 0
x_upper = 1

val, abserr = tplquad(integrand, x_lower, x_upper, y_lower, y_upper, z_lower, z_upper)

print('valor total ', val)
print('error absoluto ', abserr)


# In[106]:


import numpy as np

# Definimos la función a integrar
def f(x):
    return x/(1+x**4)

# Definimos los limites de la integral
a = 0
b = 1
# Definimos el número de puntos de la cuadratura
N = 4

# Polinomios de Legendre
def legendre(n, x):
    if n == 0: # Si n = 0, entonces el polinomio de Legendre es 1
        return x*0 + 1.0
    elif n == 1: # Si n = 1, el polinomio de Legendre es x
        return x
    else: # Para n mayor a 1, el polinomio de Legendre se calcula por recursividad
        return ((2.0*n-1.0)*x*legendre(n-1,x)-(n-1)*legendre(n-2,x))/n

# Derivada de los polinomios de Legendre    
def dlegendre(n, x):
    x = np.array(x)
    if n == 0: # Si n es 0, la derivada da 0
        return x*0
    elif n == 1: # si n es 1, la derivada es 1
        return x*0 + 1.0
    else: # Para n mayor que 1, la derivada se calculará por recursividad y la regla del producto para derivadas
        return (n/(x**2-1.0))*(x*legendre(n,x)-legendre(n-1,x))

# Definimos un método de la secante para encontrar las raíces de los polinomios de Legendre
# Mi método de la secante:
def secv1(f, p0, p1, TOL=1e-5, N0=100):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while i <= N0:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if abs(p - p1) < TOL:
            return p
        i += 1
        p0, q0 = p1, q1
        p1, q1 = p, f(p)
    print("Se alcanzó el número máximo de iteraciones")
    return p

# Calculamos las raíces de los polinomios con el método de la secante
def legroots(n, delt=.2, Nit=1000, error='dist', eps=1e-05):
    roots = np.zeros(n) # iniciamos en ceros un arreglo donde se almacenan las raíces
    npos = n//2 # pq son simétricos
    
    f = lambda x: legendre(n, x)  # recordar que da dos salidas y quiero solo el Pn
    for i in range(npos): # Para cada punto hasta la mitad de puntos
        p0 = np.cos(np.pi*(4*i+3)/(4*n+2))  # semilla o aproximación para el método de la secante
        p1 = p0 + delt # La semilla para p1
        root = secv1(f, p0, p1, TOL=eps, N0=Nit) # Encontramos las raices
        roots[i] = -root # Almacenamos los negativos en el arreglo
        roots[-1-i] = root # Almacenamos los positivos en el arreglo
    return roots # Devolvemos un arreglo de las raíces encontradas

# Calculamos pesos y nodos para la cuadratura
def gau_param(n, delt=.2, Nit=1000, error='dist', eps=1e-05): 
    # Las raíces encontradas ahora son los nodos para la cuadratura
    xroot = legroots(n, delt=delt, Nit=Nit, error=error, eps=eps)
    dPn = legendre(n, xroot)[1] # Calculamos la derivada de los polinomios en los nodos
    # Pesos para la cuadratura
    cj = 2.0 / ((1.0 - xroot**2) * (dlegendre(N, xroot)**2))
    return xroot, cj # Devuelve nodos y pesos

# Calculamos la integral en los intervalos dados
def gauInt(f, interv, Npts, delt=0.2, Nit=1000, error='dist', eps=1e-05):
    a, b = min(interv), max(interv) # Nuestros limites de integración
    
    # Utilizamos los nodos y los pesos en estas nuevas variables
    xs, cs = gau_param(Npts, delt=delt, Nit=Nit, error=error, eps=eps)
    
    # Aplicando la fórmula, cambio de variables
    coeffp = 0.5*(b+a)
    coeffm = 0.5*(b-a)
    
    ts = coeffp + coeffm*xs # Nueva función t
    fk = cs*f(ts) # Calculamos los valores de la función en los nodos y multiplicamos por los pesos
    val = coeffm*np.sum(fk) # Hacemos la suma de los valores y multiplicamos por el coeficiente
    return val # El resultado de nuestra integral

interv = [0., 1.] # Intervalo
val = gauInt(f, interv, N, eps=1e-11)
print('El resultado es ', val)


# In[ ]:




