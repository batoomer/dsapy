import random
from .sorting_config import SIZE_CONFIG, ALGORITHM_CONFIG
from ...src.algorithms.sorting.bubble_sort import BubbleSort
from ...src.algorithms.sorting.insertion_sort import InsertionSort
from ...src.algorithms.sorting.quick_sort import QuickSort
from ...src.algorithms.sorting.selection_sort import SelectionSort


class SortingModel:

    def __init__(self):
        self.__size = SIZE_CONFIG['init_val']
        self.__data = [random.randint(10, 1000) for _ in range(self.__size)]

        self.__animations = {}
        self.__metadata = {}

    def data(self) -> list:
        """
        Returns the data of the model.

        :return: the data
        """
        return self.__data

    def shuffle(self):
        """
        Creates new random data of the same size.
        """
        self.__data = [random.randint(10, 1000) for _ in range(self.__size)]

    def set_size(self, val: int):
        """
        Changes the size of the data and creates new random data.

        :param val: new size of the data
        """
        self.__size = val
        self.__data = [random.randint(10, 1000) for _ in range(self.__size)]

    def sort(self, algorithm):
        """
        Generates sorting animation and metadata for the input algorithm
        """
        sorter = self.__select_algorithm(algorithm)
        sorter.sort(self.__data)
        self.__animations = sorter.animation()
        self.__metadata = sorter.metadata()

    def swap(self, i: int, j: int):
        """
        Swaps two items of the data.

        :param i: first item
        :param j: second item
        """
        self.__data[i], self.__data[j] = self.__data[j], self.__data[i]

    def get_animation(self) -> list | None:
        """
        Returns the first element of the swap animation.
        If the animation is empty returns null

        :return: List containing the swapped indices or None.
        """
        if self.__animations['swap']:
            return self.__animations['swap'].pop(0)
        else:
            return None

    def get_metadata(self) -> dict:
        """
        Returns the metadata.

        :return: Dictionary containing the metadata
        """
        return self.__metadata

    @staticmethod
    def __select_algorithm(algorithm: str) -> BubbleSort | InsertionSort | SelectionSort | QuickSort:
        """
        Returns the sorter object according to the algorithm input

        :param algorithm: algorithm name
        :return: Sorter object
        """
        match algorithm:
            case 'Bubble Sort':
                return BubbleSort()
            case 'Insertion Sort':
                return InsertionSort()
            case 'Selection Sort':
                return SelectionSort()
            case 'Quick Sort':
                return QuickSort()
            case _:
                raise ValueError('Unexpected Algorithm')

