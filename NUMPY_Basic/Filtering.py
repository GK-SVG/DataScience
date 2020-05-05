import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print(repr(arr > 3))
print(repr(arr == 2))
print(repr(~(arr == 2)))
arr= np.array([[1, np.nan, 8],
                 [4, 6, 2],
                 [np.nan, 45, np.nan]])
print(repr(np.isnan(arr)))
print(repr(~(np.isnan(arr))))