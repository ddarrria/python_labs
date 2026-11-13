import random
import timeit
import csv

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

def read_numbers(path):
    ''' Считывает данные из csv и возвращает список'''
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]


def generate_samples():
    ''' Создаёт списки случайных чисел и сохраняет их в CSV-файлы '''
    sizes = (1000,10000,100000)
    for n in sizes:
        nums = [random.randint(-1_000_000,1_000_000) for _ in range(n)]
        rows = [[x] for x in nums]
        write_csv(rows,f'data/lab07/samples/{n}_sort.csv',header=('value',))

def bench_sorts():
    rows = []
    for n in (1_000, 10_000, 100_000):
        data = read_numbers(f'data/lab07/samples/{n}_sort.csv')

        funcs = [
            ("bubble_sort", bubble_sort),
            ("insertion_sort", insertion_sort),
            ("selection_sort", selection_sort),
            ("sorted", sorted)
        ]

        for name, sort_func in funcs:
            if n <= 10_000 or name == "sorted":
                time = min(timeit.repeat(lambda: sort_func(data),number=1,repeat=5))
                rows.append(("sorting", n, name, f"{time:.6f}"))
            else:
                rows.append(("sorting", n, name, ">60"))

    return rows

def bench_search():

    rows=[]
    data = read_numbers(f'data/lab07/samples/100000_sort.csv')
    targets = [random.choice(data) for _ in range(10_000)]
    
    time_l_search = min(timeit.repeat(lambda: [linear_search(data, t) for t in targets],number=1,repeat=5))
    rows.append(("search", 100_000, "linear_search", f"{time_l_search:.6f}"))

    time_sb_binary = min(timeit.repeat(lambda: sorted(data),number=1,repeat=5))
    rows.append(("search", 100_000, "sort_before_binary", f"{time_sb_binary:.6f}"))
    sorted_data = sorted(data)

    time_b_search = min(timeit.repeat(lambda: [binary_search(sorted_data, t) for t in targets],number=1,repeat=5))
    rows.append(("search", 100_000, "binary_search", f"{time_b_search:.6f}"))


    for n in (1_000, 10_000):
        data_ts = read_numbers(f'data/lab07/samples/{n}_sort.csv')
        x, y = random.sample(data_ts, 2)
        target = x + y

        time_tsb = min(timeit.repeat(lambda: two_sum_brute(data_ts, target),number=1,repeat=5))
        rows.append(("search", n, "two_sum_brute", f"{time_tsb:.6f}"))

        time_tsf = min(timeit.repeat(lambda: two_sum_fast(data_ts, target),number=1,repeat=5))
        rows.append(("search", n, "two_sum_fast", f"{time_tsf:.6f}"))

    return rows



def main():
    random.seed(42)
    generate_samples()

    header = ("task", "n", "impl", "seconds")
    rows = []

    rows.extend(bench_sorts())
    rows.extend(bench_search())

    write_csv(rows, 'data/lab07/bench.csv', header)

    print("Результаты бенчмарка")
    print(f"{'Task':<12} | {'N':<8} | {'Impl':<20} | {'Seconds':<12}")
    print('-' * 60)

    for task, n, impl, seconds in rows:
        print(f"{task:<12} | {n:<8} | {impl:<20} | {seconds:<12}")

    print('-' * 60)
    print("Результаты сохранены в data/lab07/bench.csv")


if __name__ == "__main__":
    main()
