f = open("PythonPractice1.txt")
print(f.read())

"""g = open("PythonPractice2.docx")
print(g.read())"""

h = open("D:\python\pycharm\PythonPractice1.txt")
#print(h.read(100))

print(h.readline(5))
print(h.readline())
for x in f:
   print(x)

#close
print(f.close())

#write to existing file
f = open("PythonPractice2.txt","a")
f.write("Now the file has more content")
f.close()
f = open("PythonPractice2.txt","r")
print(f.read())

#f = open("Crime_Data.csv","w")
#print(f.read())

#create file
g = open("My_File.txt" , "x")
g.close()
import os
os.remove("My_File.txt")

import pandas as pd
april2018 = pd.read_csv("April2018.csv")
print(april2018)

#viewing the first 5 and the last 5 data points
print(april2018.head())
print(april2018.tail())

#to locate rows
#to locate the first row
print(april2018.loc[0])

#to locate the first and the 11th row
print(april2018.loc[[0, 10]])

#To locate the first 20 rows
print(april2018.loc[:19])
print(april2018.head(20))
#to locate a spefic number of rows
print(april2018.loc[5:20])

#to locate the last rows
print(april2018.loc[110:])

print(april2018.tail(20))

#calling columns
print(april2018.iloc[:,2])

print(april2018[["Request Date" , "Fare"]])

#slice column by range
print(april2018.loc[: , "Fare" : "Tip"])
print(april2018.loc[: , "Fare" : ])
print(april2018.loc[: , : "Fare"])

#slicing by selected column position
print(april2018.iloc[: , [1,3,5]])
print(april2018.iloc[: , 1:4])
print(april2018.iloc[: , :4])
print(april2018.iloc[: , 4 : ])
print(april2018.iloc[: , : : 8])

print(april2018.iloc[1:4 , 1:4])

print(april2018.info())

safaricom = pd.read_csv("safaricom_.csv")
print(safaricom)

print(safaricom.info())
safaricom.isnull()
safaricom.notnull()
safaricom.isnull().sum()

#filling null with a value
saf1 = safaricom.fillna(10,inplace = False)
print(saf1.info())

#saf1.to_csv("D:\python\pycharm\saf2.csv")



safaricom.info()

saf1.head(10)

#fillin null forward or backward
saf2 = safaricom.fillna(method = ("ffill"))
saf2.head(10)

saf3 = safaricom.fillna(method = ("bfill"))
saf3.head(10)

#filling with a mean
saf4 = safaricom.fillna(safaricom.mean())
saf4.head(10)

#Filling with median
saf5 = safaricom.fillna(safaricom.median())
saf5.head(10)

safaricom.median()
safaricom["MarketPrice"].median()

#fill null in the second column
low = safaricom["Low"].fillna(safaricom["Low"].median())
low.head(30)

#safaricom["Low"].mode()

#drop nulls
#fropping rows
saf6 = safaricom.dropna()
saf6

#driopping columns axis 1 = columns and axis 0 rows
saf7 = safaricom.dropna(axis = 1)
saf7

import pandas as pd
weather = pd.read_csv("weather.csv")
weather.head()
weather.info()
weather.shape
weather.describe()
weather.columns
weather.duplicated()

#change the datatype of a column
weather["MinTemp"].dtype
weather['MinTemp'] = weather["MinTemp"].astype('int64')

#find count for distinct  values in a  column
weather["MinTemp"].value_counts()

#find the % of distinct values on a column
weather["MinTemp"].value_counts(normalize = True)

#sort by single column
weather.sort_values(by = 'Rainfall' ,ascending = True).head(10)

#sort multiple columns
weather.sort_values(by = ['Rainfall','MaxTemp'] ,ascending = [True , False]).head(10)

#finding mean
weather.mean()

#condition while indexing the data frame
weather[weather['Sunshine'] > 5].mean()

weather[weather['Sunshine'] > 5]['Rainfall'].mean()

#the apply function
import numpy as np

weather[['Sunshine' , 'Rainfall' ,'MaxTemp']].apply(np.max)

#apply function to filter the rows
weather[weather['WindDir3pm'].apply(lambda WindDir3pm : WindDir3pm == 'NW')].head()



#apply function to filter the rows
weather[weather['WindDir3pm'].apply(lambda WindDir3pm : WindDir3pm == 'NW')].head()

