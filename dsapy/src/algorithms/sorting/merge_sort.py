from math import floor

from dsapy.src.algorithms.sorting.sorting_algorithm import SortingAlgorithm


class MergeSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()

    def sort(self, data: list[int | float | str]) -> list[int | float | str]:
        """
        This function is an implementation of the merge sort algorithm.
        It sorts the list in ascending order.
        It returns a sorted copy of the input list.

        :param data: list to be sorted
        :return: sorted copy of input list
        """
        # Initiate/Reset the metadata and animations
        self._reset_metadata_animations()

        # Copy the input to a new list
        data = data.copy()

        # CPU start time of the sorting algorithm
        self._start_runtime()

        self.__merge_sort(data, 0, len(data) - 1)

        # CPU end time of the sorting algorithm
        self._stop_runtime()
        self._add_runtime()

        # Return the sorted array
        return data

    def __merge_sort(self, data, left: int, right: int):
        if left < right:
            middle = floor((left + right) / 2)

            self.__merge_sort(data, left, middle)
            self.__merge_sort(data, middle + 1, right)
            self.__merge(data, left, middle, right)

    def __merge(self, data, left: int, middle: int, right: int):
        """
        It's not merge sort but it produces the merge sort pattern.
        """

        i = left
        while i <= middle:
            self._add_iteration()
            j = right
            while j > middle:
                self._add_iteration()
                self._add_comparison()
                if data[i] > data[j]:
                    data[i], data[j] = data[j], data[i]
                    self._add_swap([i, j])
                j -= 1
            i += 1