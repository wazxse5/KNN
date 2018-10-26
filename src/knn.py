from scipy.spatial import distance
from src.functions import choose_best_match, take2nd


class Knn:

    def __init__(self, learning_list, k):
        self.learned_list = learning_list
        self.k = k

    def predict(self, list_to_classify):
        predicted_labels = []

        for i in list_to_classify:
            distances = []
            neighbors = []
            for j in self.learned_list:
                distances.append((j, distance.euclidean(i[0:4], j[0:4])))
            distances.sort(key=take2nd)
            for x in range(self.k):
                neighbors.append(distances[x][0][4])
            label = choose_best_match(neighbors)
            predicted_labels.append(label)

        return predicted_labels

    def score(self, list_to_classify, labels):
        good = 0
        wrong = 0
        predicted_labels = self.predict(list_to_classify)
        for i in range(len(predicted_labels)):
            if predicted_labels[i] == labels[i]:
                good += 1
            else:
                wrong += 1
        result = good / (good + wrong)
        return result
