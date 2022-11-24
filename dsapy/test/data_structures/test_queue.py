import unittest
from dsapy.src.data_structures.queue import Queue


class TestStack(unittest.TestCase):

    def test_copy(self):
        with self.subTest('Empty List'):
            q = Queue([])
            new_q = q.copy()
            self.assertNotEqual(q, new_q)

        with self.subTest('Deep Copy'):
            q = Queue([[1, 2, 3, 4], [1, 2, 3, 4]])
            new_q = q.copy()
            self.assertEqual(q.to_list(), new_q.to_list())
            self.assertNotEqual(q, q.copy())
            self.assertNotEqual(id(q.dequeue()), id(new_q.dequeue()))
            self.assertNotEqual(id(q.dequeue()), id(new_q.dequeue))

    def test_peek(self):
        with self.subTest('Empty Queue'):
            q = Queue()
            self.assertRaises(IndexError, q.peek)

        with self.subTest('Non Empty Queue'):
            q = Queue([4, 3, 2, 9])
            self.assertEqual(q.peek(), 4)
            self.assertEqual(q.size(), 4)
            self.assertEqual(q.to_list(), [4, 3, 2, 9])

        with self.subTest('Enqueue Dequeue Peek Enqueue Peek'):
            q = Queue([4, 3, 2, 9])
            q.enqueue(0)
            q.dequeue()
            self.assertEqual(q.peek(), 3)
            q.enqueue(7)
            self.assertEqual(q.peek(), 3)
            self.assertEqual(q.size(), 5)
            self.assertEqual(q.to_list(), [3, 2, 9, 0, 7])

    def test_dequeue(self):
        with self.subTest('Empty queue'):
            q = Queue()
            self.assertRaises(IndexError, q.dequeue)

        with self.subTest('Non Empty Queue'):
            q = Queue([4, 3, 2, 9])
            self.assertEqual(q.dequeue(), 4)
            self.assertEqual(q.size(), 3)
            self.assertEqual(q.to_list(), [3, 2, 9])

        with self.subTest('Enqueue Dequeue Dequeue Enqueue Dequeue'):
            q = Queue([4, 3, 2, 9])
            q.enqueue(0)
            self.assertEqual(q.dequeue(), 4)
            self.assertEqual(q.dequeue(), 3)
            q.enqueue(7)
            self.assertEqual(q.dequeue(), 2)
            self.assertEqual(q.size(), 3)
            self.assertEqual(q.to_list(), [9, 0, 7])

    def test_enqueue(self):
        with self.subTest('Empty Queue'):
            q = Queue()
            q.enqueue(1)
            self.assertEqual(q.size(), 1)
            self.assertEqual(q.to_list(), [1])

        with self.subTest('Non Empty Queue'):
            q = Queue([4, 3, 2, 9])
            q.enqueue(1)
            self.assertEqual(q.size(), 5)
            self.assertEqual(q.to_list(), [4, 3, 2, 9, 1])

    def test_initialization(self):
        with self.subTest('Empty Queue'):
            q = Queue()
            self.assertEqual(q.size(), 0)
            self.assertEqual(q.empty(), True)
            self.assertEqual(q.to_list(), [])
            self.assertEqual(q.to_string(), 'FRONT<-[]<-REAR')
        with self.subTest('Queue from list'):
            q = Queue([1, 2, 3, 4, 5])
            self.assertEqual(q.size(), 5)
            self.assertEqual(q.empty(), False)
            self.assertEqual(q.to_list(), [1, 2, 3, 4, 5])
            self.assertEqual(q.to_string(), 'FRONT<-[1, 2, 3, 4, 5]<-REAR')


if __name__ == '__main__':
    unittest.main()
