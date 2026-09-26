def flatten(mat: list[list | tuple]) -> list:

    '''Переделывает список списков (или кортежей) в один список 

    Args:
        Список списков или кортежей
    
    Returns:
        Список
    
    Raises:
        TypeError: 
            'Элемент не является списком или кортежем'
    '''


    r = []
    for i in mat:
        if type(i)== list or type(i)== tuple:
            for j in i:
                r.append(j)
        else:
            raise TypeError('Элемент не является списком или кортежем')
    return r
print(flatten([[1, 2], [3, 4]] ))
print(flatten([[1, 2], (3, 4, 5)] ))
print(flatten([[1], [], [2, 3]] ))
print(flatten([[1, 2], "ab"]))