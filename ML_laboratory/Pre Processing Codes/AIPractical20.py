#Working with Missing data in Pandas dataset to used for machine learning
#In Pandas missing data is represented by two value:
# Filling missing values using fillna(), replace and interpolate()

#1) In order to fill null value in a dataset we use fillna, replace() and interpolate()
# These will replace NaN values with some some values of their own
# Interpolate() is used to fill NA values in the data frame
# but it uses various interpolation techniques to fill the mising values rather tan hard coding the value

import pandas as pd
import numpy as np

#filling missing value with previous ones
dict={'First Score':[100,90,np.nan,95],'Second Score':[30,45,56,np.nan], 'Third Score':[np.nan, 40, 80,98]}
df=pd.DataFrame(dict)
#filling a missing with previous ones
df2=df.fillna(method='pad')
print( df )
print( df2 )
