#SimpleImputer is a scikit-learn class which is helpful in
#handling the missing data in predictive model dataset

#it replaces the NaN values with a specified placeholder
# It is implemented by the use of SimpleImputer(), which takes following arguments:
#1) missing_values : the missing_values placeholder which has to be imputed, by default it is NaN
#2) strategy : the data which will replace the NaN values from the dataset
# the strategy argument can take the values - 'mean'(default)
# 'median, 'most-frequent' and 'constant'
#3) fill_value: the constant value to be given to the Nan data uisng the constant strategy


import numpy as np
from sklearn.impute import SimpleImputer
#Imputer object using the mean strategy and missing_values type for imputation

imputer= SimpleImputer(missing_values=np.nan,strategy='mean')
data=[[12, np.nan,34],[10,32, np.nan],[np.nan, 11,20]]

print("Original Data : \n", data)

#fitting the data to the imputer object

imputer = imputer.fit(data)


#Imputing the data
data2=imputer.transform(data)
print("Imputed Data : \n", data2)
#NOte: the mean or median is taken along the column of the matrix
