import numpy as np

# There comes a time in programming when you think you're too smart for a prerequisite
# And you skip it...only for it to stump you later on
# Don't be that guy
# I tried and it humbled me.
# (I tried to do machine learning without understanding foundational frameworks from Data Science)


# Making a matrix of 1s and 0s in any particular sequence
a = np.zeros((3,3))
b = np.ones((2,3,4,5))

# print(a,b)

# empty and random
c = np.empty((4,4))
d = np.random.random((2,3))



# Ranges
e = np.arange(8,52,4,) # Min, Max and step size


# Linspace, is different by usinf number of digits in set vs step size

f = np.linspace(8,80,11)


# NaN...no not my nan...Not A Number
# Acts as a placeholder
g = np.NAN

# Attributes 
# print(b.shape)
# print(b.ndim)
# print(b.size)
# print(b.dtype)

