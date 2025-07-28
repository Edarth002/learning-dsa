def quicksort(arr):
# Base case to ensure a single element array does not get computed
    if len(arr) < 1:
        return arr
    
    pivot = arr[-1]

    left = [s for s in arr[:-1] if s < pivot]
    right = [s for s in arr[:-1] if s >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)

# Example usage
myArr = [5,7,6,9,2,8,9,2]
sorted_array = quicksort(myArr)
print("Sorted array is given as: ", sorted_array)
