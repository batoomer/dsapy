import random
from string import ascii_lowercase, digits
import unittest
from dsapy.src.algorithms.sorting.bubble_sort import BubbleSort


class TestBubbleSort(unittest.TestCase):
    def test_sort_string(self):
        chars = ascii_lowercase + digits
        data = [''.join(random.choice(chars) for _ in range(10)) for _ in range(1000)]

        sorter = BubbleSort()
        sorted_data = sorter.sort(data)
        self.assertNotEqual(id(data), id(sorted_data))
        self.assertEqual(sorted(data), sorted_data)

    def test_sort_float(self):
        data = [round(random.uniform(-1000, 1000), 2) for _ in range(1000)]

        sorter = BubbleSort()
        sorted_data = sorter.sort(data)
        self.assertNotEqual(id(data), id(sorted_data))
        self.assertEqual(sorted(data), sorted_data)

    def test_sort_integers(self):
        data = [random.randint(-100, 100) for _ in range(1000)]

        sorter = BubbleSort()
        sorted_data = sorter.sort(data)
        self.assertNotEqual(id(data), id(sorted_data))
        self.assertEqual(sorted(data), sorted_data)
        print(sorter.metadata())
        print(len(sorter.animation()['swap']))


if __name__ == '__main__':
    unittest.main()
