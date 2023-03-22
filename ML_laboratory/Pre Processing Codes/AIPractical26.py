#Dropping missing values using dropna()

# In order to drop a null values from a dataframe
#this function drop rows/columns of datasets with NUll values in different ways

# dropping rows with al least 1 null value

import pandas as pd
import numpy as np

# dictionary of lists

dict = {'First Score':[100,98,np.nan,95,np.nan],
        'Second Score':[30,np.nan,45, 56, np.nan],
        'Third Score':[52,48,88, 98,np.nan],
        'Fourth Score':[np.nan,np.nan, np.nan,65,np.nan]
        }
#Creating a dataframe from dictionary
df=pd.DataFrame(dict)
print(df)

#drop all rows that have any NaN values
df2=df.dropna()
print("\n\n", df2)

#drop only if ALL columns are NaN
df3 = df.dropna(how='all')
print("df3 = \n", df3 )
