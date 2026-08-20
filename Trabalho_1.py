#Questão 1
import numpy as np
P2 = float(input("Insira aqui sua potência:"))
dB = 10*np.log10(P2/(10**(-3)))
if dB>0:
    print (f"Sua potência em dB é:{dB}")
else:
    print ("Não é possivel calcular sua potência em dB")
#Questão 2
#item a)
n = int(input("Insira valor de n:"))
e = (1+1/n)**n
print (f"Seu valor de Euler para quando n for igual a {n} é:{e:.6f}")
#item b)
n = 1
e = 1
while e <= 2.718100:
    e = (1 + 1/n)**n
    n = n + 1
print(f"{e:.6f};{n}")
#Questão 3
import matplotlib.pyplot as plt
import numpy as np
p = 1200
pi = np.pi
Epsilon = float(input("Digite o valor de Epsilon:"))
theta_valor = []
r_valor = []
for theta in np.arange(-pi, pi, 0.1*pi):
    r = p/(1 - Epsilon*np.cos(theta))
    theta_valor.append(theta)
    r_valor.append(r)
    print(r, theta)
distancia_minima = min(r_valor)
distancia_maxima = max(r_valor)
plt.xlabel("Angulo ()")
plt.ylabel("Distância (r)")
plt.title("Estudo de Excentricidade")
plt.plot(theta_valor, r_valor)
plt.show()
print (f"Menor distância: {distancia_minima:.2f}")
print (f" Maior distância: {distancia_maxima:.2f}")
#Questão 4
pi = 3
i = int(input("Digite um valor para i:"))
for i in range(1, i+1):
    pi += (4*(-1)**(i-1))/(2*i*(2*i+1)*(2*i+2))
print (f"O valor de pi é: {pi:.10f}")
#Questão 5
import numpy as np
Epsilon = 1e-5
n = 1
termo = 1
s = termo
x = np.pi/2
def fatorial(n):
    fat = 1
    for i in range(2,n+1):
        fat = i*fat
    return fat
while np.abs(termo) >= Epsilon:
    termo = ((-1)**n)*x**(2*n)/(fatorial(2*n))
    s += termo
    n += 1
    print(s,n)