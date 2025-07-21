def binary_search(list, target):
    """
    
    """
    first = 0
    last = len(list) - 1

    while(first <= last):
        midpoint = (first + last) // 2

        if(list[midpoint] == target):
            return list[midpoint]
        if(list[midpoint] > target):
            last = midpoint - 1
        if(list[midpoint] < target):
            first = midpoint  + 1
    return "Target not found"

list = [0,1,2,3,4,5,6]
target = 3

print("The target is found at index: ",binary_search(list, target))