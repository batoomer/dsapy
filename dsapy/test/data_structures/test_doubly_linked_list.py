import unittest
from dsapy.src.data_structures.doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    # Test Copying Linked List
    def test_copy(self):
        with self.subTest('Empty List'):
            ll = DoublyLinkedList([])
            new_ll = ll.copy()
            self.assertNotEqual(ll, new_ll)

        with self.subTest('Deep Copy'):
            ll = DoublyLinkedList([[1, 2, 3, 4], [1, 2, 3, 4]])
            new_ll = ll.copy()
            self.assertEqual(ll.to_list(), new_ll.to_list())
            self.assertNotEqual(ll, ll.copy())
            self.assertNotEqual(id(ll.get(0)), id(new_ll.get(0)))
            self.assertNotEqual(id(ll.get(1)), id(new_ll.get(1)))

    # Test Searching of an item in the linked list
    def test_search(self):
        with self.subTest('Empty Linked List'):
            ll = DoublyLinkedList()
            self.assertEqual(ll.search('a'), None)
        with self.subTest('Single Item Encounter'):
            ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
            self.assertEqual(ll.search('a'), 0)
        with self.subTest('Multiple Item Encounter'):
            ll = DoublyLinkedList(['a', 'b', 'z', 'c', 'd', 'z', 'z', 'z', 'e'])
            self.assertEqual(ll.search('z'), 2)
        with self.subTest('Non Existing Item'):
            ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
            self.assertEqual(ll.search('z'), None)

    # Test Item Retrieval from the linked list
    def test_get(self):
        with self.subTest('Invalid Position'):
            ll = DoublyLinkedList(['a', 'b', 'c', 'd'])
            self.assertRaises(IndexError, ll.get, 5)
            self.assertRaises(IndexError, ll.get, -2)

        with self.subTest('Empty Linked List'):
            ll = DoublyLinkedList()
            self.assertRaises(IndexError, ll.get, 0)

        with self.subTest('Delete from head'):
            with self.subTest('Single Node'):
                ll = DoublyLinkedList(['a'])
                self.assertEqual(ll.get(0), 'a')
                self.assertEqual(ll.size(), 1)
                self.assertEqual(ll.to_list(), ['a'])

            with self.subTest('Many Nodes'):
                ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
                self.assertEqual(ll.get(0), 'a')
                self.assertEqual(ll.size(), 5)
                self.assertEqual(ll.to_list(), ['a', 'b', 'c', 'd', 'e'])

        with self.subTest('Delete from tail'):
            with self.subTest('Single Node'):
                ll = DoublyLinkedList(['a'])
                self.assertEqual(ll.get(-1), 'a')
                self.assertEqual(ll.size(), 1)
                self.assertEqual(ll.to_list(), ['a'])

            with self.subTest('Many Nodes'):
                ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
                self.assertEqual(ll.get(-1), 'e')
                self.assertEqual(ll.size(), 5)
                self.assertEqual(ll.to_list(), ['a', 'b', 'c', 'd', 'e'])

        with self.subTest('Delete from middle'):
            with self.subTest('Random Position'):
                ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
                self.assertEqual(ll.get(3), 'd')
                self.assertEqual(ll.size(), 5)
                self.assertEqual(ll.to_list(), ['a', 'b', 'c', 'd', 'e'])

            with self.subTest('Last Item'):
                ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
                self.assertEqual(ll.get(4), 'e')
                self.assertEqual(ll.size(), 5)
                self.assertEqual(ll.to_list(), ['a', 'b', 'c', 'd', 'e'])

    # Test Item Removal from the linked list
    def test_delete(self):
        with self.subTest('Invalid Position'):
            ll = DoublyLinkedList(['a', 'b', 'c', 'd'])
            self.assertRaises(IndexError, ll.delete, 5)
            self.assertRaises(IndexError, ll.delete, -2)

        with self.subTest('Empty Linked List'):
            ll = DoublyLinkedList()
            self.assertRaises(IndexError, ll.delete, 0)

        with self.subTest('Delete from head'):
            with self.subTest('Single Node'):
                ll = DoublyLinkedList(['a'])
                self.assertEqual(ll.delete(0), 'a')
                self.assertEqual(ll.size(), 0)
                self.assertEqual(ll.to_list(), [])

            with self.subTest('Many Nodes'):
                ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
                self.assertEqual(ll.delete(0), 'a')
                self.assertEqual(ll.size(), 4)
                self.assertEqual(ll.to_list(), ['b', 'c', 'd', 'e'])

        with self.subTest('Delete from tail'):
            with self.subTest('Single Node'):
                ll = DoublyLinkedList(['a'])
                self.assertEqual(ll.delete(-1), 'a')
                self.assertEqual(ll.size(), 0)
                self.assertEqual(ll.to_list(), [])

            with self.subTest('Many Nodes'):
                ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
                self.assertEqual(ll.delete(-1), 'e')
                self.assertEqual(ll.size(), 4)
                self.assertEqual(ll.to_list(), ['a', 'b', 'c', 'd'])

            with self.subTest('Delete from middle'):
                with self.subTest('Random Position'):
                    ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
                    self.assertEqual(ll.delete(3), 'd')
                    self.assertEqual(ll.size(), 4)
                    self.assertEqual(ll.to_list(), ['a', 'b', 'c', 'e'])

                with self.subTest('Last Item'):
                    ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e'])
                    self.assertEqual(ll.delete(4), 'e')
                    self.assertEqual(ll.size(), 4)
                    self.assertEqual(ll.to_list(), ['a', 'b', 'c', 'd'])

    # Test Item Insertion to the linked list
    def test_insert(self):
        with self.subTest('Invalid Position'):
            ll = DoublyLinkedList(['a', 'b', 'c', 'd'])
            self.assertRaises(IndexError, ll.insert, 'z', 5)
            self.assertRaises(IndexError, ll.insert, 'z', -2)

        with self.subTest('Insert to head'):
            with self.subTest('Empty Linked List'):
                ll = DoublyLinkedList()
                ll.insert('a', 0)
                self.assertEqual(['a'], ll.to_list())
                self.assertEqual(1, ll.size())

            with self.subTest('Single Node'):
                ll = DoublyLinkedList(['b'])
                ll.insert('a', 0)
                self.assertEqual(['a', 'b'], ll.to_list())
                self.assertEqual(2, ll.size())

            with self.subTest('Non-Empty Linked List'):
                ll = DoublyLinkedList(['a', 'b', 'c', 'd'])
                ll.insert('z', 0)
                self.assertEqual(['z', 'a', 'b', 'c', 'd'], ll.to_list())
                self.assertEqual(5, ll.size())

        with self.subTest('Insert to tail'):
            with self.subTest('Empty Linked List'):
                ll = DoublyLinkedList()
                ll.insert('a', -1)
                self.assertEqual(['a'], ll.to_list())
                self.assertEqual(1, ll.size())

            with self.subTest('Single Node'):
                ll = DoublyLinkedList(['b'])
                ll.insert('a', -1)
                self.assertEqual(['b', 'a'], ll.to_list())
                self.assertEqual(2, ll.size())

            with self.subTest('Non-Empty Linked List'):
                ll = DoublyLinkedList(['a', 'b', 'c', 'd'])
                ll.insert('z', -1)
                self.assertEqual(['a', 'b', 'c', 'd', 'z'], ll.to_list())
                self.assertEqual(5, ll.size())

        with self.subTest('Insert to middle'):
            with self.subTest('Two Nodes'):
                ll = DoublyLinkedList(['a', 'b'])
                ll.insert('z', ll.size() - 1)
                self.assertEqual(['a', 'z', 'b'], ll.to_list())
                self.assertEqual(3, ll.size())

            with self.subTest('Many Nodes'):
                ll = DoublyLinkedList(['a', 'b', 'c', 'd', 'e', 'f'])
                ll.insert('z', 3)
                self.assertEqual(['a', 'b', 'c', 'z', 'd', 'e', 'f'], ll.to_list())
                self.assertEqual(7, ll.size())

    # Test Initialization of the linked list
    def test_initialization(self):
        with self.subTest('Initialize Empty Linked List'):
            ll = DoublyLinkedList()
            self.assertEqual(0, ll.size())
            self.assertEqual(True, ll.empty())
            self.assertEqual('HEAD/NONE<->NONE/TAIL', ll.to_string())
            self.assertEqual([], ll.to_list())

        with self.subTest('Initialize from a list'):
            ll = DoublyLinkedList(['a', 'b', 'c', 'd'])
            self.assertEqual(4, ll.size())
            self.assertEqual(False, ll.empty())
            self.assertEqual('HEAD/NONE<->[a]<->[b]<->[c]<->[d]<->NONE/TAIL', ll.to_string())
            self.assertEqual(['a', 'b', 'c', 'd'], ll.to_list())


if __name__ == '__main__':
    unittest.main()
