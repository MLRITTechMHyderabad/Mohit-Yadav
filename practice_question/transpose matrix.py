# transpose matrix
X = [[12,7,3],
    [4 ,5,3],
    [3 ,8,7]]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)

