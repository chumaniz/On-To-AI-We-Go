import numpy as np
import matplotlib.pyplot as plt
# If you see this, my advice is to comment out the non related code so that there is no clach in the interpreter 

x = np.linspace(0, 100, 100000)
y = np.sin(x)

plt.plot(x,y)
plt.show()

a = np.linspace(0, 10, 10000)
b = 4*a+6

plt.plot(a,b)
plt.show()

# Population density plot graph, just playing around
popul_dens_low = 10*np.random.random(100)

popul_dens_mid = 10*np.random.random(250)

popul_dens_high = 10*np.random.random(500)
plt.plot(popul_dens_high, 'bo')
plt.show()
plt.plot(popul_dens_mid, 'bo')
plt.show()
plt.plot(popul_dens_low, 'bo')
plt.show()

# Multiple Graphs
a = np.linspace(0,5,200)
b1 = 2*a
b2 = a**3
b3 = np.log(a)
plt.plot(a, b1)
plt.plot(a, b2)
plt.plot(a, b3)
plt.show()

# Sub Plots 

c = np.linspace(0,5,200)
d1 =  np.sin(c)
d2 = np.sqrt(c)
plt.subplot(211)
plt.plot(c, d1, 'r-')
plt.subplot(212)
plt.plot(c,d2,'g--')
plt.show()

# Figures instead of sub plots

plt.figure(1)
plt.title('My Life Right Now')
plt.xlabel("As Time Passes")
plt.ylabel("Life Trajectory")
plt.plot(c,d1,'r-')
plt.show()
plt.figure(2)
plt.title("How It should Be")
plt.xlabel("As Time Passes")
plt.ylabel("Life Trajectory")
plt.plot(c, d2, 'g--')
plt.show()