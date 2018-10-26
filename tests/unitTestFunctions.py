import unittest

import src.functions


class TestFunctions(unittest.TestCase):
    def setUp(self):
        print("\nsetUp")

    def tearDown(self):
        print("tearDown")

    def testRemove_labels_from(self):
        tab = [[4.4, 3.2, 1.3, 0.2, 'Iris-setosa'], [4.9, 3.1, 1.5, 0.1, 'Iris-setosa']]
        self.assertEqual(src.functions.remove_labels_from(tab), [[4.4, 3.2, 1.3, 0.2], [4.9, 3.1, 1.5, 0.1]])
        print("test remove_labels_from")

    def testRemove_data_from(self):
        tab = [[4.4, 3.2, 1.3, 0.2, 'Iris-setosa'], [4.9, 3.1, 1.5, 0.1, 'Iris-setosa']]
        self.assertEqual(src.functions.remove_data_from(tab), ['Iris-setosa', 'Iris-setosa'])
        print("test remove_data_from")

    def testChoose_best_match(self):
        tab = ['Iris-setosa', 'Iris-versicolor', 'Iris-versicolor', 'Iris-setosa', 'Iris-versicolor']
        self.assertEqual(src.functions.choose_best_match(tab), 'Iris-versicolor')
        print("test choose_best_match")

    def testTake2nd(self):
        tab = ['test_one', 'test_two']
        self.assertEqual(src.functions.take2nd(tab), 'test_two')
        print("test take2nd ")


if __name__ == '__main__':
    unittest.main()
