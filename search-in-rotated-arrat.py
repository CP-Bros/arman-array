def findPivot(arr, n):

    if n < 2:
        return -1

    x1 = 0
    x2 = 1

    for i in range(0, n):
        if arr[x1] > arr[x2]:
            return x1
        else:
            x1 = i
            x2 = i + 1

    return -1


def binarySearch(arr, low, high, key):

    if high < low:
        return -1

    if high == low:
        return low

    mid = int((low + high)/2)

    if key == arr[mid]:
        return mid

    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high, key)
    else:
        return binarySearch(arr, low, mid, key)


def pivotedBinarySearch(arr, n, key):

    pivot = findPivot(arr, n)

    if pivot == -1:
        return binarySearch(arr, 0, n, key)

    if arr[pivot] == key:
        return pivot

    if arr[pivot] <= key:
        return binarySearch(arr, pivot + 1, n, key)

    return binarySearch(arr, 0, pivot, key)


arr = [3, 4, 5, 1, 2]
print(pivotedBinarySearch(arr, len(arr), 4))
