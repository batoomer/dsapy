import math

from dsapy.src.algorithms.sorting.sorting_algorithm import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    def __init__(self):
        """
        Initializes the base abstract class SortingAlgorithm
        """
        super().__init__()

    def sort(self, data: list[int | float | str]) -> list[int | float | str]:
        # Initiate/Reset the metadata and animations
        self._reset_metadata_animations()

        # Copy the input to a new list
        data = data.copy()

        # CPU start time of the sorting algorithm
        self._start_runtime()

        self.__quick_sort(data, 0, len(data) - 1)

        # CPU end time of the sorting algorithm
        self._stop_runtime()
        self._add_runtime()

        # Return the sorted array
        return data

    def __quick_sort(self, data, left, right):
        if left < right:
            # partition the data and get the pivot
            p = self.__hoare_partition(data, left, right)

            # Quick Sort on the left of pivot
            self.__quick_sort(data, left, p)

            # Quick Sort on the right of pivot
            self.__quick_sort(data, p + 1, right)

    def __hoare_partition(self, data, left, right):
        """
        This function implements the Hoare partition scheme. It uses two pointers, that start
        at both ends of the data.

        :param data: data to partition
        :param left: left end of the data
        :param right: right end of the data
        :return: new right end
        """

        # Pivot value is set to the element at the middle
        p_idx = math.floor((right + left) / 2)
        pivot = data[p_idx]

        # Left index pointer
        l_idx = left - 1
        # Right index pointer
        r_idx = right + 1

        while True:
            self._add_iteration()

            # Move the left index once
            l_idx += 1
            # Keep the left index moving until the item at left index is greater than pivot
            self._add_comparison()
            while data[l_idx] < pivot:
                self._add_iteration()
                l_idx += 1
                self._add_comparison()

            # Move the right index once
            r_idx -= 1
            # Keep the right index moving until the item at right index is less than pivot
            self._add_comparison()
            while data[r_idx] > pivot:
                self._add_iteration()
                r_idx -= 1
                self._add_comparison()

            # If right and left indices cross, return the new right index
            if l_idx >= r_idx:
                return r_idx

            # Swap left index with right index
            self._add_swap([l_idx, r_idx])
            data[l_idx], data[r_idx] = data[r_idx], data[l_idx]
