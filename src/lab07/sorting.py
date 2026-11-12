def bubble_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    result = nums.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def insertion_sort(nums):
    """Возвращает отсортированный список методом сортировки вставками. Исходный не меняется."""
    rez = nums.copy()
    for i in range(1, len(rez)):
        current = rez[i]
        j = i - 1
        while j >= 0 and rez[j] > current:
            rez[j + 1] = rez[j]
            j -= 1
        rez[j + 1] = current
    return rez

def selection_sort(nums):
    """Возвращает отсортированный список методом сортировки выбором. Исходный не меняется."""
    rez = nums.copy()
    n = len(rez)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if rez[j] < rez[min_index]:
                min_index = j
        rez[i], rez[min_index] = rez[min_index], rez[i]
    return rez