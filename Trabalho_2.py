#Questão 1
# Newton-Raphson para Raiz Cúbica de 7 e Raiz Quadrada de 5
def Newton(function, dfunction, x, n):
    def f(x):
        f_val = eval(function)
        return f_val
    def df(x):
        df_val = eval(dfunction)
        return df_val
        
    for intercept in range(1, n):
        i = x - (f(x)/df(x))
        x = i
    print(f"A raiz foi encontrada em {x}, após {n} iterações")

Newton("x**3 - 7", "3*x**2", 7, 10)
Newton("x**2 - 5", "2*x", 5, 10)
#Questão 2
import numpy as np

def cotg(x):
    return np.cos(x)/np.sin(x)

def f(x):
    return ((np.sqrt(938 + (60 - abs(x)))) / (197.326)) * cotg((1.45 * np.sqrt(938 + (60 - abs(x)))) / 197.326) + (np.sqrt(938 - abs(x)) / 197.326)

def secant(x0, x1, n, e):
    for interations in range(1, n):
        fx0 = f(x0)
        fx1 = f(x1)
        xi = x0 - fx0 / ((fx0 - fx1) / (x0 - x1))
        if abs(xi - x1) <= e:
            return xi
        x0 = x1
        x1 = xi
    print(f"O valor da raiz {xi} foi encontrada depois de {n} iterações")

def bissection(a, b, e):
    fa = f(a)
    fb = f(b)
    error = abs(b - a)
    while error > e:
        c = (a + b) / 2
        if fa * fb >= 0:
            print("Não há raizes ou multiplas raizes presentes, o metodo da bissecção não vai funcionar.")
            quit()
        elif fa * f(c) < 0:
            b = c
            error = abs(b - a)
        elif fb * f(c) < 0:
            a = c
            error = abs(b - a)
    print(f"O erro é {error}")
    print(f"O intervalo menor é {a} e o intervalo maior é {b}")

secant(0, 2, 5, 1e-5)
bissection(0, -2, 1e-5)