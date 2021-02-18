import numpy as np

#Access Array Elements
# arr = np.array([[1, 2, 3], [4, 5, 6]]) 2-D arrays
#arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])# 3-D arrays
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
b = np.array([1, 2, 3, 4, 5])
print(b.ndim)



print(b[3])
