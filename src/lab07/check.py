import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(fn, trials=100):
    k = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = nums.copy()
        result = fn(nums)

        assert result == sorted(nums), f"{fn.__name__} ошибься на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменил исходный список"
        k +=1
    return k


def check_search(trials=100):
    """
    Проверяет linear_search и binary_search на случайных примерах
    """
    k = 0

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-100, 100)

        # linear_search
        try:
            lin_p = nums.index(x)
        except ValueError:
            lin_p = -1

        assert linear_search(nums, x) == lin_p, (
            f"linear_search ошиблась в поиске {x} на {nums}"
        )
        k += 1

        # binary_search
        sorted_nums = sorted(nums)
        bin_p = binary_search(sorted_nums, x)

        if x in sorted_nums:
            assert bin_p != -1 and sorted_nums[bin_p] == x, (
                f"binary_search ошиблась на {sorted_nums}, искали {x}: {bin_p}"
            )
        else:
            assert bin_p == -1, (
                f"binary_search нашел отсутствующий элемент {x}"
            )
        k += 1

        if sorted_nums:
            for i in (sorted_nums[0], sorted_nums[-1]):
                bin_p = binary_search(sorted_nums, i)

                assert bin_p != -1 and sorted_nums[bin_p] == i, (
                    f"binary_search не нашла крайний элемент {i}"
                )
                k += 1

    return k


def check_two_sum(trials=100):
    k = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-200, 200)

        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)

        if brute is None or fast is None:
            assert brute == fast, f"Функции дали разный результат при поиске {target} в {nums}"
        else:
            assert nums[brute[0]] + nums[brute[1]] == target, (
                f"two_sum_brute ошиблась на {nums}, искали {target}"
            )
            assert nums[fast[0]] + nums[fast[1]] == target, (
                f"two_sum_fast ошиблась на {nums}, искали {target}"
            )
        k += 1
    return k


if __name__== "__main__":
    random.seed(42)
    n=0
    
    for fn in (bubble_sort, insertion_sort, selection_sort):
        n += check_sorting(fn)
    
    n += check_search()
    
    n += check_two_sum()
    
    print(f"OK, {n} проверок")
