# Create a function for binary search recursive method
def binary_search_recursive(arr, target):
    if len(arr) == 0:
        return False
    mid = len(arr) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search_recursive(arr[mid + 1:], target)
    else:
        return binary_search_recursive(arr[:mid], target)
    return False
