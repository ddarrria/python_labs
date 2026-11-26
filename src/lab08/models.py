from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def check_fio(value):
    """fio: строка, после strip() не пустая."""
    if not isinstance(value, str):
        raise ValueError(f"получено {type(value)}. ожидается строка")
    if not value.strip():
        raise ValueError(f": строка не должна быть пустой")
   


def check_birthdate(value):
    """birthdate: строка YYYY-MM-DD, существующая дата, не в будущем."""
    if not isinstance(value, str):
        raise ValueError("поле birthdate: ожидается строка формата YYYY-MM-DD")
    if not value.strip():
        raise ValueError('birthdate: не должно быть пустым')
    
    try:
        d = date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"поле birthdate: '{value}' не является датой формата YYYY-MM-DD")
    if d > date.today():
        raise ValueError(f"поле birthdate: дата '{value}' в будущем")
   


def check_gpa(value):
    """gpa: int или float, 0 <= gpa <= 5."""
    if isinstance(value,bool) or not isinstance(value, (int, float)):
        raise ValueError("поле gpa: ожидается число (int или float)")
    if not (0 <= value <= 5):
        raise ValueError(f"поле gpa: значение {value} вне диапазона [0;5]")
   


def check_group(value):
    if not isinstance(value,str):
        raise ValueError("group: ожидается строка")
    if not value.strip():
        raise ValueError("group: не должно быть пустым")
   


def make_student(fio, birthdate, group, gpa):
    """Собирает запись студента, проверяя каждое поле."""
    check_fio(fio)
    check_birthdate(birthdate)
    check_group(group)
    check_gpa(gpa)

    return {
        'fio': fio.strip(),
        'birthdate': birthdate,
        'group': group.strip(),
        'gpa': float(gpa),
    }
    


def validate_student(rec):
    """Проверяет готовую запись: набор ключей и значения. При ошибке - ValueError."""

    if not isinstance(rec, dict):
        raise ValueError("запись должна быть словарём")
    
    if set(rec) != set(STUDENT_FIELDS):

        missing = set(STUDENT_FIELDS) - set(rec)
        extra = set(rec) - set(STUDENT_FIELDS)

        raise ValueError(f"неверный набор ключей: нет {sorted(missing)}, лишние {sorted(extra)}")
    
    check_fio(rec["fio"])
    check_birthdate(rec["birthdate"])
    check_group(rec["group"])
    check_gpa(rec["gpa"])


def student_age(rec, today=None):
    """Вычисляет полных лет на дату (по умолчанию сегодня)."""
    born = date.fromisoformat(rec["birthdate"])
    today = today or date.today()
    age = today.year - born.year
    if (today.month, today.day) < (born.month, born.day):  
        age -= 1
    return age



def format_student(rec):
    """Выводит фамилию с инициалами, группу, возраст и средний балл."""
    parts = rec["fio"].split()
    initials = "".join(part[0].upper() + "." for part in parts[1:])
    second_name = parts[0]
    if initials:
        second_name += " " + initials
    age = student_age(rec)

    if 11 <= age % 100 <= 14:
        rez = "лет"
    elif age % 10 == 1:
        rez = "год"
    elif 2 <= age % 10 <= 4:
        rez = "года"
    else:
        rez = "лет"

    return f"{second_name} ({rec['group']}), {age} {rez}, GPA {rec['gpa']:.2f}"


def student_to_dict(rec: dict):
    """Возвращает отдельную копию проверенной записи для сериализации."""
    validate_student(rec)
    return {key: rec[key] for key in STUDENT_FIELDS}


def student_from_dict(d):
    """Десериализация: берёт ровно нужные ключи, gpa приводит к float, валидирует."""
    if not isinstance(d, dict):
        raise ValueError("запись должна быть словарём")
    for key in STUDENT_FIELDS:
        if key not in d:
            raise ValueError(f"отсутствует поле {key}")

    if isinstance(d["gpa"], bool):
        raise ValueError("gpa: значение bool не допускается")
    try:
        gpa = float(d["gpa"])
    except (ValueError, TypeError):
        raise ValueError(f"gpa: некорректное значение {d['gpa']}")
    
    return make_student(d["fio"], d["birthdate"], d["group"], gpa)


if __name__ == "__main__":

    student = make_student("Шилова Дарья Александровна", "2009-03-26", "БИВТ-26-6-2", 4)
    print("Создан студент:", student)

    print("Форматирование:", format_student(student))

    print("Возраст:", student_age(student))

    print("Попытка создать студента с неверным GPA")
    try:
        make_student("Иванов Иван Иванович", "2007-05-14", "БИВТ-26-6-2", "4")
    except ValueError as e:
        print(f"Перехвачена ожидаемая ошибка: {e}")