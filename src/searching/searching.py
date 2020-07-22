def binary_search(arr, target, start, end):
    '''
    Binary search with recursive code
    '''

    if start > end:
        return -1
    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)


#        0   1   2   3   4   5  6  7  8  9   10  11 12 13
arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3,  5,  7,  8, 9]

fnd = binary_search(arr1, 6, (len(arr1)-1), 1)
print(fnd)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

    pass
