from dsapy.src.algorithms.sorting.sorting_algorithm import SortingAlgorithm


class SelectionSort(SortingAlgorithm):
    def __init__(self):
        """
        Initializes the base abstract class SortingAlgorithm
        """
        super().__init__()

    def sort(self, data: list[int | float | str]) -> list[int | float | str]:
        """
        This function is an implementation of the selection sort algorithm.
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

        # Loop through the list
        for i in range(len(data)):
            self._add_iteration()
            # Set the minimum index to the first element of the unsorted part of the list
            min_idx = i

            # Loop through the unsorted part of the list and find the minimum element
            for j in range(i + 1, len(data)):
                self._add_iteration()

                self._add_comparison()
                if data[j] < data[min_idx]:
                    min_idx = j

            # Swap the first element of the unsorted list with the minimum element of the unsorted list
            self._add_swap(i, min_idx)
            data[i], data[min_idx] = data[min_idx], data[i]

            # CPU end time of the sorting algorithm
            self._stop_runtime()
            self._add_runtime()

        # Return the sorted array
        return data
