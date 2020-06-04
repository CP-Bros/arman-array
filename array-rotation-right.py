# Write a program that rotate an array right side

a = [1, 2, 3, 4, 5, 6]
n = len(a)

temp = []

rotation = 10

for i in range(n - rotation, n):
    temp.append(a[i])

for i in range(n - rotation - 1, -1, -1):
    a[i + rotation] = a[i]

j = 0
for i in range(0, rotation):
    a[i % n] = temp[j]
    j += 1

print(a)
