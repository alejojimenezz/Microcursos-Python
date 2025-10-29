import numpy as np
import matplotlib.pyplot as plt

# Datos - extraidos de https://www.cpubenchmark.net/cpu_list.php
procesadores_intel = ['i5-12400F', 'i7-12700K', 'i9-13900K']
rendimiento_intel = [19506, 34363, 58461]

procesadores_amd = ['Ryzen 5 7600', 'Ryzen 7 7800X3D', 'Ryzen 9 7950X']
rendimiento_amd = [27016, 34292, 62381]

# Posiciones en eje X
x = np.arange(len(procesadores_intel))
ancho = 0.4

plt.figure(figsize=(9,5))
plt.bar(x - ancho/2, rendimiento_intel, width=ancho, label='Intel', color='royalblue')
plt.bar(x + ancho/2, rendimiento_amd, width=ancho, label='AMD', color='darkorange')

procesadores_parejas = ['i5-12400F | Ryzen 5 7600', 'i7-12700K | Ryzen 7 7800X3D', 'i9-13900K | Ryzen 9 7950X']

plt.xlabel('Procesador', fontweight='bold')
plt.ylabel('Puntaje de rendimiento', fontweight='bold')
plt.title('Intel vs. AMD')
plt.xticks(x, procesadores_parejas, fontsize=8)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Puntajes sobre barras
for i in range(len(x)):
    plt.text(x[i] - ancho/2, rendimiento_intel[i] + 500, str(rendimiento_intel[i]), ha='center')
    plt.text(x[i] + ancho/2, rendimiento_amd[i] + 500, str(rendimiento_amd[i]), ha='center')

plt.show()