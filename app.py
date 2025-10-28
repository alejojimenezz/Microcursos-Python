import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
y = x**3 - 4*x

puntos_cero = []
for i in range(1, len(x)):
    if y[i-1] * y[i] < 0:  
        puntos_cero.append((x[i], y[i]))

plt.plot(x, y, label='f(x) = x³ - 4x')
for px, py in puntos_cero:
    plt.plot(px, py, 'ro', label='Raíz' if px == puntos_cero[0][0] else "")
plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.title("Gráfica de f(x) = x³ - 4x")
plt.legend()
plt.show()

print(puntos_cero)