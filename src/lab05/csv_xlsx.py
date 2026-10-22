from openpyxl import Workbook
import csv
from pathlib import Path
from src.lab04.io_txt_csv import ensure_parent_dir


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX.

    Первая строка CSV — заголовок. Лист называется "Sheet1". 
    Ширина каждой колонки равна длине самого длинного значения, но не меньше 8 символов.
    Значения записываются как строки (типы не угадываются).

    Raises:
        FileNotFoundError: входного CSV нет.
        ValueError: неверное расширение, пустой CSV.
    """

    cp = Path(csv_path)
    xlp = Path(xlsx_path)

    if not cp.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")

    if cp.suffix.lower() != '.csv':
        raise ValueError("Указанный файл не формата CSV")

    with cp.open('r', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))

    if not reader:
        raise ValueError("Файл CSV пустой")

    wb = Workbook()
    ws = wb.active
    assert ws is not None
    ws.title = "Sheet1"
    for row in reader:
        ws.append(row)

    for col in ws.columns:
        max_len = 0
        letter = col[0].column_letter

        for cell in col:
            if cell.value and len(str(cell.value)) > max_len:
                max_len = len(str(cell.value))

        ws.column_dimensions[letter].width = max(max_len, 8)

    ensure_parent_dir(xlp)
    wb.save(xlp)

if __name__ == '__main__':
    csv_to_xlsx(r"data/lab05/samples/people.csv", r"data/lab05/out/people.xlsx")
    