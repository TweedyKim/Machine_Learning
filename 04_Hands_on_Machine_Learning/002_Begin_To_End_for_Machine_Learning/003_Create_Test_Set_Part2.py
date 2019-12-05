print('===================================================================')
print('|  Supervised Learning - Regression                               |')
print('|   - Data: California Housing Prices for 1990s                   |')
print('|   - Predict the median of housing prices in California          |')
print("===================================================================\n\n")

import pandas as pd
import numpy as np
from zlib import crc32

csv_path = "./04_Hands_on_Machine_Learning/002_Begin_To_End_for_Machine_Learning/datasets/housing/housing.csv"
housing = pd.read_csv(csv_path)

def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

print('1. Description')
print('   1) Split "Train_Set_Data" and "Test_Set_Data"')
print('   2) Ratio: Train_Set 80% / Test_Set 20%')
print('   3) Using by CRC32')
print('   4) Caculate hash value and get into Test_Set about 20%% of the last byte.\n')
print("   5) 1'st Result: It makes ID using by index")
print("   6) 2'nd Result: It makes ID using longitude and latitude")

print("2. 1'st Result")
housing_with_id = housing.reset_index()
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")
print('   1) The count of Train Set: {}ea'.format(len(train_set)))
print('   2) The count of Test Set: {}ea'.format(len(test_set)))

print("3. 2'nd Result")
housing_with_id["id"] = housing["longitude"]*1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")
print('   1) The count of Train Set: {}ea'.format(len(train_set)))
print('   2) The count of Test Set: {}ea'.format(len(test_set)))
