from matplotlib import pyplot as plt
import numpy as np
students = {
    'Gautam':40,
    'Ashu':60,
    'Gaurav':50,
}
names = list(students.keys())
values = list(students.values())
plt.bar(names,values,color="green")
plt.title("Student Marks")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.grid(True)
plt.show()