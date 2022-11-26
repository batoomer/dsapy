def selection_sort(data: list[int | float | str]) -> list[int | float | str]:
    """
    This function is an implementation of the selection sort algorithm.
    It sorts the list in ascending order.
    It returns a sorted copy of the input list.

    :param data: list to be sorted
    :return: sorted copy of input list
    """
    # Copy the input to a new list
    data = data.copy()

    # Loop through the list
    for i in range(len(data)):
        # Set the minimum index to the first element of the unsorted part of the list
        min_idx = i

        # Loop through the unsorted part of the list and find the minimum element
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j

        # Swap the first element of the unsorted list with the minimum element of the unsorted list
        data[i], data[min_idx] = data[min_idx], data[i]

    # Return the sorted array
    return data
