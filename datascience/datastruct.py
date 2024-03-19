import numpy as np

# One dimensional arrays
a = np.array([10,20,30])

b = np.array([1,77,2,3])

print(a[0])
print(b[3])
print()
print()
# 2 Dimensional array

c = np.array([
    [10,20,30,40],
    [20,40,60,80]
])

# print(c)

d = np.full((3,5,4),7) 

print(d)

a = np.ones((3,3))
print(a)

a = np.arange(10, 50, 5)

print(a)

print()
print()
print()
print()
print()
b  = np.linspace(0, 100, 10)

print(b)

b = np.savetxt('myspace.csv', b, delimiter=';')

loaded_data = np.loadtxt('myspace.csv', delimiter=';')
print(loaded_data)