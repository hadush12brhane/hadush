def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort the sub-arrays
        quick_sort(arr, low, pivot_index)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Choose the rightmost element as the pivot
    pivot = arr[low]

    i = low
    j = high

    while True:
        # Find element larger than the pivot from the left side
        while arr[i] < pivot:
            i += 1

        # Find element smaller than the pivot from the right side
        while arr[j] > pivot:
            j -= 1

        # If there are elements to swap
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            # If no elements to swap, the partition is complete
            return j

# Example usage
A = [2, 4, 7, 1, 6, 9, 0]
quick_sort(A, 0, len(A) - 1)

print("Sorted Array:", A)
