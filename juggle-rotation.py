def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def juggleRotation(arr, n, k):

    sets = gcd(n, k)
    d = -1

    for i in range(0, sets):
        j = i
        temp = arr[i]

        while True:
            d = (j + k) % n

            if d == i:
                break

            arr[j] = arr[d]
            j = d

        arr[j] = temp

    return arr


arr = [1, 2, 3, 4, 5, 6]  # [3, 4, 5, 6, 1, 2]

print(juggleRotation(arr, len(arr), 2))
