import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100000)
y = np.sin(x)

# plt.plot(x,y)
# plt.show()

a = np.linspace(0, 10, 10000)
b = 4*a+6

# plt.plot(a,b)
# plt.show()

popul_dens_low = 10*np.random.random(100)
plt.plot(popul_dens_low, 'bo')
plt.show()

popul_dens_mid = 10*np.random.random(250)
plt.plot(popul_dens_low, 'bo')
plt.show()

popul_dens_high = 10*np.random.random(500)
plt.plot(popul_dens_high, 'bo')
plt.show()