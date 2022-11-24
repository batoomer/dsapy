from typing import Any
import copy


class SinglyLinkedNode:
    """
    This class implements a Singly Linked Node. It has two attributes:
        - Data: Data of the Node
        - Next: Reference to another node
    """

    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __str__(self):
        """
        A String representation of the node
        :return: A String representation of the node
        """
        return f'Data: {self.data}, Next ID: {id(self.next)}'


class SinglyLinkedList:
    """
    This class is an Implementation of a Singly Linked List.\n
    The supported operations are:
        - empty
        - size
        - insert
        - delete
        - get
        - search
        - to_list
        - to_string
        - copy
    """
    # ---- Public Methods ----

    def __init__(self, data: list | None = None):
        """
        Initializes a Singly Linked List. If the data parameter is provided it initializes the linked list
        with the values in the data parameter. If it is not provided, an empty linked list will be initiated.

        :param data: List containing the values. Defaults to None
        """
        if not data:
            self.__head = None
            self.__item_count = 0
        else:

            # Set the linked list size to the size of the list
            self.__item_count = len(data)

            # Pop the last item and make it the head node
            node = SinglyLinkedNode(data.pop())
            self.__head = node

            # Pop the list until its empty and add the new data as a new node to the linked list
            while data:
                node = SinglyLinkedNode(data.pop())
                self.__insert_head(node)

    def __str__(self) -> str:
        """
        Returns the string representation of the Linked List.
            HEAD->[item1]->[item2]->...->[itemN]->NONE

        :return: String representation of the Linked List.
        """
        return self.to_string()

    def copy(self):
        """
        Returns a deep copy of the linked list

        :return: Deep copy of the linked list
        """
        return SinglyLinkedList(copy.deepcopy(self.to_list()))

    def to_string(self) -> str:
        """
        Transforms the Linked List to a string.
        HEAD->[item1]->[item2]->...->[itemN]->NONE

        :return: A String representing the Linked List
        """

        # Variable to hold the final result. Initialized with the HEAD-> pointer
        ll_string = 'HEAD->'

        # If the linked list is not empty, traverse and for each node add "node.data->" to the string
        if not self.empty():
            temp = self.__head
            while temp:
                ll_string += f'[{temp.data}]->'
                temp = temp.next

        # Add "NONE" to the string, indicating the end of the linked list
        ll_string += 'NONE'

        return ll_string

    def to_list(self) -> list:
        """
        Transforms the linked list to a python list.

        :return: Python list containing the values of the nodes
        """
        # Variable to hold the values of the linked list.
        ll_list = []

        # If linked list is not empty, traverse and for each node append its value to the list.
        if not self.empty():
            temp = self.__head
            while temp:
                ll_list.append(temp.data)
                temp = temp.next

        return ll_list

    def empty(self) -> bool:
        """
        Checks if the linked list is empty.

        :return: True if the linked list is empty, else false
        """
        # Linked List is empty if the head pointer is None
        return self.__head is None

    def size(self) -> int:
        """
        Returns the current size of the linked list.

        :return: size of the linked list.
        """
        return self.__item_count

    def insert(self, item: Any, position: int):
        """
        Inserts a new item to the linked list at the given position.\n
        Valid positions are -2 < x < size
            -  0: Insert at beginning
            - -1: Insert at end
            - x: Insert at the target position
        Note: (size-1) inserts at position (size-1) and not as the last item.
            e.g. a->b->c->d  => a->b->c->item->d

        :param item: item to insert
        :param position: position to insert to
        :raises IndexError: If position is out of range
        """

        # Check if the position is valid. If not raise IndexError
        if not self.__valid_position(position):
            raise IndexError('Position is out of range.')

        # Create a new node from the given item
        new_node = SinglyLinkedNode(item)

        # Insert according to the given position
        match position:
            case 0:  # Insert as new head node
                self.__insert_head(new_node)
            case -1:  # Insert as new tail node
                if self.empty():
                    self.__insert_head(new_node)
                else:
                    self.__insert(new_node, self.size() - 1)
            case _:  # Insert at the given position
                self.__insert(new_node, position - 1)

        self.__item_count += 1

    def delete(self, position: int):
        """
        Deletes and returns the item at the given position.

        :param position: Position to remove the item from
        :return: Removed item
        :raises IndexError: If position is out of range or linked list is empty
        """

        # Check if position is valid and the linked list is not empty. Else throw IndexError
        if not self.__valid_position(position) or self.empty():
            raise IndexError('Position is out of range.')

        # Variable to hold the deleted node
        deleted_node: SinglyLinkedNode
        # Delete according to the position
        match position:
            case 0:
                deleted_node = self.__delete_head()
            case -1:
                if self.size() == 1:
                    deleted_node = self.__delete_head()
                else:
                    deleted_node = self.__delete(self.size() - 1)
            case _:
                deleted_node = self.__delete(position)

        # Decrement the item count of the linked list
        self.__item_count -= 1

        # Return the deleted nodes data
        return deleted_node.data

    def get(self, position: int):
        """
        Returns the item at the given position
        :param position: Position of the item
        :return: Item at the given position
        :raises IndexError: If position is out of range or linked list is empty
        """

        # Check if position is valid and the linked list is not empty. Else throw IndexError
        if not self.__valid_position(position) or self.empty():
            raise IndexError('Position is out of range.')

        # Variable to hold the node to be returned
        target_node: SinglyLinkedNode
        # Get the node according to the position
        match position:
            case 0:  # Time Complexity O(1)
                target_node = self.__head
            case -1:  # Time Complexity O(n)
                if self.size() == 1:
                    target_node = self.__head
                else:
                    target_node = self.__traverse(self.size() - 1)
            case _:  # Time Complexity O(n)
                target_node = self.__traverse(position)

        # Return the data of the target node
        return target_node.data

    def search(self, item: Any) -> int | None:
        """
        Searches for an item in the linked list and returns the position of
        the first encounter.
        If the item is not found returns None, else it
        returns the position of the item.

        :param item: Item to search for
        :return: Position of the item if found, else None
        """

        # Position of the target item
        target_position = None

        # Traverse linked list and compare each node data with the target item
        temp = self.__head
        current_position = 0
        while temp:
            if temp.data == item:
                target_position = current_position
                break
            temp = temp.next
            current_position += 1

        return target_position

    # ---- Private Methods -----

    def __delete_head(self):
        """
        Removes the head node from the linked list and returns it.
        :return: Deleted Head Node

        Time Complexity: O(1)
        """
        deleted_node = self.__head
        self.__head = self.__head.next
        return deleted_node

    def __delete(self, position: int):
        """
        Removes the node at the given position and returns it.\n
        Time Complexity: O(n)

        :param position: Position of node to delete
        :return: Deleted node
        """
        # Traverse to the node before the given position
        target_node = self.__traverse(position - 1)
        deleted_node = target_node.next
        target_node.next = deleted_node.next
        return deleted_node

    def __insert_head(self, new_node: SinglyLinkedNode):
        """
        Inserts a new node to the beginning of the linked list.\n
        Time Complexity O(1)

        :param new_node: Node to insert
        """
        new_node.next = self.__head
        self.__head = new_node

    def __insert(self, new_node: SinglyLinkedNode, position: int):
        """
        Inserts a new node to the specified position in the Linked List.\n
        Time Complexity O(N)

        :param new_node: Node to insert
        :param position: Position to insert to
        """
        # Traverse to the node before the target position
        target_node = self.__traverse(position)

        new_node.next = target_node.next
        target_node.next = new_node

    def __valid_position(self, position: int) -> bool:
        """
        Checks if the position is in the desired range.

        :param position: position to check
        :return: True if position is valid, else false
        """
        return (-2 < position < self.size()) or position == 0

    def __traverse(self, position: int) -> SinglyLinkedNode:
        """
        Traverses the linked list and returns the node at the given position.

        :param position: Position to traverse to
        :return: Node at the given position.
        """
        temp = self.__head
        current_position = 0

        while temp:
            if position == current_position:
                break
            temp = temp.next
            current_position += 1

        return temp
