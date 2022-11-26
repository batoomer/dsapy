def insertion_sort(data: list[int | float | str]) -> list[int | float | str]:
    """
    This function is an implementation of the insertion sort algorithm.
    It sorts the list in ascending order.
    It returns a sorted copy of the input list.

    :param data: list to be sorted
    :return: sorted copy of input list
    """
    # Copy the input to a new list
    data = data.copy()

    # Loop through the list starting from the second element.
    for i in range(1, len(data)):
        j = i

        # Loop through the sorted part of the list and place the new element in the correct place
        while j > 0 and data[j - 1] > data[j]:
            # Swap
            data[j], data[j - 1] = data[j - 1], data[j]
            j -= 1

    # Return the sorted array
    return data
