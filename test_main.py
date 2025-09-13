import unittest
from main import sum_finder

# Функция, которую будем тестировать
def sum_finder(a, b):
    return a + b

# Тесты
class TestMath(unittest.TestCase):
    def test_sum_finder_positive(self):
        self.assertEqual(sum_finder(2, 3), 5)

    def test_sum_finder_negative(self):
        self.assertEqual(sum_finder(-1, -3), -4)

    def test_sum_finder_zero(self):
        self.assertEqual(sum_finder(0, 5), 5)

if __name__ == '__main__':
    unittest.main()