def quick_sort(arr):
    """Quick sort algorithm."""
    if len(arr) <= 1:  # Base case: an empty or single-element list is already sorted
        return arr
    else:
        pivot = arr[0]  # Choose the first element as the pivot
        # Partition the array into three parts
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        # Recursively sort and combine
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
unsorted_list = [34, 7, 23, 32, 5, 62]
sorted_list = quick_sort(unsorted_list)
print("Sorted List:", sorted_list)
