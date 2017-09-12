import numpy as np
import matplotlib.pyplot as plt
def f(t): return (4.5 * np.sin(2*np.pi*t)) + 2013
t1 = np.arange(0.0,5.0,0.1)
plt.plot(t1, f(t1), 'b--')
plt.title('Grafica de sin', fontsize=15, color='red')
plt.savefig('preguntados')
plt.show()
