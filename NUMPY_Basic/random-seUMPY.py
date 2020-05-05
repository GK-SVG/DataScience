import numpy as np
'''
    ***Utility functions***
Some fundamental utility functions from the np.random module are 
'np.random.seed'. We use the np.random.seed function to set the 
random seed, which allows us to control the outputs of the pseudo-random
functions. The function takes in a single integer as an argument, 
representing the random seed.

The code below uses np.random.seed with the same random seed. 
Note how the outputs of the random functions in each subsequent run 
are identical when we set the same random seed.
'''
np.random.seed(1)
print(np.random.randint(1, high=1000))
np.random.seed(2)
print(np.random.randint(1, high=1000))
print(np.random.randint(1, high=1000))
np.random.seed(1)
print(np.random.randint(1, high=1000))
np.random.seed(2)
print(np.random.randint(1, high=1000))
np.random.seed(3)
arr = np.random.randint(1, high=100, size=(2, 3))
print(repr(arr))
print(np.random.randint(1, high=100, size=(2, 3)))
np.random.seed(3)
arr = np.random.randint(1, high=100, size=(2, 3))
print(repr(arr))

'''
The np.random.shuffle function allows us to randomly shuffle an array. 
Note that the shuffling happens in place (i.e. no return value), and 
shuffling multi-dimensional arrays only shuffles the first dimension.

The code below shows example usages of np.random.shuffle. 
Note that only the rows of matrix are shuffled 
(i.e. shuffling along first dimension only).
'''

vec = np.array([1, 2, 3, 4, 5])
print(vec)
np.random.shuffle(vec)
print(vec)
np.random.shuffle(vec)
print(vec)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
np.random.shuffle(matrix)
print(matrix)
