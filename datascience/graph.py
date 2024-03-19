import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100000)
y = np.sin(x)



a = np.linspace(0, 10, 10000)
b = 4*a+6

plt.plot(a,b)
plt.show()