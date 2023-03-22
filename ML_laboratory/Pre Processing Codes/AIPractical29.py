# Working with Simple Imputer using most_frequent

import numpy as np

# Importing the SimpleImputer class
from sklearn.impute import SimpleImputer

# Imputer object using the mean strategy and  missing_values type for imputation
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

data = [[12,     np.nan, 30     ],
        [10,     20,     31     ],
        [np.nan, 11,     30     ],
        [10,     20,     np.nan ],
       ]


print("Original Data : \n", data)

# Fitting the data to the imputer object
imputer = imputer.fit(data)

# Imputing the data
data2 = imputer.transform(data)

print("Imputed Data : \n", data2)
