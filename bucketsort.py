def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Find minimum and maximum values to know range
    min_value, max_value = min(arr), max(arr)
    
    # Create buckets and distribute the elements
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    for num in arr:
        index = int((num - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(num)

    # Sort each bucket and concatenate the results
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Example usage
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Given array is", arr)
sorted_arr = bucket_sort(arr)
print("Sorted array is", sorted_arr)