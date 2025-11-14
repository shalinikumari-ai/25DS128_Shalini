import pandas as pd 
data = [10, 20, 30, 40]
s=pd.Series(data)

print(s)


data = {
    'Name' : ['Ritik', 'Aman', 'Priya','Neha'],
    'Age' : [21, 23, 20, 22],
    'Marks' : [85, 90, 78, 88]
}

df = pd.DataFrame(data)
print(df)
print(pd.__version__)

a = [1, 7, 2]
myvar = pd.Series(a, index=['x', 'y', 'z'])
print(myvar)
print(myvar["y"])

calories = {"day1" : 420, "day2" : 380, "day3" : 390}
myvar = pd.Series(calories)
print(myvar)