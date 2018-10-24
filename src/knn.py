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
           neightbours = []
           for j in self.list:
                distances.append((j,distance.euclidean(i[0:4], j[0:4])))
           distances.sort(key=take2nd)
           #printarray(distances)
           for x in range(self.k):
                neightbours.append(distances[x][0][4])
           print(neightbours)
       return neightbours

    def score(self, list, labels):
        result = 0.0
        return result



arraytest = np.array(pd.read_csv('../resources/test_data.csv', sep=',', header=None))
arraylearn = np.array(pd.read_csv('../resources/learn_data.csv', sep=',', header=None))
kn = knn(arraylearn,15)
sc = kn.predict(arraytest)
wsp = kn.score(arraytest,sc)
#print(kn.list)
