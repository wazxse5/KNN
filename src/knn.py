from scipy.spatial.distance import euclidean
from scipy.spatial import distance
import numpy as np
import pandas as pd



class knn:

    def __init__(self, list, k):
        self.list = list
        self.k = k

    def predict(self, list):
       for i in list:
           distances = []
           for j in self.list:
                distances.append((j,distance.euclidean(i[0:4], j[0:4])))
       print(distances)

    def score(self, list):
        result = 0.0
        return result



arraytest = np.array(pd.read_csv('../resources/test_data.csv', sep=',', header=None))
arraylearn = np.array(pd.read_csv('../resources/learn_data.csv', sep=',', header=None))
kn = knn(arraytest,5)
kn.predict(arraylearn)
#print(kn.list)
