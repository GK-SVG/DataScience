import pandas as pd
#read_csv is a inbuild input function which takes .csv file in input
iris = pd.read_csv('iris.csv')
#head give top 5 values of the file we can also give number of values like iris.head[10]
print(iris.head())
#tail give last 5 values of the file or iris.tail[10]
print(iris.tail())
#describe give the descripation f given file
print(iris.describe())

         #iloc give perticular row and column output

# iris = iris.iloc[50:60, 0:1]
# print(iris)
# iris2 = iris.iloc[10:25, 0:1]
# print(iris2)
# iris3 = iris.loc[50:60, ("first_name")]
# print(iris3)

record = {

    'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya'],
    'Age': [21, 19, 20, 18, 17, 21],
    'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
    'Percentage': [88, 92, 95, 70, 65, 78]}

# create a dataframe
dataframe = pd.DataFrame(record, columns=['Name', 'Age', 'Stream', 'Percentage'])

print("Given Dataframe :\n", dataframe)

# selecting rows based on condition
rslt_df = dataframe[dataframe['Percentage'] > 80]

print('\nResult dataframe :\n', rslt_df) 