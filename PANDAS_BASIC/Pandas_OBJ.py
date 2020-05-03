import pandas as pd

#pandas arry are labled array which show value as well index
s1 = pd.Series([10, 20, 30, 40])
print(s1)
#we can also use it as an dictionary
s1 = pd.Series({"a": 10, "b": 20, "e": 30, "d": 40})
print(s1)
     #now this is all about  1d array

    #Lets move on multi diamentonal array

stu = pd.DataFrame({"Name": ['Gautam', 'Ashu', 'Gaurav', 'Amit'], "Marks": [30, 28, 35, 25]})
print(stu)


