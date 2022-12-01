from dsapy.src.algorithms.sorting.sorting_algorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    def __init__(self):
        """
        Initializes the base abstract class SortingAlgorithm
        """
        super().__init__()

    def sort(self, data: list[int | float | str]) -> list[int | float | str]:
        """
        This function is an implementation of the bubble sort algorithm.
        It sorts the array in ascending order.
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

        # Loop through each element
        for i in range(len(data)):
            self._add_iteration()
            # Loop to bubble up the elements
            for j in range(len(data) - 1 - i):
                self._add_iteration()
                # Compare to adjacent elements. > Ascending
                self._add_comparison()
                if data[j] > data[j + 1]:
                    # Swap the elements
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self._add_swap([j, j+1])

        # CPU end time of the sorting algorithm
        self._stop_runtime()
        self._add_runtime()

        # Return the sorted array
        return data
