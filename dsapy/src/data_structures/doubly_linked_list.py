import copy
from typing import Any


class DoublyLinkedNode:
    """
    This class implements a Doubly Linked Node. It has three attributes:
        - Data: Data of the Node
        - Next: Reference to another node
        - Prev: Reference to another node
    """

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        """
        A String representation of the node
        :return: A String representation of the node
        """
        return f'Data: {self.data}, Next ID: {id(self.next)}, Prev ID {id(self.prev)}'


class DoublyLinkedList:
    """
    This class is an Implementation of a Doubly Linked List.\n
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
        Initializes a Doubly Linked List. If the data parameter is provided it initializes the linked list
        with the values in the data parameter. If it is not provided, an empty linked list will be initiated.

        :param data: List containing the values. Defaults to None
        """
        if not data:
            self.__head = None
            self.__tail = None
            self.__item_count = 0
        else:
            # Set the linked list size to the size of the list
            self.__item_count = len(data)

            # Pop the last item and make it the head and tail node
            node = DoublyLinkedNode(data.pop())
            self.__head = node
            self.__tail = node

            # Pop the list until its empty and add the new data as a new node to the linked list
            while data:
                node = DoublyLinkedNode(data.pop())
                node.next = self.__head
                self.__head.prev = node
                self.__head = node

    def __str__(self):
        """
        A String representation of the linked list

        :return: String Representation of the linked list
        """
        return self.to_string()

    def copy(self):
        """
        Returns a deep copy of the linked list

        :return: Deep copy of the linked list
        """
        return DoublyLinkedList(copy.deepcopy(self.to_list()))

    def to_string(self) -> str:
        """
        Transforms the Linked List to a string.
        HEAD/NONE<->[item1]<->[item2]<->...<->[itemN]<->NONE/TAIL

        :return: A String representing the Linked List
        """

        # Variable to hold the final result. Initialized with the HEAD-> pointer
        ll_string = 'HEAD/NONE<->'

        # If the linked list is not empty, traverse and for each node add "node.data->" to the string
        if not self.empty():
            temp = self.__head
            while temp:
                ll_string += f'[{temp.data}]<->'
                temp = temp.next

        # Add "NONE" to the string, indicating the end of the linked list
        ll_string += 'NONE/TAIL'

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
            e.g. a<->b<->c<->d  => a<->b<->c<->item<->d

        :param item: item to insert
        :param position: position to insert to
        :raises IndexError: If position is out of range
        """

        # Check if the position is valid. If not raise IndexError
        if not self.__valid_position(position):
            raise IndexError('Position is out of range.')

        # Create a new Doubly Linked Node from the item
        new_node = DoublyLinkedNode(item)
        # Insert according to the position
        match position:
            case 0:  # Time complexity O(1)
                self.__insert_head(new_node)
            case -1:  # Time complexity O(1)
                self.__insert_tail(new_node)
            case _:  # Time complexity O(n)
                self.__insert(new_node, position)

        # Increment the linked list item count
        self.__item_count += 1

    def delete(self, position: int) -> Any:
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
        deleted_node: DoublyLinkedNode
        # Delete according to the position
        match position:
            case 0:  # Time complexity O(1)
                deleted_node = self.__delete_head()
            case -1:  # Time complexity O(1)
                deleted_node = self.__delete_tail()
            case _:
                if position == self.size() - 1:  # Time complexity O(1)
                    deleted_node = self.__delete_tail()
                else:  # Time complexity O(n)
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
        target_node: DoublyLinkedNode
        # Get the node according to the position
        match position:
            case 0:  # Time Complexity O(1)
                target_node = self.__head
            case -1:  # Time Complexity O(1)
                target_node = self.__tail
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

    # ---- Private Methods ----

    def __delete(self, position: int):
        """
        Deletes and returns the node at the given position

        :param position: Position of the node to remove
        :return: Removed Node
        """
        deleted_node = self.__traverse(position)
        deleted_node.prev.next = deleted_node.next
        deleted_node.next.prev = deleted_node.prev
        return deleted_node

    def __delete_tail(self):
        """
        Deletes and returns the tail node.

        :return: Removed tail node
        """
        deleted_node = self.__tail
        if self.size() == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__tail.prev.next = None
            self.__tail = self.__tail.prev
        return deleted_node

    def __delete_head(self):
        """
        Deletes and returns the head node.

        :return: Removed head node
        """
        deleted_node = self.__head
        if self.size() == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None
        return deleted_node

    def __insert(self, new_node: DoublyLinkedNode, position: int):
        """
        Insert a new node at the given position.

        :param new_node: Node to insert
        :param position: Position to insert to
        """
        # Traverse to the node before the given position
        target_node = self.__traverse(position - 1)

        # Connect the pointers
        new_node.next = target_node.next
        new_node.prev = target_node
        target_node.next.prev = new_node
        target_node.next = new_node

    def __insert_tail(self, new_node: DoublyLinkedNode):
        """
        Inserts a new node as the tail node of the linked list.

        :param new_node: Node to insert
        """

        if self.size() == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node

    def __insert_head(self, new_node: DoublyLinkedNode):
        """
        Inserts a new node as the head node of the linked list.

        :param new_node: Node to insert
        """
        if self.size() == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

    def __valid_position(self, position: int) -> bool:
        """
        Checks if the position is in the desired range.

        :param position: position to check
        :return: True if position is valid, else false
        """
        return (-2 < position < self.size()) or position == 0

    def __traverse(self, position: int) -> DoublyLinkedNode:
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