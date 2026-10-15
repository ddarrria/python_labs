import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    
    p = Path(path)
    rows = list(rows)

    if len(rows)>0:
        first_rows = len(rows[0])

        for r in rows:
            if len(r)!= first_rows:
                raise ValueError ("Все строки в rows должны быть одной длины")

        if header is not None and len(header) != first_rows:
            raise ValueError("Длина header должна совпадать с длиной строк в rows")

    p.parent.mkdir(parents=True, exist_ok=True)


    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


if __name__ == "__main__":
    txt = read_text("data/lab04/input.txt")
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data/lab04/check.csv")
    print("CSV создан.")