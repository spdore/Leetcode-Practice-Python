numRows = 30

res = []
for i in range(numRows):
    row = []
    for j in range(0, i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(res[i - 1][j] + res[i - 1][j - 1])
    res.append(row)

print(res)