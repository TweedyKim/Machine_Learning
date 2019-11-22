import os
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"

# def fetch_housing_data():
#     if not os.path.isdir("./Machine_learning/" + HOUSING_PATH):
#         os.makedirs("./Machine_learning/" + HOUSING_PATH)
#     tgz_path = os.path.join("./Machine_learning/", HOUSING_PATH, "/housing.tgz")
#     urllib.request.urlretrieve(HOUSING_URL, tgz_path)
#     housing_tgz = tarfile.open(tgz_path)
#     housing_tgz.extractall(path="./Machine_learning/" + HOUSING_PATH)
#     housing_tgz.close()

#fetch_housing_data()

import pandas

def load_housing_data():
    csv_path = os.path.join("./Machine_learning/" + HOUSING_PATH, "housing.csv")
    return pandas.read_csv(csv_path)

#housing = load_housing_data()

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,1,50)

y1 = np.cos(4*np.pi*x)
y2 = np.cos(4*np.pi*x)*np.exp(-2*x)

plt.plot(x,y1,'r',label=r'$sin(4\pi x)$', lw=1)
plt.plot(x,y2,'b',label=r'$e^{-2x} sin(4\pi x)$', lw=1)
plt.title(r'$sin(4\pi x)$ vs $e^{-2x} sin(4\pi x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.text(0.5,-1.0,r'This is sample')
plt.axis([0,1,-1.5,1.5])
plt.grid(True)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
