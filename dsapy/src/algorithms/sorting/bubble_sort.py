def bubble_sort(data: list[int | float | str]) -> list[int | float | str]:
    """
    This function is an implementation of the bubble sort algorithm.
    It sorts the array in ascending order.
    It returns a sorted copy of the input list.

    :param data: list to be sorted
    :return: sorted copy of input list
    """

    # Copy the input to a new list
    data = data.copy()

    # Loop through each element
    for i in range(len(data)):
        # Loop to bubble up the elements
        for j in range(len(data) - 1 - i):
            # Compare to adjacent elements. > Ascending
            if data[j] > data[j + 1]:
                # Swap the elements
                data[j], data[j + 1] = data[j + 1], data[j]

    # Return the sorted array
    return data
