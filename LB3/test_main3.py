import unittest
from main3 import gen_bin_tree


class TestBinaryTree(unittest.TestCase):

    # ===== Базовые случаи =====

    def test_height_0(self):
        self.assertEqual(gen_bin_tree(0, 9), {"9": []})

    def test_height_1(self):
        self.assertEqual(
            gen_bin_tree(1, 9),
            {"9": [{"19": []}, {"17": []}]}
        )

    def test_height_2_structure(self):
        tree = gen_bin_tree(2, 9)
        self.assertIn("9", tree)
        self.assertEqual(len(tree["9"]), 2)

    # ===== Проверка значений =====

    def test_left_right_values(self):
        tree = gen_bin_tree(1, 9)
        left = tree["9"][0]
        right = tree["9"][1]

        self.assertIn("19", left)
        self.assertIn("17", right)

    def test_height_2_values(self):
        tree = gen_bin_tree(2, 9)
        left_subtree = tree["9"][0]
        self.assertIn("19", left_subtree)

        left_left = left_subtree["19"][0]
        self.assertIn("39", left_left)  # 19 * 2 + 1

    # ===== Переопределение функций =====

    def test_custom_functions(self):
        tree = gen_bin_tree(
            1,
            5,
            l_b=lambda x: x + 1,
            r_b=lambda x: x ** 2
        )
        self.assertEqual(
            tree,
            {"5": [{"6": []}, {"25": []}]}
        )

    def test_custom_only_left(self):
        tree = gen_bin_tree(
            1,
            3,
            l_b=lambda x: x + 10
        )
        self.assertIn("13", tree["3"][0])

    def test_custom_only_right(self):
        tree = gen_bin_tree(
            1,
            4,
            r_b=lambda x: x * 10
        )
        self.assertIn("40", tree["4"][1])

    # ===== Граничные случаи =====

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            gen_bin_tree(-1, 9)

    def test_zero_root(self):
        tree = gen_bin_tree(1, 0)
        self.assertIn("0", tree)

    def test_large_root(self):
        tree = gen_bin_tree(1, 1000)
        self.assertIn("2001", tree["1000"][0])

    # ===== Типы =====

    def test_keys_are_strings(self):
        tree = gen_bin_tree(1, 9)
        for key in tree.keys():
            self.assertIsInstance(key, str)


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
