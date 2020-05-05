import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]])
print(repr(arr[:, 1:]))
print(repr(arr[0:3, :-2]))
print(repr(arr[:, -1]))
print(repr(arr[0:1, 1:]))
print(repr(arr[0, 1:]))
