import unittest
from main2 import guess_number


class TestGuessNumberSimplified(unittest.TestCase):

    def test_1(self):
        result = guess_number([1, 3, 5, 7, 9], 5, "bin")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 5)

    def test_2(self):
        result = guess_number([10, 20, 30, 40, 50], 10, "bin")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 10)

    def test_3(self):
        result = guess_number([2, 4, 6, 8, 10, 12], 12, "bin")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 12)

    def test_4(self):
        result = guess_number([1, 2, 3], 5, "bin")
        self.assertIsNone(result)

    def test_5(self):
        result = guess_number([], 5, "bin")
        self.assertIsNone(result)

    def test_6(self):
        result = guess_number(range(10, 0, -1), 3, "bin")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 3)

    def test_7(self):
        result = guess_number(range(1, 1000001), 999999, "bin")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 999999)

    def test_8(self):
        result = guess_number([100, 200, 300, 400], 300, "seq")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 300)

    def test_9(self):
        result = guess_number([9, 3, 7, 1, 5], 5, "seq")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 5)

    def test_10(self):
        result = guess_number([15, 3, 8, 20, 1], 20, "seq")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 20)

    def test_11(self):
        result = guess_number([1, 2, 3, 4, 5], 10, "seq")
        self.assertIsNone(result)

    def test_12(self):
        result = guess_number([], 10, "seq")
        self.assertIsNone(result)

    def test_13(self):
        result = guess_number([-10, -5, 0, 5, 10], -5, "bin")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], -5)

    def test_14(self):
        result = guess_number([0], 0, "bin")
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 0)

    def test_15(self):
        result = guess_number([42], 13, "seq")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
