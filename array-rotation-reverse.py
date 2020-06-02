# Write a program that rotate an array - reverse method

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(a)
rotation = 3

# Using python's inbuit methods

# rev1 = a[0:rotation]
# rev1.reverse()

# rev2 = a[rotation:n]
# rev2.reverse()

# rev3 = rev1 + rev2
# rev3.reverse()

# Using loops  

rev1 = []
rev2 = []
rev3 = []

for i in range(rotation - 1, -1, -1):
    rev1.append(a[i])

for i in range(n - 1, rotation - 1, -1):
    rev2.append(a[i])

i = 0
j = 0

while True:
    if j < len(rev2):
        rev3.append(rev2[j])
        j += 1
    elif i < len(rev1):
        rev3.append(rev1[i])
        i += 1
    else:
        break

print(rev3)
