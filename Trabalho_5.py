#Questão 1
import numpy as np
matA_B = [
    [3, 5, 7, 2, -2],
    [12, 11, 4, 6, 36],
    [10, 8, 4, -1, 4],
    [8, 10, 6, -2, -60]
]

print(np.array(matA_B))
n = len(matA_B)

def gauss(matA_B):
    for j in range(n-1):
        matA_B[j][j] = np.argmax(matA_B)
        for i in range(n):
            if i > j:
                m_ij = (matA_B[i][j]) / (matA_B[j][j])
                for k in range(n+1):
                    if matA_B[i][k] != 0:
                        matA_B[i][k] += -m_ij * matA_B[j][k]
    
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = matA_B[i][n]
        for j in range(i+1, n):
            x[i] -= matA_B[i][j] * x[j]
        x[i] /= matA_B[i][i]
    return x

print(gauss(matA_B))
#Questão 2
import numpy as np

def EGPP(n, A, b):
    matA_B = []
    for i in range(n):
        linha_completa = list(A[i]) + [b[i]]
        matA_B.append(linha_completa)
        
    for j in range(n-1):
        linha_pivo = j
        for linha in range(j+1, n):
            if abs(matA_B[linha][j]) > abs(matA_B[linha_pivo][j]):
                linha_pivo = np.copy(linha)
        matA_B[j], matA_B[linha_pivo] = matA_B[linha_pivo], matA_B[j]
        
        for i in range(n):
            if i > j:
                m_ij = (matA_B[i][j]) / (matA_B[j][j])
                for k in range(n+1):
                    if matA_B[i][k] != 0:
                        matA_B[i][k] += -m_ij * matA_B[j][k]
                        
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = matA_B[i][n]
        for j in range(i+1, n):
            x[i] -= matA_B[i][j] * x[j]
        x[i] /= matA_B[i][i]
    return x

matriz_A = [
    [3, 5, 7, 2],
    [12, 11, 4, 6],
    [10, 8, 4, -1],
    [8, 10, 6, -2]
]
vetor_b = [-2, 36, 4, -60]
dimensao = 4

solucao = EGPP(dimensao, matriz_A, vetor_b)
print(solucao)
#Questão 3
import numpy as np

# A função EGPP(n,A,b) declarada no exercício 3 é repetida aqui no código original

VO = 110
R = 1 + 19 * np.random.rand(12)
R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12 = R
G1, G2, G3, G4, G5, G6 = 1/R1, 1/R2, 1/R3, 1/R4, 1/R5, 1/R6
G7, G8, G9, G10, G11, G12 = 1/R7, 1/R8, 1/R9, 1/R10, 1/R11, 1/R12

matriz_A = [
    [G1+G2+G4, -G2, 0, -G4, 0, 0, 0], # Nó b
    [-G2, G2+G5, 0, 0, -G5, 0, 0], # Nó c
    [0, 0, G3+G6+G8, -G6, 0, 0, 0], # Nó d
    [-G4, 0, -G6, G4+G6+G7+G9, -G7, -G9, 0], # Nó e
    [0, -G5, 0, -G7, G5+G7+G10, 0, -G10], # Nó f
    [0, 0, 0, -G9, 0, G11+G9+G12, -G12], # Nó h
    [0, 0, 0, 0, -G10, -G12, G10+G12] # Nó g
]

vetor_b = [G1*VO, 0, G3*VO, 0, 0, 0, 0]
dimensao = 7

solucao = EGPP(dimensao, matriz_A, vetor_b)
nos = ['Vb', 'Vc', 'Vd', 'Ve', 'Vf', 'Vh', 'Vg']

print("Tensões calculadas para cada nó:")
for no, valor in zip(nos, solucao):
    print(f"{no} = {valor:.4f} V")

# Para o exercício 5 (Resistor Equivalente):
Vb = solucao[0]
Vd = solucao[2]
I_total = ((VO - Vb) / R1) + ((VO - Vd) / R3)
Ref = VO / I_total
print(f"Valor de Resistor Equivalente: {Ref}")
