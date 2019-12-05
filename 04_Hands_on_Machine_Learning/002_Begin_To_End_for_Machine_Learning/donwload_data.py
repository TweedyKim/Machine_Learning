print('===================================================================')
print('|  Download California Housing Prices for 1990s                   |')
print("===================================================================\n\n")


import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

def fetch_housing_data():
    if not os.path.isdir("./Machine_learning/" + HOUSING_PATH):
        os.makedirs("./Machine_learning/" + HOUSING_PATH)
    tgz_path = os.path.join("./Machine_learning/", HOUSING_PATH, "/housing.tgz")
    urllib.request.urlretrieve(HOUSING_URL, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path="./Machine_learning/" + HOUSING_PATH)
    housing_tgz.close()

fetch_housing_data()



