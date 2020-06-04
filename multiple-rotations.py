currentRotation = 0
tempAr = []


def rotateArray(arr, n, rotations):

    global currentRotation, tempAr

    rotations = abs(rotations - currentRotation)
    currentRotation += rotations

    if len(tempAr) != 0:
        arr = tempAr

    rev1 = arr[0:rotations]
    rev1.reverse()

    rev2 = arr[rotations:n]
    rev2.reverse()

    rev3 = rev1 + rev2
    rev3.reverse()

    tempAr = rev3

    return rev3


arr = [1, 3, 5, 7, 9]
n = len(arr)

k = 2
print(rotateArray(arr, n, k))

k = 3
print(rotateArray(arr, n, k))

k = 4
print(rotateArray(arr, n, k))
