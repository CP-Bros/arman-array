def findRotateCount(arr, n):
    min = arr[0]
    min_index = 0

    for i in range(0, n):
        if min > arr[i]:
            min = arr[i]
            min_index = i

    return min_index

a = [7, 9, 11, 12, 15]
print(findRotateCount(a, len(a)))
