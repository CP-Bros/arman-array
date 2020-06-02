# returns max possible value of Sum(i*arr[i])

def findMax(arr, n):
    maxEl = -1
    maxElIndex = -1

    for i in range(0, n):
        if arr[i] > maxEl:
            maxElIndex = i
            maxEl = arr[i]

    return maxElIndex


def rotateArray(arr, n, rotations):
    rev1 = arr[0:rotations]
    rev1.reverse()

    print(rev1)

    rev2 = arr[rotations:n]
    rev2.reverse()

    print(rev2)

    rev3 = rev1 + rev2
    rev3.reverse()

    return rev3


def sumOfArray(arr, n):

    maxElIndex = findMax(arr, n)

    if maxElIndex == 0:
        rotations = 1
    else:
        rotations = (n - 1) - maxElIndex

    rotatedArray = rotateArray(arr, n, rotations)

    print(rotatedArray)

    sumX = 0

    for i in range(0, n):
        sumX += rotatedArray[i] * i

    return sumX


arr = [1, 2, 3, 4, 10, 5, 6, 7, 8, 9]
print(sumOfArray(arr, len(arr)))
