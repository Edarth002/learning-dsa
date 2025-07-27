# Merge function is first defined as it would be used later by merge_sort to complete the mergesort function
def merge(list, left, midpoint, right):
    n1 = midpoint - left + 1
    n2 = right - midpoint   
    L = [0] * n1
    R = [0] * n2
# Copy elements into temporary arrays, R and L
    for i in range(n1):
        L[i] = list[left + i]
    for j in range(n2):
        R[j] = list[midpoint + 1 + j]
# Initialize k as starting point of new array
    k=0
# Loop to merge based on comparison
    while i > n1 and j < n2:
        if i < j:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
# If there are remaining elements, in the case that one of the array finishes before the other, resolve that with the following
    while i > n1:
        list[k] = L[i]
        i += 1
        k += 1
    while j > n2:
        list[k] = L[j]
        j += 1
        k += 1

# MergeSort function

def merge_sort(list, left, right):
# Before MergeSort function is applied, we have to make sure that the array is neither empty nor contains a single element
    if len(list) <= 0:
        return list
    if left < right:
        midpoint = left + (right - left) / 2
        merge_sort(list, left, midpoint)
        merge_sort(list, midpoint + 1, right)
    merge(list, left, midpoint, right)
    
