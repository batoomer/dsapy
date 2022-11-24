import unittest
from dsapy.src.data_structures.stack import Stack


class TestStack(unittest.TestCase):

    def test_copy(self):
        with self.subTest('Empty List'):
            s = Stack([])
            new_s = s.copy()
            self.assertNotEqual(s, new_s)

        with self.subTest('Deep Copy'):
            s = Stack([[1, 2, 3, 4], [1, 2, 3, 4]])
            new_s = s.copy()
            self.assertEqual(s.to_list(), new_s.to_list())
            self.assertNotEqual(s, s.copy())
            self.assertNotEqual(id(s.pop()), id(new_s.pop()))
            self.assertNotEqual(id(s.pop()), id(new_s.pop()))

    def test_peek(self):
        with self.subTest('Empty Stack'):
            s = Stack()
            self.assertRaises(IndexError, s.peek)

        with self.subTest('Non Empty Stack'):
            s = Stack([4, 3, 2, 9])
            self.assertEqual(s.peek(), 4)
            self.assertEqual(s.size(), 4)
            self.assertEqual(s.to_list(), [4, 3, 2, 9])

        with self.subTest('Push Pop Peek Push Peek'):
            s = Stack([4, 3, 2, 9])
            s.push(0)
            s.pop()
            self.assertEqual(s.peek(), 4)
            s.push(7)
            self.assertEqual(s.peek(), 7)
            self.assertEqual(s.size(), 5)
            self.assertEqual(s.to_list(), [7, 4, 3, 2, 9])

    def test_pop(self):
        with self.subTest('Empty Stack'):
            s = Stack()
            self.assertRaises(IndexError, s.pop)

        with self.subTest('Non Empty Stack'):
            s = Stack([4, 3, 2, 9])
            self.assertEqual(s.pop(), 4)
            self.assertEqual(s.size(), 3)
            self.assertEqual(s.to_list(), [3, 2, 9])

        with self.subTest('Push Pop Pop Push Pop'):
            s = Stack([4, 3, 2, 9])
            s.push(0)
            self.assertEqual(s.pop(), 0)
            self.assertEqual(s.pop(), 4)
            s.push(7)
            self.assertEqual(s.pop(), 7)
            self.assertEqual(s.size(), 3)
            self.assertEqual(s.to_list(), [3, 2, 9])

    def test_push(self):
        with self.subTest('Empty Stack'):
            s = Stack()
            s.push(1)
            self.assertEqual(s.size(), 1)
            self.assertEqual(s.to_list(), [1])

        with self.subTest('Non Empty Stack'):
            s = Stack([4, 3, 2, 9])
            s.push(1)
            self.assertEqual(s.size(), 5)
            self.assertEqual(s.to_list(), [1, 4, 3, 2, 9])

    def test_initialization(self):
        with self.subTest('Empty Stack'):
            s = Stack()
            self.assertEqual(s.size(), 0)
            self.assertEqual(s.empty(), True)
            self.assertEqual(s.to_list(), [])
            self.assertEqual(s.to_string(), 'TOP->[]')
        with self.subTest('Stack from list'):
            s = Stack([1, 2, 3, 4, 5])
            self.assertEqual(s.size(), 5)
            self.assertEqual(s.empty(), False)
            self.assertEqual(s.to_list(), [1, 2, 3, 4, 5])
            self.assertEqual(s.to_string(), 'TOP->[1, 2, 3, 4, 5]')


if __name__ == '__main__':
    unittest.main()
