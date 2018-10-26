import numpy as np
import pandas as pd

from src.functions import remove_labels_from
from src.knn import Knn

array_test = np.array(pd.read_csv('resources/test_data.csv', sep=',', header=None))
array_learn = np.array(pd.read_csv('resources/learn_data.csv', sep=',', header=None))

kn = Knn(array_learn, 15)
sc = kn.predict(remove_labels_from(array_test))
print(sc)
wsp = kn.score(array_test, sc)
print(wsp)
