from matplotlib import pyplot as plt
import numpy as np
x = np.array([8,7,9,2,4])
y = np.array([6,5,1,9,3])
plt.scatter(x,y)
plt.title("Scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()