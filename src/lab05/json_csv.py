from pathlib import Path
import json
import csv

from src.lab04.io_txt_csv import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте.
    """
    jp = Path(json_path)
    cp = Path(csv_path)

    if not jp.exists():
        raise FileNotFoundError("Указанный JSON файл не найден")

    if jp.suffix.lower() != '.json':
        raise ValueError("Указанный файл не формата JSON")

    with jp.open('r', encoding='utf-8') as p:
        try:
            data = json.load(p)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Файл JSON пустой или имеет неправильный формат')
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")

    ensure_parent_dir(cp)
    fieldnames = {}
    for element in data:
        for key in element.keys():
            fieldnames[key] = None

    with cp.open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames.keys()))
        w.writeheader()
        w.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    """
    jp = Path(json_path)
    cp = Path(csv_path)

    if not cp.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")

    if cp.suffix.lower() != '.csv':
        raise ValueError("Указанный файл не формата CSV")

    with cp.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("Файл CSV пустой")

        data = list(reader)

    if not data:
        raise ValueError("Файл CSV не содержит данных")

    ensure_parent_dir(jp)
    with jp.open('w', encoding='utf-8') as p:
        json.dump(data, p, ensure_ascii=False, indent=2)
    
if __name__ == '__main__':
    csv_to_json(r'data\samples\people.csv',
                r'data\out\people_from_csv.json')
    json_to_csv(r'data\samples\people.json',
                r'data\out\people_from_json.csv')
    csv_to_json(r"data/samples/cities.csv",
                r"data/out/cities.json")
    json_to_csv(r'data\samples\broken.json',
                r'data\out\broken.csv')