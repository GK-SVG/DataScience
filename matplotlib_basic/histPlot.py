from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
exams = pd.read_csv('exams2.csv')
plt.hist(exams['math score'],bins=15)
plt.grid(True)
plt.show()