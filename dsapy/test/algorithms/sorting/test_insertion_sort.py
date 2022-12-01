import random
from string import ascii_lowercase, digits
import unittest
from dsapy.src.algorithms.sorting.insertion_sort import InsertionSort


class TestBubbleSort(unittest.TestCase):
    sorter = InsertionSort()

    def test_sort_string(self):
        chars = ascii_lowercase + digits
        data = [''.join(random.choice(chars) for _ in range(10)) for _ in range(1000)]

        sorted_data = self.sorter.sort(data)
        self.assertNotEqual(id(data), id(sorted_data))
        self.assertEqual(sorted(data), sorted_data)

    def test_sort_float(self):
        data = [round(random.uniform(-1000, 1000), 2) for _ in range(1000)]

        sorted_data = self.sorter.sort(data)
        self.assertNotEqual(id(data), id(sorted_data))
        self.assertEqual(sorted(data), sorted_data)

    def test_sort_integers(self):
        data = [random.randint(-100, 100) for _ in range(1000)]

        sorted_data = self.sorter.sort(data)
        self.assertNotEqual(id(data), id(sorted_data))
        self.assertEqual(sorted(data), sorted_data)


if __name__ == '__main__':
    unittest.main()
