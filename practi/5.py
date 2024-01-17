import numpy as np
a = np.array ([[1,2,3],[4,5,6],[7,8,9]])
print(type(a))
print(a)
print(a.shape)
b = np.mat(a)
#b = np.matrix ([[1,2,3],[4,5,6],[7,8,9]])
print(type(b))
print(b)
print(b.shape)
 