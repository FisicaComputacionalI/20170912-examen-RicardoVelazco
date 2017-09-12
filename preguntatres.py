import numpy as np
import matplotlib.pyplot as plt
def f(a): return a + 1995
def g(t): return (4.5*np.sin(2*np.pi*t)) + 2013
a1 = np.arange(0, 22, 0.1)
t1 = np.arange(0, 22, 0.1)
plt.figure(1)
plt.subplot(211)
plt.title('Dos graficas', fontsize=20, color='red')
plt.plot(a1, f(t1), 'y', t1, g(t1), 'b')
plt.subplot(212)
plt.plot(t1, g(t1))
plt.savefig('preguntatres.png')
plt.show()
