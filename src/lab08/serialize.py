import json
from pathlib import Path
from src.lab04.io_txt_csv import read_text
from src.lab08.models import student_to_dict, student_from_dict


def students_to_json(students, path):
    """Сохраняет список записей в JSON (массив объектов)."""
    data = [student_to_dict(s) for s in students]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)




def students_from_json(path) -> list[dict]:

    '''Загружает данные о студентах из JSON с валидацией каждой записи. Первая битая запись 
    вызывает ValueError с номером записи и причиной.
    '''

    text = read_text(path).strip()
    if not text:
        raise ValueError(f"Получен пустой файл {path} ")
       
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"Некорректные данные в файле {path}: {error}") from error

    if not isinstance(data, list):
        raise ValueError(f'Содержимое файла должно быть списком. Получено: {type(data)}')

    students = []
    for i, item in enumerate(data, 1):
        try:
            students.append(student_from_dict(item))
        except ValueError as e:
            raise ValueError(
                f'Ошибка в записи под индексом {i}: {e}'
            ) from e

    return students



if __name__ == '__main__':

    # Чтение и сохранение данных
    print('Чтение из data/lab08/students_input.json, сохранение в data/lab08/students_output.json')

    try:
        students_list = students_from_json('data/lab08/students_input.json')
        students_to_json(students_list, 'data/lab08/students_output.json')
    except ValueError as e:
        print(f'Ошибка: {e}')


    # Проверка обработки некорректного файла
    try:
        students_from_json('data/lab08/students_bad.json')
    except ValueError as e:
        print(f'Ошибка: {e}')



