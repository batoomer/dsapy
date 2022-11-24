import copy
from typing import Any

from .doubly_linked_list import DoublyLinkedList


class Queue:

    def __init__(self, data: list | None = None):
        """
        Initializes a Queue from the given data. If the data is not provided, an empty
        Queue will be initiated.

        :param data: list containing the data to initialize the queue. Defaults to None
        """
        self.__data = DoublyLinkedList(data)

    def __str__(self):
        """
        String Representation of the Queue.
        :return: String Representation of the Queue.
        """
        return self.to_string()

    def copy(self):
        """
        Returns a deep copy of the Queue.
        :return:
        """
        return Queue(copy.deepcopy(self.to_list()))

    def to_list(self) -> list:
        """
        Transforms the Queue to a Python List.

        :return: Python List consisting of the Queue data.
        """
        return self.__data.to_list()

    def to_string(self) -> str:
        """
        Transforms the Queue to a string.\n
            FRONT<-[item1, item2, ..., itemN]<-REAR

        :return: String representing the Queue
        """
        return f'FRONT<-{self.__data.to_list()}<-REAR'

    def empty(self) -> bool:
        """
        Checks if the queue is empty.

        :return: True if queue is empty, else false.
        """
        return self.__data.empty()

    def size(self) -> int:
        """
        Returns the current size of the Queue.

        :return: The current size of the Queue
        """
        return self.__data.size()

    def enqueue(self, item: Any):
        """
        Enqueues an item to the Queue.

        :param item: Item to enqueue.
        """
        self.__data.insert(item, -1)

    def dequeue(self):
        """
        Dequeues an item from the Queue.

        :return: The Front item of the queue.
        :raise IndexError: If queue is empty.
        """
        if self.empty():
            raise IndexError('Queue is empty')
        return self.__data.delete(0)

    def peek(self):
        """
        Peeks at the Front item of the Queue.

        :return: The front item of the queue without removing it.
        :raise IndexError: If queue is empty.
        """
        if self.empty():
            raise IndexError('Queue is empty')
        return self.__data.get(0)
