# Check if any pair in array can sum upto given value

def hasPairSum(arr, n, x):
    temp = {}

    for i in range(0, len(a)):
        diff = x - a[i]

        if diff in temp:
            return True
        else:
            temp[a[i]] = True

    return False


a = [3, 4, 5, 1, 2]
x = 7

print(hasPairSum(a, len(a), x))