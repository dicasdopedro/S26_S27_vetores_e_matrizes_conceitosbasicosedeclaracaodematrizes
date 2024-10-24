# Criação de um vetor de inteiros
vetor = [10, 20, 30, 40, 50]
print(vetor)

# Acessar o terceiro elemento do vetor
print(vetor[2])  # Saída: 30

# Atualizar o segundo valor para 25
vetor[1] = 25
print(vetor) # Saída: [10, 25, 30, 40, 50]

# Criar uma matriz 2x2
matriz = [[1, 2], [3, 4]]
print(matriz) # Saída: [[1, 2], [3, 4]]

# Acessar o elemento na primeira linha e segunda coluna
print(matriz[0][1])  # Saída: 2

# Atualizar o valor da segunda linha e primeira coluna
matriz[1][0] = 10
print(matriz) # Saída: [[1, 2], [10, 4]]

# Criar uma matriz 3x3 usando um loop
matriz = [[i * j for j in range(3)] for i in range(3)]
print(matriz) # Saída: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Somar dois vetores de mesmo tamanho
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
soma_vetores = [vetor1[i] + vetor2[i] for i in range(len(vetor1))]
print(soma_vetores) # Saída: [5, 7, 9]

# Multiplicar um vetor por um escalar
escalar = 3
multiplicacao_vetor = [escalar * x for x in vetor1]
print(multiplicacao_vetor) # Saída: [3, 6, 9]

# Somar duas matrizes 2x2
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
soma_matrizes = [[matriz1[i][j] + matriz2[i][j] for j in range(2)] for i in range(2)]
print(soma_matrizes) # Saída: [[6, 8], [10, 12]]

# Multiplicar uma matriz 2x2 por um escalar
escalar = 2
multiplicacao_matriz = [[escalar * matriz1[i][j] for j in range(2)] for i in range(2)]
print(multiplicacao_matriz) # Saída: [[2, 4], [6, 8]]

# Transpor uma matriz 2x3 para 3x2
matriz = [[1, 2, 3], [4, 5, 6]]
transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print(transposta) # Saída: [[1, 4], [2, 5], [3, 6]]

# Calcular o produto escalar de dois vetores
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
produto_escalar = sum(v1 * v2 for v1, v2 in zip(vetor1, vetor2))
print(produto_escalar) # Saída: 32

# Multiplicar duas matrizes 2x2
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
print(resultado) # Saída: [[19, 22], [43, 50]]

# Usando NumPy para simplificar operações com matrizes
import numpy as np


matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])


# Soma de matrizes
print(matriz1 + matriz2)

"""
Saída: [[ 6  8]
 [10 12]]
"""

# Multiplicação de matrizes
print(np.dot(matriz1, matriz2))
"""
Saída: [[19 22]
 [43 50]]
"""