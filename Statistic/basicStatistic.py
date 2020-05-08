import statistics
import random
randomList = random.sample(range(0, 1000), 10)
print(randomList)
#https://pynative.com/python-random-sample/
import numpy

random_float_array = numpy.random.rand(2, 3)
print("Random float array 2X3 \n")
print(random_float_array,"\n")

#https://pynative.com/python-get-random-float-numbers/

random_float_array = numpy.random.uniform(75.5, 125.5, size=(2, 2))
print(random_float_array)

arr = numpy.arange(1,20,2)
