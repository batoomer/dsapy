from dsapy.src.algorithms.sorting.sorting_algorithm import SortingAlgorithm


class InsertionSort(SortingAlgorithm):

    def __init__(self):
        """
        Initializes the base abstract class SortingAlgorithm
        """
        super().__init__()

    def sort(self, data: list[int | float | str]) -> list[int | float | str]:
        """
        This function is an implementation of the insertion sort algorithm.
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

        # Loop through the list starting from the second element.
        for i in range(1, len(data)):
            self._add_iteration()
            j = i
            # Loop through the sorted part of the list and place the new element in the correct place
            while j > 0:
                self._add_comparison()
                # Transferred condition from while loop to make the comparisons animations
                if data[j - 1] <= data[j]:
                    break

                # REAL while loop starts from this line
                self._add_iteration()

                # Swap
                self._add_swap(j, j-1)
                data[j], data[j - 1] = data[j - 1], data[j]
                j -= 1

        # CPU end time of the sorting algorithm
        self._stop_runtime()
        self._add_runtime()

        # Return the sorted array
        return data
