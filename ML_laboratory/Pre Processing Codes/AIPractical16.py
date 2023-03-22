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
bool_series=data.isnull()
bool_series=data["Gender"].isnull()
#creating bool series True for NaN values
#bool series = =pd.isnull(data["Gender"])  #this is also ok

print(bool_series)

#filtering data
# displaying data only with Gender = NaN
result1 = data[bool_series]
result2 = data["Gender"][bool_series]
print(result1)
print(result2)