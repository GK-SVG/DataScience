from matplotlib import pyplot as plt
fruits = ['pepsi','dew','mirinda','slice','coke','sprite']
cost = [60,60,55,70,45,50]
plt.pie(cost,labels=fruits,autopct='%0.1f%%')
plt.show()