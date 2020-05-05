import numpy as np
'''
A. Ranged data
While 'np.array' can be used to create any array, it is
equivalent to hardcoding an array. This won't work when the array has 
hundreds of values. Instead, NumPy provides an option to create ranged 
data arrays using 'np.arange'. The function acts very similar to the 
'range' function in Python, and will always return a 1-D array.
'''

arr = np.arange(5)
print(arr)
arr = np.arange(1.5, 6)
print("\n", arr)
arr = np.arange(1.5, 9, 1.5)
print("\n", arr)


