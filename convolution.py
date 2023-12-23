import numpy as np

def convolve(x, h):
    N = len(x)
    M = len(h)
    X = np.zeros((N+M-1, N))
    for i in range(N):
        X[i:i+M, i] = h
    y = np.dot(X, x)
    return y

x = np.array([1,2,3])
h = np.array([1,2,1,1,1])
y = convolve(x, h)
print(y)
