from random import randint

from dsapy.src.data_structures.queue import Queue


class QueueModel:
    def __init__(self):
        """
        Initializes a Queue.
        """
        self.__queue = Queue([4, 7, 1])

    def queue(self) -> list[int]:
        """
        Returns the queue as a python list.

        :return: Queue as python list.
        """
        queue = self.__queue.to_list()
        return queue

    def stats(self):
        """
        Returns a dictionary containing the queue status.\n
        Keys:
            - size
            - front

        :return: Python dictionary
        """
        front = 'Empty'
        if not self.__queue.empty():
            front = self.__queue.peek()

        return {
            'size': self.__queue.size(),
            'front': front,
        }

    def delete(self):
        """
        Deletes the queue, by creating a new empty Queue
        """
        self.__queue = Queue()

    def enqueue(self):
        """
        Enqueues a random integer to the queue.
        """
        self.__queue.enqueue(randint(0, 100))

    def dequeue(self):
        """
        If the queue is not empty, dequeues an item.
        """
        if not self.__queue.empty():
            self.__queue.dequeue()
