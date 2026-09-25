def format_record(rec: tuple[str, str, float]) -> str:


    if not isinstance(rec, tuple):
        raise TypeError ('Запись не являеся кортежем')
    if len(rec)!=3:
             raise ValueError ('Введены не все элементы')
    if not isinstance(rec[0], str):
                raise TypeError ('ФИО записано не как строка')
    if not isinstance(rec[1], str):
                raise TypeError ('Группа записана не как строка')
    if not isinstance(rec[2], (float, int)):
                raise TypeError ('GPA записоно не как число')
    if len(rec[0].strip().split())==0:
           raise ValueError ('ФИО не введено')
    if len(rec[0].strip().split())!= 3 and len(rec[0].strip().split())!= 2:
               raise ValueError ('Введено неплное ФИО')
    if len(rec[0].strip().split()[0])==0:
        raise ValueError ('Фамилия не введена')
    if len(rec[0].strip().split()[1])==0:
        raise ValueError ('Имя не введно')
    if not(0.0<=rec[2]<=5.0):
         raise ValueError ('GPA не соответствует диапазону')
    

    fio = rec[0].strip().split()
    for i in fio:
           if not i.isalpha():
                  raise ValueError('ФИО должно состоять только из букв')
    surname = fio[0].capitalize()
    name = fio[1]
    group = rec[1]
    gpa = rec[2]
    if len(fio)==3:
        initials = surname + ' ' + name[0].upper() + '.' + fio[2][0].upper() + '.'
    else:
        initials = surname + ' ' + name[0].upper() + '.'
    return (f'{initials}, гр. {group}, GPA {gpa:.2f}')

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6) ))
print(format_record(("Петров Пётр", "IKBO-12", 5.0) ))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0) ))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("       ддд 1233", "ABB-01", 3.999)))

