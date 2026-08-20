#Questão 1
import numpy as np
import matplotlib.pyplot as plt

def derivada_5pontos(f, x, h):
    tam = len(x)
    fx = f(x)
    df = np.zeros(tam)
    for i in range(tam):
        if i < 2:
            df[i] = (fx[i+1] - fx[i]) / h
        elif i >= tam-2:
            df[i] = (fx[i] - fx[i-1]) / h
        else:
            df[i] = (1 / (12*h)) * (fx[i-2] - 8*fx[i-1] + 8*fx[i+1] - fx[i+2])
    return df

def f(x):
    return np.cos(x) * np.sinh(x)

def df(x):
    return -np.sin(x) * np.sinh(x) + np.cos(x) * np.cosh(x)

x, passo = np.linspace(0, np.pi/2, 1002, retstep=True)
resultado = derivada_5pontos(f, x, passo)

plt.plot(x, df(x))
plt.plot(x, resultado)
plt.grid()
plt.show()
#Questão 2
import numpy as np

a = 0.0
b = 1.0
N = 10000 
h = (b-a)/N
x0 = a

def f(x):
    return 4 / (1 + x**2)

def Trapezio(f, a, b, h):
    y = np.empty(N+1)
    y[0] = f(a)
    y[N] = f(b)
    i = 1
    sum_val = h * ((f(x0) + f(x0 + N*h)) / 2)
    while i < N:
        y[i] = f(x0 + i*h)
        sum_val = sum_val + h * f(x0 + i*h)
        i += 1
    return sum_val

def Simpson13(f, a, b, h):
    y = np.empty(N+1)
    y[0] = f(a)
    y[N] = f(b)
    i = 1
    sum_val = (f(x0) + f(x0 + N*h))
    p = 0
    q = 0
    while i < N:
        y[i] = f(x0 + i*h)
        if i % 2 == 0:
            p += 2 * (y[i])
        else:
            q += 4 * (y[i])
        i += 1
    sum_val = (h/3) * (sum_val + p + q)
    return sum_val

def Simpson38(f, a, b, h):
    y = np.empty(N+1)
    y[0] = f(a)
    y[N] = f(b)
    i = 1
    sum_val = (f(x0) + f(x0 + N*h))
    p = 0
    q = 0
    while i < N:
        y[i] = f(x0 + i*h)
        if i % 3 == 0:
            p += 2 * (y[i])
        else:
            q += 3 * (y[i])
        i += 1
    sum_val = (3*h/8) * (sum_val + p + q)
    return sum_val
#Questão 3
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = np.pi
N = 1000 
h = (b-a)/N

def f_bessel(theta, m, x):
    return (np.cos(m * theta - x * np.sin(theta)))

def Simpson13_bessel(m, x):
    y = np.empty(N+1)
    i = 1
    sum_val = (f_bessel(a, m, x) + f_bessel(b, m, x))
    p = 0
    q = 0
    while i < N:
        theta_i = a + i*h
        y[i] = f_bessel(theta_i, m, x)
        if i % 2 == 0:
            p += 2 * (y[i])
        else:
            q += 4 * (y[i])
        i += 1
    sum_val = (h/3) * (sum_val + p + q) / np.pi
    return sum_val

# Item (b)
Lambda = 500e-9 
r_val = np.linspace(1e-9, 10e-6, 100) 

def Intensidade(r):
    k = 2 * np.pi / Lambda
    m1 = 1
    Bessel = Simpson13_bessel(m1, k*r)
    termo = k*r
    return (Bessel/termo)**2

I = np.zeros(len(r_val))
for i, r_atual in enumerate(r_val):
    I[i] = Intensidade(r_atual)