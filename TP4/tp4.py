import numpy as np
from scipy.linalg import solve

def gauss_jordan(A, b):
    n = len(A)
    # Aumenta a matriz A com o vetor b
    Ab = np.hstack((A, b.reshape(-1, 1)))
    
    for i in range(n):
        # Torna o elemento diagonal igual a 1
        Ab[i] = Ab[i] / Ab[i, i]
        
        # Torna todos os elementos na coluna atual 0, exceto o pivô
        for j in range(n):
            if i != j:
                Ab[j] = Ab[j] - Ab[j, i] * Ab[i]
    
    # A solução agora está na última coluna de Ab
    return Ab[:, -1]

# Exemplo de uso:
A = np.array([[3, -2,  5], [1,  0,  3], [2,  1,  1]], dtype=float)
b = np.array([5, 6, 7], dtype=float)
x_gauss_jordan = gauss_jordan(A, b)
print("Solução Gauss-Jordan:", x_gauss_jordan)

x_scipy = solve(A, b)
print("Solução Scipy:", x_scipy)

print("Comparação dos resultados:")
print("Solução Gauss-Jordan:", x_gauss_jordan)
print("Solução Scipy:", x_scipy)
print("Erro relativo:", np.linalg.norm(x_gauss_jordan - x_scipy))