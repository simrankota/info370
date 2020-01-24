import numpy as np
# print(np._version_) 

a = np.array([1, 2, 3, 4, 5])
print(a)

b = np.array([[1, 2], [3,4]])
print(b)

print(b.shape)

print(a.shape)

print(a)
print(1 + a)

print(b)
print(np.sqrt(b))

print(np.arange(10))

print(1 + np.arange(10))

print(np.arange(10).reshape((2, 5)))

print(np.zeros((2, 5)))
print(np.ones((2, 5)))

print(np.random.normal(size = (4,3)))
