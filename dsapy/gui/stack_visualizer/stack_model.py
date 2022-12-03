import random

from dsapy.src.data_structures.stack import Stack


class StackModel:
    def __init__(self):
        """
        Initializes the StackModel by initializing a stack
        """
        self.__stack = Stack([4, 7, 1])

    def stack(self) -> list[int]:
        """
        Returns the stack as a python list.

        :return: stack as a python list.
        """
        # convert the stack to a list
        data = self.__stack.to_list()
        # reverse the list such that the last index is the top element
        data.reverse()
        return data

    def push(self):
        """
        Pushes a random integer onto the stack
        """
        self.__stack.push(random.randint(0, 100))

    def pop(self):
        """
        If the stack is not empty pops an item
        """
        if not self.__stack.empty():
            self.__stack.pop()

    def delete(self):
        """
        Deletes the stack by replacing it with a new empty stack.
        """
        self.__stack = Stack()

    def stats(self) -> dict:
        """
        Returns a dictionary containing the stack status.\n
        Keys:
            - size
            - top

        :return: Python dictionary
        """
        top = 'Empty'
        if not self.__stack.empty():
            top = self.__stack.peek()

        return {
            'size': self.__stack.size(),
            'top': top
        }
