
import numpy as np
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

data = [[12, np.nan, 34],
        [10, 32, np.nan],
        [np.nan, 11, 20]]

print("Original Data : \n", data)

# Fitting the data to the imputer object
imputer = imputer.fit(data)

# Imputing the data
data2 = imputer.transform(data)

print("Imputed Data : \n", data2)
