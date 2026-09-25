def col_sums(mat: list[list[float | int]]) -> list[float]:

    if mat == []:
            return []
    for i in mat:
        if len(i) != len(mat[0]):
            return ValueError ('Рваная матрица')
    r = []
    for i in range(len(mat[0])):
        s = 0
        for j in range(len(mat)):
            s  = s+ mat[j][i]
        r.append(s)
    return r
print(col_sums([[1, 2, 3], [4, 5, 6]] ))
print(col_sums([[-1, 1], [10, -10]] ))
print(col_sums([[0, 0], [0, 0]] ))
print(col_sums([[1, 2], [3]]))

    