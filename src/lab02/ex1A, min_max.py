def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    
    ''' Вычисляет максимум и минимум списка

    Args: 
        Список чисел (float и int)

    Returns:
        Кортеж (минимум, максимум)

    Raises:
        ValueError:
          'Список пуст'

    '''

    if len(nums)==0:
        raise ValueError('Список пуст')
    minn = nums[0]
    maxx = nums[0]
    for i in nums:
        if i<minn:
            minn= i
        if i > maxx:
            maxx = i
    return (minn, maxx)
print(min_max([3, -1, 5, 5, 0] ))
print(min_max([42] ))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([] ))

