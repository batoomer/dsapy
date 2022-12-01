from abc import ABC, abstractmethod
from time import process_time
from dsapy.src.data_structures.queue import Queue


class SortingAlgorithm(ABC):
    def __init__(self):
        """
        Initializes properties
        """
        self.__stop_time = None
        self.__start_time = None
        self.__metadata = {}
        self.__animations = {}

    def _reset_metadata_animations(self):
        """
        Resets the metadata and animations attributes
        """
        self.__metadata = {
            'swap_count': 0,
            'comparison_count': 0,
            'iteration_count': 0,
            'runtime': 0.0,
        }

        self.__animations = {
            'swap': Queue(),
        }

    def _add_swap(self, seq: list[int]):
        """
        Adds a list of animation to the animation attributes and increments the swap count metadata.

        :param seq: list of indices
        """
        self.__metadata['swap_count'] += 1
        self.__animations['swap'].enqueue(seq)

    def _add_comparison(self):
        """
        Increments the comparison count metadata.
        """
        self.__metadata['comparison_count'] += 1

    def _add_iteration(self):
        """
        Increments the iteration count metadata
        """
        self.__metadata['iteration_count'] += 1

    def _add_runtime(self):
        """
        Add the runtime metadata.
        Note: _start_runtime and _stop_runtime must run before this function
        """
        self.__metadata['runtime'] = round(1000 * (self.__stop_time - self.__start_time), 2)

    def _start_runtime(self):
        """
        Adds a starting time
        :return:
        """
        self.__start_time = process_time()

    def _stop_runtime(self):
        """
        Adds an ending time
        """
        self.__stop_time = process_time()

    def metadata(self):
        """
        Returns the metadata

        Keys:
        - 'swap_count',
        - 'comparison_count'
        - 'iteration_count'
        - 'runtime'

        :return: Dictionary containing the metadata.
        """
        return self.__metadata

    def animation(self):
        """
        Returns the animations
        :return:
        """
        return self.__animations

    @abstractmethod
    def sort(self, data: list[int | float | str]) -> list[int | float | str]:
        pass
