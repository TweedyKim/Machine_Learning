print('===================================================================')
print('|  Supervised Learning - Regression                               |')
print('|   - Data: California Housing Prices for 1990s                   |')
print('|   - Predict the median of housing prices in California          |')
print("===================================================================\n\n")

import pandas as pd
import numpy as np
from zlib import crc32

from sklearn.model_selection import train_test_split

csv_path = "./04_Hands_on_Machine_Learning/002_Begin_To_End_for_Machine_Learning/datasets/housing/housing.csv"
housing = pd.read_csv(csv_path)

print('1. Description')
print('   1) Split "Train_Set_Data" and "Test_Set_Data"')
print('   2) Ratio: Train_Set 80% / Test_Set 20%')
print('   3) Using by Scikit-learn')

print('2. Result')
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
print('   1) The count of Train Set: {}ea'.format(len(train_set)))
print('   2) The count of Test Set: {}ea'.format(len(test_set)))
