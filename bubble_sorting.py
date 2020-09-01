a = [5, 2, 4, 4, 3, 5, 6, 7, 8, 9]
print("What we had before is:")
print(a)
for j in range(len(a)):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp

print("Now we have this:")
print(a)
