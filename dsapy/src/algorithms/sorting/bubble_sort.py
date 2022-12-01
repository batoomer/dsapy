import time


class BubbleSort:
    """
    This class is an implementation of the Bubble Sort Algorithm.\n
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
        """
        This function is an implementation of the bubble sort algorithm.
        It sorts the array in ascending order.
        It returns a sorted copy of the input list.

        :param data: list to be sorted
        :return: sorted copy of input list
        """

        # Initiate/Reset the metadata and animations
        self.__init_metadata()

        # Copy the input to a new list
        data = data.copy()

        # CPU start time of the sorting algorithm
        start_time = time.process_time()

        # Loop through each element
        for i in range(len(data)):
            self.__metadata['iteration_count'] += 1
            # Loop to bubble up the elements
            for j in range(len(data) - 1 - i):
                self.__metadata['iteration_count'] += 1
                # Compare to adjacent elements. > Ascending
                self.__metadata['comparison_count'] += 1
                self.__animation['comparison'].append([j, j+1])
                if data[j] > data[j + 1]:
                    # Swap the elements
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.__metadata['swap_count'] += 1
                    self.__animation['swap'].append([j, j + 1])

        # CPU end time of the sorting algorithm
        end_time = time.process_time()

        # Total CPU time in ms
        self.__metadata['runtime'] = round(1000 * (end_time - start_time), 2)

        # Return the sorted array
        return data
