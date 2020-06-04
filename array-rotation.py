# Write a program that rotate an array

a = [1, 2, 3, 4, 5, 6]
n = len(a)

temp = []

rotation = 10

for i in range(0, rotation):
    temp.append(a[i])

j = 0
for i in range(0, n):
    if i + rotation < n:
        a[i] = a[i + rotation]
    else:
        a[i] = temp[j]
        j += 1

print(a)
