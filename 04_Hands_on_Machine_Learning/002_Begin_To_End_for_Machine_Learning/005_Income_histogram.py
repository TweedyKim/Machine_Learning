print('===================================================================')
print('|  Supervised Learning - Regression                               |')
print('|   - Data: California Housing Prices for 1990s                   |')
print('|   - Predict the median of housing prices in California          |')
print("===================================================================\n\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

csv_path = "./04_Hands_on_Machine_Learning/002_Begin_To_End_for_Machine_Learning/datasets/housing/housing.csv"
housing = pd.read_csv(csv_path)

print('1. Modify median_income')
print('   1) Make a specific category by median_income')
print('   2) median_income divide 1.5 = income_cat')
print('   3) If income_cat goes over 5, it fix as 5\n')
housing["income_cat"] = np.ceil(housing["median_income"]/1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)

print('2. Show histogram')
housing["income_cat"].hist(bins=50, figsize=(20,15))
plt.show()

from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

print(housing["income_cat"].value_counts() / len(housing))