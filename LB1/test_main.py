import unittest
from main import sum_finder


# Тесты
class TestMath(unittest.TestCase):
    def test_sum_finder_zero(self):
        self.assertEqual(sum_finder([2,7,11,15], 9), [0,1])

    def test_sum_finderh_zero(self):
        self.assertEqual(sum_finder([3,2,4], 6), [1,2])

    def test_sum_findger_zero(self):
        self.assertEqual(sum_finder([3,3], 6), [0,1])

    def test_sum_finder_positive(self):
        self.assertEqual(sum_finder([2,3], 5), [0,1])

    def test_sum_finder_negative(self):
        self.assertEqual(sum_finder([-1, -3],-4), [0,1])

    def test_sum_finder_zkero(self):
        self.assertEqual(sum_finder([1,24,7], 5), None)

    def test_sum_finder(self):
        self.assertEqual(sum_finder([1], 5), None)


if __name__ == '__main__':
    unittest.main()