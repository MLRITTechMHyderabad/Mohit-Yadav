#max_min_2d_array

def min_max(mat):
    row = len(mat)
    col = len(mat[0])
    ans = 0
    for i in range(row):
        for j in range(col):
            if ans < mat[i][j]:
                ans = mat[i][j]
    return ans
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(a)
