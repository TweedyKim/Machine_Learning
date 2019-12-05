print('===================================================================')
print('|  Supervised Learning - Regression                               |')
print('|   - Data: California Housing Prices for 1990s                   |')
print('|   - Predict the median of housing prices in California          |')
print("===================================================================\n\n")


import pandas as pd
import numpy as np

csv_path = "./04_Hands_on_Machine_Learning/002_Begin_To_End_for_Machine_Learning/datasets/housing/housing.csv"
housing = pd.read_csv(csv_path)

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

print('1. Description')
print('   1) Split "Train_Set_Data" and "Test_Set_Data"')
print('   2) Ratio: Train_Set 80% / Test_Set 20%')
print('   3) Mixing data by np.random.permutation()')
print('   4) List slicing according to test_ratio\n')
print('2. Problem')
print('   1) Train_Set will be same with Test_Set when it runs over and over.\n')

print('3. Result')
train_set, test_set = split_train_test(housing, 0.2)
print('   1) The count of Train Set: {}ea'.format(len(train_set)))
print('   2) The count of Test Set: {}ea'.format(len(test_set)))
