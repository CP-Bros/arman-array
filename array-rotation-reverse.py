# Write a program that rotate an array - reverse method

a = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(a)
rotation = 9

# Using python's inbuit methods

# rev1 = a[0:rotation]
# rev1.reverse()
# print(rev1)

# rev2 = a[rotation:n]
# rev2.reverse()

# print(rev2)

# rev3 = rev1 + rev2
# rev3.reverse()

# Using loops  

rev1 = []
rev2 = []
rev3 = []

for i in range(rotation - 1, -1, -1):
    rev1.append(a[i])

print(rev1)

for i in range(n - 1, rotation - 1, -1):
    rev2.append(a[i])

print(rev2)

i = 0
j = 0

x = len(rev2)
y = len(rev1)

while True:
    if j < x:
        rev3.append(rev2.pop())
        j += 1
    elif i < y:
        rev3.append(rev1.pop())
        i += 1
    else:
        break

print(rev3)
