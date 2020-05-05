import numpy as np
'''
To specify the number of elements in the returned array, rather than 
the step size, we can use the 'np.linspace' function.

This function takes in a required first two arguments, for the start and
end of the range, respectively. The end of the range is inclusive for 
'np.linspace', unless the keyword argument endpoint is set to False. 
To specify the number of elements, we set the num keyword argument 
(its default value is 50).

The code below shows example usages of np.linspace. 
It also takes in the dtype keyword argument for manual casting.
'''
arr = np.linspace(5, 11)
print(arr)
arr = np.linspace(5, 11, num=4)
print(arr)

arr = np.linspace(5, 11, num=4, endpoint=False)
print(arr)

arr = np.linspace(5, 11, num=4, dtype=np.int32)
print(arr)