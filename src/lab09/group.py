import csv
from pathlib import Path

from src.lab08.models import STUDENT_FIELDS, student_from_dict, student_to_dict, validate_student

HEADER = STUDENT_FIELDS


def ensure_storage(path) -> None:
    """Создаёт CSV-файл с заголовком, если хранилища ещё нет."""
    storage = Path(path)
    storage.parent.mkdir(parents=True, exist_ok=True)

    if not storage.exists():
        with storage.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
            writer.writeheader()



def load_students(path) -> list[dict]:
    """Читает все записи из CSV. Каждая строка проходит через student_from_dict."""
    path = Path(path)

    if not path.is_file():
        raise FileNotFoundError(f"Файл не найден: {path}")

    students = []

    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError("В CSV нет строки-заголовка")

        if reader.fieldnames != HEADER:
            raise ValueError(f"Неверный заголовок CSV: {reader.fieldnames}, "f"ожидается {HEADER}")

        for number, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"Строка {number}: лишние колонки")

            try:
                students.append(student_from_dict(row))
            except (ValueError, KeyError, TypeError) as e:
                raise ValueError(f"Строка {number}: {e}") from e

    return students


def save_students(path, students):
    """Перезаписывает файл целиком."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(students)


def add_student(path, student):
    """Валидирует запись студента и дописывает её в конец CSV файла."""
    validate_student(student)
    students = load_students(path)
    students.append(student_to_dict(student))
    save_students(path, students)


def list_students(path, sort_by=None):
    students = load_students(path)
    if sort_by is None:
        return students
        
    if sort_by not in ("fio", "gpa"):
        raise ValueError("Недопустимый параметр сортировки. Используйте 'fio' или 'gpa'.")
        
    return sorted(students, key=lambda x: x[sort_by])


def find_students(path, substr: str) -> list[dict]:
    """Ищет студентов по подстроке в ФИО без учёта регистра."""
    students = load_students(path)
    search_text = substr.casefold()
    return [s for s in students if search_text in s["fio"].casefold()]


def remove_student(path, fio: str) -> int:
    """Удаляет все записи с таким ФИО и возвращает их количество."""

    students = load_students(path)
    initial_count = len(students)

    students = [s for s in students if s["fio"].casefold() != fio.casefold()]

    removed_count = initial_count - len(students)
    if removed_count > 0:
        save_students(path, students)

    return removed_count


def update_student(path, fio: str, **fields):
    """Обновляет поля первой записи с таким ФИО. True, если запись найдена."""
    for key in fields:
        if key not in HEADER:
            raise KeyError(f"Неизвестное поле: {key}")

    students = load_students(path)

    for i in range(len(students)):
        if students[i]["fio"].casefold() == fio.casefold():
            new_rec = dict(students[i])
            new_rec.update(fields)
            students[i] = student_from_dict(new_rec)
            save_students(path, students)
            return True

    return False


