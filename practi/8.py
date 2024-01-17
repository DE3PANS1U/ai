import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print("After Slicing:")
print("everything")
b=a[:]
print(b)
print("everything till 1st row")
b=a[:1]
print(b)
print("everything execpt 1st row")
b=a[1:]
print(b)
print("[row,column] all row till 1st column")
b=a[:,:1]
print(b)
print("all row except 1st column")
b=a[:,1:]
print(b)
print("all row & last column")
b=a[:,-1:]
print(b)