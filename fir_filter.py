import numpy as np
import matplotlib.pyplot as plt

def fir_filter_freq(x, b):
    M = len(b)
    N = len(x)
    H = np.fft.fft(b, N)
    X = np.fft.fft(x, N)
    Y = H * X   
    y = np.real(np.fft.ifft(Y, N))
    return y[0:N]
n = 200
t = np.linspace(0, 1, n)
x = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*10*t) + np.random.randn(n)*0.25
b = np.array([0.2, 0.2, 0.2, 0.2, 0.2,0.2,0.2])

y = fir_filter_freq(x, b)

plt.plot(t, x, label='Input signal')
plt.plot(t, y, label='Filtered signal')
plt.legend()
plt.show()
