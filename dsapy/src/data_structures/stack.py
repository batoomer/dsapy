import copy
from typing import Any

from .singly_linked_list import SinglyLinkedList


class Stack:
    """
    This class implements a Stack data structure using a singly linked list.\n
    Supported Operations are:
        - empty
        - size
        - copy
        - to_string
        - to_list
        - push
        - pop
        - peek
    """

    def __init__(self, data: list | None = None):
        """
        Initializes a Stack with the given data. If the data is not provided, it will initialize
        an empty linked list.

        :param data: List to initialize the stack
        """

        self.__data = SinglyLinkedList(data)

    def __str__(self):
        """
        String Representation of the stack.
        :return: String Representation of the stack.
        """
        return self.to_string()

    def copy(self):
        """
        Returns a deep copy of the stack.
        :return: Deep copy of the stack
        """

        return Stack(copy.deepcopy(self.to_list()))

    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        :return: True if the stack is empty else false.
        """
        return self.__data.empty()

    def size(self) -> int:
        """
        Returns the current size of the stack.
        :return: The current size of the stack
        """
        return self.__data.size()

    def to_string(self) -> str:
        """
        Returns a string representation of the stack.\n
            TOP->[item1, item2, ..., itemN]

        :return: String representation of the stack
        """
        return f'TOP->{self.to_list()}'

    def to_list(self) -> list:
        """
        Transforms the stack to a python list.

        :return: Python list
        """
        return self.__data.to_list()

    def push(self, item):
        """
        Pushes an item to the stack.

        :param item: Item to push to the stack
        """
        self.__data.insert(item, 0)

    def pop(self) -> Any:
        """
        Pops an item from the stack.

        :return: The top item of the stack.
        :raise IndexError: If the stack is empty
        """
        if self.empty():
            raise IndexError('Stack is empty')
        return self.__data.delete(0)

    def peek(self) -> Any:
        """
        Peeks at the top element of the stack without removing it.

        :return: The top element of the stack
        """
        if self.empty():
            raise IndexError('Stack is empty')
        return self.__data.get(0)
