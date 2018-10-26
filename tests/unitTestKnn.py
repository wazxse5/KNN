import unittest
import src.Knn


class TestKnn(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")

    def tearDown(self):
        print("tearDown")

    def testPredict(self):
        tab = [[4.4, 3.2, 1.3, 0.2, "Iris-setosa"], [4.9, 3.1, 1.5, 0.1, 'Iris-setosa'], [5, 1, 2, 3, 'Iris-virginica']]
        tab2 = [[4.4, 3.2, 1.3, 0.2], [4.9, 3.1, 1.5, 0.1]]
        knn = src.Knn.Knn(tab, 3)
        self.assertEqual(knn.predict(tab2), ['Iris-setosa', 'Iris-setosa'])

    def testScore(self):
        print("test Score")
        tab = ['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor',
               'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-virginica',
               'Iris-virginica', 'Iris-versicolor', 'Iris-virginica', 'Iris-virginica']
        # self.assertEqual(src.Knn.Knn.score(tab),Z)


if __name__ == '__main__':
    unittest.main()
