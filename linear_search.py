

def linear_search(list, target): 
    """
    Returns index position of target or returns Not Found
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return "Not found"


list = [4, 7, 8, 9, 0, 3, 5]
target = 3

print(linear_search(list, target))