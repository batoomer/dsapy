def bubble_sort(arr: list[int | float | str]) -> list[int | float | str]:
    """
    This function is an implementation of the bubble sort algorithm.
    It sorts the array in ascending order.
    It returns a sorted copy of the input list.

    :param arr: list to be sorted
    :return: sorted copy of input list
    """

    # Copy the input to a new list
    arr = arr.copy()

    # Loop through each element
    for i in range(len(arr)):
        # Loop to bubble up the elements
        for j in range(len(arr) - 1 - i):
            # Compare to adjacent elements. > Ascending
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Return the sorted array
    return arr
