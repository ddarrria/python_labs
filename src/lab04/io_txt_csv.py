import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    """
    Читает текстовый файл и возвращает содержимое одной строкой
    
    Args:
        path: Путь к файлу в виде строки или объекта Path.
        encoding: Кодировка файла. По умолчанию UTF-8. 
                  Для файлов в другой кодировке можно указать, например, encoding='cp1251'
            
    Returns:
        Содержимое файла в виде строки
    
    Raises:
        FileNotFoundError: Если файл не найден.
        UnicodeDecodeError: Если содержимой файла невозможно декодировать в указанной кодировке"""
     
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:


    """
    Записывает строки rows в CSV-файл path с разделителем ",".

    Если указан header - он записывается первой строкой файла.

    Файл создаётся заново (если его не было) либо полностью
    перезаписывается (если уже существовал).

    Перед записью проверяется, что все строки в rows имеют одинаковую длину. Если нет - ValueError.
    Если header задан, его длина должна совпадать с длиной строк.

    Если rows пуст и header=None - создаётся пустой файл (0 строк).
    Если rows пуст, а header задан - в файле будет только заголовок.

    """
    p = Path(path)
    rows = list(rows)

    if len(rows)>0:
        first_rows = len(rows[0])

        for r in rows:
            if len(r)!= first_rows:
                raise ValueError ("Все строки в rows должны быть одной длины")

        if header is not None and len(header) != first_rows:
            raise ValueError("Длина header должна совпадать с длиной строк в rows")

     
    ensure_parent_dir(path)
    p = Path(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории для path, если их ещё нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt")
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
    print("CSV создан.")