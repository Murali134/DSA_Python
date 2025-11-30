"""
Sorts using merge sort algorithm.
Args:
array: The list to be sorted
Returns:
A new sorted list
"""

def merge_sort(arr):
    # Base case: already sorted
    if len(arr) <= 1:
        return arr
    # Divide array into halves
    mid = len(arr)//2
    # Recursively sort halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # Merge sorted halves
    return merge(left, right)

"""
Merges two sorted arrays.
Args:
left: First sorted array
right: Second sorted array
Returns:
New sorted array with all elements
"""
def merge(left, right):
    merged = []
    i = j = 0
    # Compare and merge elements
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i = i+1
        else:
            merged.append(right[j])
            j = j+1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# list = [12, 13, 2, 4, 23, 43, 0]
# print(merge_sort(list))
array = [23, 16, 6, 59, 3, 11, 37]
sorted_array = merge_sort(array)
print(sorted_array)