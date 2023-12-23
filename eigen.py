import numpy as np
N = 8
t = np.arange(N)
x = np.sin(5*np.pi*t)
W = np.zeros((N, N), dtype=np.complex64)
for i in range(N):
    for j in range(N):
        W[i,j] = np.exp(-2j * np.pi * i * j / N)

X = np.dot(W, x)
el, ev = np.linalg.eig(W)
print('Eigenvalues of DFT matrix:')
print(el)
print('Eigenvectors of DFT matrix:')
print(ev)

eigvals_mag = np.absolute(ev)
print("Energy at each frequency component of the signal.:\n", eigvals_mag)
