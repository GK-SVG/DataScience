import numpy as np
'''
     *** Reshaping data ***
The function we use to reshape data in NumPy is np.reshape.
It takes in an array and a new shape as required arguments. 
The new shape must exactly contain all the elements from the input array.
For example, we could reshape an array with 12 elements to (4, 3), but 
we can't reshape it to (4, 4).

We are allowed to use the special value of -1 in at most one dimension
of the new shape. The dimension with -1 will take on the value necessary
to allow the new shape to contain all the elements of the array.
'''
arr = np.arange(8)

reshaped_arr = np.reshape(arr, (2, 4))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))

reshaped_arr = np.reshape(arr, (2, 2, 2))
print(repr(reshaped_arr))
print('New shape: {}'.format(reshaped_arr.shape))
transposed = np.transpose(reshaped_arr, axes=(0, 2 ,1))
print(transposed)

arr2 = np.arange(12)
reshaped_arr2 = np.reshape(arr2, (3, 2, 2))
transposed2 = np.transpose(reshaped_arr2, axes=(1, 0, 2))
print("arr2:", arr2)
print("\nreshaped_arr2:", reshaped_arr2)
print("\nTransposed2:", transposed2)

