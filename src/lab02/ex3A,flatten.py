def flatten(mat: list[list | tuple]) -> list:

    r = []
    for i in mat:
        if type(i)== list or type(i)== tuple:
            for j in i:
                r.append(j)
        else:
            return TypeError('Элемент не является списком или кортежем')
    return r
print(flatten([[1, 2], [3, 4]] ))
print(flatten([[1, 2], (3, 4, 5)] ))
print(flatten([[1], [], [2, 3]] ))
print(flatten([[1, 2], "ab"]))