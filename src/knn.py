import numpy as np
import pandas as pd
from scipy.spatial import distance


def printarray(array):
    for z in array:
        print(z)

def take2nd(e):
    return e[1]

class knn:

    def __init__(self, list, k):
        self.list = list
        self.k = k

    def predict(self, list):
       for i in list:
           distances = []
           for j in self.list:
                distances.append((j,distance.euclidean(i[0:4], j[0:4])))
       distances.sort(key=take2nd)
       printarray(distances)
    def score(self, list):
        result = 0.0
        return result



arraytest = np.array(pd.read_csv('../resources/test_data.csv', sep=',', header=None))
arraylearn = np.array(pd.read_csv('../resources/learn_data.csv', sep=',', header=None))
kn = knn(arraylearn,5)
kn.predict(arraytest)
#print(kn.list)
