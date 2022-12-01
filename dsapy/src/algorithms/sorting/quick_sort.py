import math
import time


class QuickSort:
    """
    This class is a base class for the in-place sorting algorithms.\n
    It has the following methods:
        - sort: The main implementation of the sort algorithm
        - animation: Returns a Dictionary of Lists, containing all swap and comparison operations.\n
        - metadata: Returns a Dictionary of metadata for the algorithm.

    Animation Keys:
        - swap
        - comparison
    """

    def __init__(self):
        """
        Initializes the class with a metadata and an animation dictionary.
        """
        self.__metadata = {}

        self.__animation = {}

    def __init_metadata(self):

        self.__metadata = {
            'swap_count': 0,
            'comparison_count': 0,
            'iteration_count': 0,
            'runtime': 0.0,
        }

        self.__animation = {
            'swap': [],
            'comparison': []
        }

    def metadata(self) -> dict:
        """
        Returns a metadata dictionary.\n
        Metadata Keys:
            - swap_count
            - comparison_count
            - iteration_count
            - run_time

        :return: A metadata dictionary
        """
        return self.__metadata

    def animation(self) -> dict:
        """
        Returns a dictionary containing all swaps and animations.\n
        Animation Keys:
            - swap
            - comparison

        :return: An animation dictionary
        """
        return self.__animation

    def sort(self, data: list[int | float | str]) -> list[int | float | str]:
        # Initiate/Reset the metadata and animations
        self.__init_metadata()

        # Copy the input to a new list
        data = data.copy()

        # CPU start time of the sorting algorithm
        start_time = time.process_time()

        self.__quick_sort(data, 0, len(data) - 1)

        # CPU end time of the sorting algorithm
        end_time = time.process_time()
        # Total CPU time in ms
        self.__metadata['runtime'] = round(1000 * (end_time - start_time), 2)

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
            self.__metadata['iteration_count'] += 1

            # Move the left index once
            l_idx += 1
            # Keep the left index moving until the item at left index is greater than pivot
            self.__metadata['comparison_count'] += 1
            self.__animation['comparison'].append([l_idx, p_idx])
            while data[l_idx] < pivot:
                self.__metadata['iteration_count'] += 1
                l_idx += 1
                self.__metadata['comparison_count'] += 1
                self.__animation['comparison'].append([l_idx, p_idx])

            # Move the right index once
            r_idx -= 1
            # Keep the right index moving until the item at right index is less than pivot
            self.__metadata['comparison_count'] += 1
            self.__animation['comparison'].append([r_idx, p_idx])
            while data[r_idx] > pivot:
                self.__metadata['iteration_count'] += 1
                r_idx -= 1
                self.__metadata['comparison_count'] += 1
                self.__animation['comparison'].append([r_idx, p_idx])

            # If right and left indices cross, return the new right index
            if l_idx >= r_idx:
                return r_idx

            # Swap left index with right index
            self.__animation['swap'].append([l_idx, r_idx])
            self.__metadata['swap_count'] += 1
            data[l_idx], data[r_idx] = data[r_idx], data[l_idx]
