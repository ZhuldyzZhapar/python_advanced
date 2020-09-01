a = [5, 2, 4, 4, 3, 5, 6, 7, 1, 9]
print("What we had before is:")
print(a)

for j in range(len(a)-1):
    for i in range(j, len(a)):
        if a[j] > a[i]:
            t = a[j]
            a[j] = a[i]
            a[i] = t
    print("Now we have this:")
    print(a)

if a == sorted(a):
    print("correct!")
else:
    print("incorrect!")
