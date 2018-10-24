from scipy.spatial.distance import euclidean


class knn:

    def __init__(self, list, k):
        self.list = list
        self.k = k

    def predict(self, list):
        test = ()
        for x in list:
            print(x)
           # test[x] = x[0:3]
        print(test)
        for i in list:
            nearest = ()
            for j in self.list:
               # distance = euclidean(list[3:4][i], self.list[3:4][j])
                print(j)

    def score(self, list):
        result = 0.0
        return result
