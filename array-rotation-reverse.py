# Write a program that rotate an array - reverse method

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(a)
rotation = 3

rev1 = a[0:rotation]
rev1.reverse()

rev2 = a[rotation:n]
rev2.reverse()

rev3 = rev1 + rev2
rev3.reverse()

print(rev3)
