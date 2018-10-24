import pandas as pd

from src.knn import knn

dt = pd.read_csv('resources/test_data.csv', sep=',', header=None)
du = pd.read_csv('resources/learn_data.csv', sep=',', header=None)

kn = knn(du, 5)
kn.predict(dt)

#print(du)