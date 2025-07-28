def binary_search(list, target):
    """
        Binary Search Algorithm
    """
    first = 0
    last = len(list) - 1

    while(first <= last):
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] > target:
            last = midpoint - 1
        else: 
            first = midpoint  + 1
    return "Target not found"
