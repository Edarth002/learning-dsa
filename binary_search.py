


def binary_search(list, target):
    """
        Binary Search Al
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

list = [0,1,2,3,4,5,6]
"""
    target = 10
"""
target = 3

print("The target is found at index: ",binary_search(list, target))