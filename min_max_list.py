def find_min_max(numbers):
    """
    Function to find the minimum and maximum elements in a list.
    :param numbers: List of numbers
    :return: Tuple (min_element, max_element)
    """
    if not numbers:  # Check if the list is empty
        return None, None
    return min(numbers), max(numbers)

# Example usage
my_list = [10, 45, 3, 99, 23]
min_element, max_element = find_min_max(my_list)
print("Minimum Element:", min_element)
print("Maximum Element:", max_element)
