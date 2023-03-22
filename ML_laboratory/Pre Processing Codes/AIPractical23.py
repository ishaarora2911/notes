#Working with Missing data in Pandas dataset to used for machine learning
#In Pandas missing data is represented by two value:

#1) None:  None is a python singelton object that is often used for missing data in python code
#2) NaN: NaN (an accronym for NOt a Number) is a special floating point value recognized by all system

#Pandas treat None and Nan as essentitaly interchangeable for indicating missing or null values
#useful functions in pandas are
# isnull()
# notnull()
# dropna()
# fillna()
# replace()
# interpolate()

#1 Checking for missing using isnull()
# return dataframe of boolean values which are true for NaN

import pandas as pd
import numpy as np
data=pd.read_csv('employees_with_missing_data.csv')
#printing the first 10 to 24 rows of the data frame form visualization
print( data[10:25] )


#Analyse the value of gender in RowIndex no 20 and 22
#Now we are going to fill all the null values in Gender column with "NO GENDER"

#filling a null values using fillna()

df2=data["Gender"].fillna("No Gender")
df3=data[10:25]["Gender"].fillna("No Gender")
print("\n\n\n", data)
print("\n\n\n", df2)
print("\n\n\n", df3)

