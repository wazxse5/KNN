import numpy as np
import pandas as pd
from src.Knn import Knn
from src.functions import remove_labels_from, remove_data_from

array_test = np.array(pd.read_csv('resources/test_data.csv', sep=',', header=None))
array_learn = np.array(pd.read_csv('resources/learn_data.csv', sep=',', header=None))

kn = Knn(array_learn, 2)
sc = kn.predict(remove_labels_from(array_test))

wsp = kn.score(remove_labels_from(array_test), remove_data_from(array_test))
print(wsp)
