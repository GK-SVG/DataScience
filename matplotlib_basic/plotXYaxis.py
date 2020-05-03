from matplotlib import pyplot as plt
import numpy as np
x = np.arange(1,11)
y = x*2
z = x*3
plt.plot(x,y,color="orange")
plt.plot(x,z,color="green",linestyle=':')
plt.title("line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.show()