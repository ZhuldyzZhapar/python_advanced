a = [
    [4, 7, 8, 4],
    [3, 2, 8, 4],
    [2, 7, 1, 4],
    [1, 7, 2, 3],
    [0, 7, 8, 8],
    [1, 2, 3, 4],
]

b = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 2],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
]

c = []
for i in range(len(a)):
    another_line = []
    for j in range(len(b[0])):
        another_line.append(0)
    c.append(another_line)

# n,m x m, k = n, k
# 6,4 x 4, 5 = 6, 5

for w in range(len(a)):
    for j in range(len(b[0])):
        s = 0
        for i in range(len(b)):
            s += a[w][i] * b[i][j]
        c[w][j] = s

for i in range(len(c)):
    print(c[i])
