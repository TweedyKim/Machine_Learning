print('===================================================================')
print('|  Supervised Learning - Regression                               |')
print('|   - Data: California Housing Prices for 1990s                   |')
print('|   - Predict the median of housing prices in California          |')
print("===================================================================\n\n")


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_path = "./04_Hands_on_Machine_Learning/002_Begin_To_End_for_Machine_Learning/datasets/housing/housing.csv"
housing = pd.read_csv(csv_path)

print('1. Head Info')
print(housing.head(), end='\n\n')
print('2. Data Info')
print(housing.info(),end='\n\n')
print('3. Index Info of "ocean_proximity"')
print(housing["ocean_proximity"].value_counts(),end='\n\n')
print('4. Data Describe')
print(housing.describe(), end='\n\n')
print('5. Show histogram')
housing.hist(bins=50, figsize=(20,15))
plt.show()
