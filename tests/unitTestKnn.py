import unittest
import src.knn


class TestKnn(unittest.TestCase):
    def setUp(self):
        print("\ntestSetUp")

    def tearDown(self):
        print("testComplete")

    def testPredict(self):
        print("     testPredict")
        tab = [[4.4, 3.2, 1.3, 0.2, "Iris-setosa"], [4.9, 3.1, 1.5, 0.1, 'Iris-setosa'], [5, 1, 2, 3, 'Iris-virginica']]
        tab2 = [[4.4, 3.2, 1.3, 0.2], [4.9, 3.1, 1.5, 0.1]]
        knn = src.knn.Knn(tab, 3)
        self.assertEqual(knn.predict(tab2), ['Iris-setosa', 'Iris-setosa'])

    def testScore(self):
        print("     testScore")
        tab = ['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor']
        tab2 = [[5.1, 3.5, 1.4, 0.2, 'Iris-setosa'], [4.9, 3.0, 1.4, 0.2, 'Iris-setosa'],
                [6.5, 2.8, 4.6, 1.5, 'Iris-versicolor'], [5.7, 2.8, 4.5, 1.3, 'Iris-versicolor']]
        knn = src.knn.Knn(tab, 3)
        self.assertEqual(knn.score(tab2, tab), 0.75)


if __name__ == '__main__':
    unittest.main()
