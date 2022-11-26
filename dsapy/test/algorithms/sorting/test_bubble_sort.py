import random
from string import ascii_lowercase, digits
import unittest
from dsapy.src.algorithms.sorting.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_sort_string(self):
        chars = ascii_lowercase + digits
        arr = [''.join(random.choice(chars) for _ in range(10)) for _ in range(1000)]

        sorted_arr = bubble_sort(arr)
        self.assertNotEqual(id(arr), id(sorted_arr))
        self.assertEqual(sorted(arr), sorted_arr)

    def test_sort_float(self):
        arr = [round(random.uniform(-1000, 1000), 2) for _ in range(1000)]

        sorted_arr = bubble_sort(arr)
        self.assertNotEqual(id(arr), id(sorted_arr))
        self.assertEqual(sorted(arr), sorted_arr)

    def test_sort_integers(self):
        arr = [random.randint(-100, 100) for _ in range(1000)]

        sorted_arr = bubble_sort(arr)
        self.assertNotEqual(id(arr), id(sorted_arr))
        self.assertEqual(sorted(arr), sorted_arr)


if __name__ == '__main__':
    unittest.main()
