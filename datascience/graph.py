import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100000)
y = np.sin(x)

plt.plot(x, y)
plt.show()