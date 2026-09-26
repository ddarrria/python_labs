def unique_sorted(nums: list[float | int]) -> list[float | int]:

    '''Возвращает уникальный отсортированный (по возрастанию) список

    Args:
        Список чисел (float и int)

    Returns:
        Cписок
    '''

    for i in nums:
        if nums.count(i)>1:
            while nums.count(i)>1:
                nums.remove(i)

    nums1  = []
    while nums:
        m = nums[0]
        for i in nums:
            if i<m:
                m = i
        nums.remove(m)
        nums1.append(m)
    return nums1
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))


