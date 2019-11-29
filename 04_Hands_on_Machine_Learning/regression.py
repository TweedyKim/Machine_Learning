import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from zlib import crc32

from sklearn.model_selection import train_test_split

def Get_Housing_Data():
    csv_path = "./04_Hands_on_Machine_Learning/datasets/housing/housing.csv"
    return pd.read_csv(csv_path)

def Print_Houisng(h):
    print(h.head(), end='\n\n')
    print(h.info(),end='\n\n')
    print(h["ocean_proximity"].value_counts(),end='\n\n')
    print(h.describe(), end='\n\n')

def Plt_Housing(h):
    h.hist(bins=50, figsize=(20,15))
    plt.show()

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]


housing = Get_Housing_Data()
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
print(train_set.info())
print(test_set.info())

# housing_with_id = housing.reset_index()
# housing_with_id["id"] = housing["longitude"]*1000 + housing["latitude"]

# train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

# Print_Houisng(housing)
# Plt_Housing(housing)
# train_set, test_set = split_train_test(housing, 0.2)
# print(len(train_set), "train +", len(test_set), "test")
