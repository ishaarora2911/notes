# Working with Simple Imputer using most_frequent
# Count total NaN at each column in DataFrame.

# import numpy library as np
import numpy as np

# import pandas library as pd
import pandas as pd

# List of Tuples
players = [ ('John',    22,     'Lucknow',   'Male'),
            ('Sachin',  np.NaN, 'Delhi',     np.NaN),
            ('Priti',   16,     'Patna',    'Female'),
            ('Trump',   41,     'Delhi',    'Male'),
            ('Alisha', np.NaN, 'Delhi',     'Female'),
            ('Virat',   35,     'Mumbai',    np.NaN),
            ('Obama',   35,      np.NaN,    'Male'),
            (np.NaN,    35,     'Uk',       'Male'),
            ('Jeet',    35,     'Guj',      'Male'),
            (np.NaN,    np.NaN, np.NaN,     np.NaN)
           ]

# Create a DataFrame object from list of tuples with columns and indices.
df = pd.DataFrame(players, columns=['Name', 'Age', 'Place', 'Sex'],
                            index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k'])

# show the boolean dataframe
print(" \nshow the boolean Dataframe : \n\n", df.isnull())

report = df.isnull().sum()
# Count total NaN at each column in a DataFrame
print(" \nCount total NaN at each column in a DataFrame : \n\n", report )
