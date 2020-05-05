import numpy as np
'''
    ***Random integers***
Similar to the Python random module, NumPy has its own submodule for
pseudo-random number generation called np.random. 
It provides all the necessary randomized operations and extends it to
multi-dimensional arrays. To generate pseudo-random integers, we use the
np.random.randint function.

The code below shows example usages of np.random.randint.
'''
print(np.random.randint(5))
print(np.random.randint(5))
print(np.random.randint(5, high=7))
arr = np.random.randint(-3, high=10, size=(2,2))
print(repr(arr))

'''
The np.random.randint function takes in a single required argument, 
which actually depends on the high keyword argument. 
If high=None (which is the default value), then the required argument 
represents the upper (exclusive) end of the range, with the lower end 
being 0. Specifically, if the required argument is n, then the random 
integer is chosen uniformly from the range [0, n).

If high is not None, then the required argument will represent the 
lower (inclusive) end of the range, while high represents 
the upper (exclusive) end.

The size keyword argument specifies the size of the output array, where 
each integer in the array is randomly drawn from the specified range. 
As a default, np.random.randint returns a single integer.
'''
