def row_sums(mat: list[list[float | int]]) -> list[float]:
    
    if mat == []:
            return []
    for i in mat:
        if len(i) != len(mat[0]):
            return ValueError ('Рваная матрица')
    
    r = []
    for i in range (len(mat)):
        r.append(sum(mat[i]))
    return r
print(row_sums([[1, 2, 3], [4, 5, 6]] ))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]] ))
print(row_sums([[1, 2], [3]] ))