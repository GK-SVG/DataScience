import numpy as np
'''
While NumPy provides built-in distributions to sample from, we can 
also sample from a custom distribution with the np.random.choice 
function.
'''
arr = np.array(['a', 'b', 'c', 'd'])
print(np.random.choice(arr))
print(np.random.choice(arr, p=[.01, .35, .35, .29], size=(2, 2)))
'''
The required argument for np.random.choice is the custom distribution 
we sample from. The p keyword argument denotes the probabilities given 
to each element in the input distribution. Note that the list of 
probabilities for p must sum to 1.
'''