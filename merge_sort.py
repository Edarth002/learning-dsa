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
    

# MergeSort function

def merge_sort(list, left, right):
    if len(list) <= 0:
        return list
    if left < right:
        midpoint = left + (right - left) / 2
        merge_sort(list, left, midpoint)
        merge_sort(list, midpoint + 1, right)
    
    
# Before MergeSort function is applied, we have to make sure that the array is neither empty nor contains a single element