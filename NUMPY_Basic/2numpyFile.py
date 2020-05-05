import numpy as np

arr = np.array([[1, 2, 3, 4] , [5, 5, 6.9, 8]], dtype=float)
arr2 = arr
arr2[0][1] = 12
print('when arr2=arr directly')
print(arr)
print("\n", arr2)
print('when arr2=arr.copy()')
arr2 = arr.copy()
arr2[1][1] = 9
print(arr)
print("\n", arr2)
