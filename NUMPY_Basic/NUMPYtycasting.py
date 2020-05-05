import numpy as np

arr = np.array([6, 8.9, 76, 9.8], dtype=float)
print(arr)
#Here 'astype' is using for type-conversion or typecasting
arr = arr.astype(int)
print(arr)
#Here we using 'np.nan' for filling the value of those indexes in future
arr2 = np.array([np.nan, 8, 9, np.nan])
print(arr2)
arr2[0] = 54
arr2[3] = 78
print(arr2)
#Here 'np.inf' is using for infinite value
#for +v 'np.inf' -v '-np.inf'
arr3 = np.array([np.inf, 9, 8, -np.inf])
print(arr3)
