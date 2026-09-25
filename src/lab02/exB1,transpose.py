def transpose(mat: list[list[float | int]]) -> list[list]:

    if mat == []:
        return []
    for i in mat:
        if len(i) != len(mat[0]):
            return ValueError ('Рваная матрица')

    r = []
    for i in range(len(mat[0])):
        r1 = []
        for j in range(len(mat)):
            r1.append(mat[j][i])
        r.append(r1)
    return r
print(transpose([[1, 2, 3]] ))
print(transpose([[1], [2], [3]] ))
print(transpose([[1, 2], [3, 4]] ))
print(transpose([] ))
print(transpose([[1, 2], [3]]))