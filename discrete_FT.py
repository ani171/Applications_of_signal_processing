import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 8, endpoint=False)
x = np.sin(5*np.pi*t)

N = len(x)
W = np.zeros((N, N), dtype=np.complex_)
for n in range(N):
    for k in range(N):
        W[n, k] = np.exp(-2j*np.pi*n*k/N)
X = np.dot(W, x)
print(X)
mag = np.abs(X)

fig, ax = plt.subplots(2, 1)
ax[0].plot(t, x)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].stem(mag)
ax[1].set_xlabel('Frequency')
ax[1].set_ylabel('Magnitude')
plt.show()
