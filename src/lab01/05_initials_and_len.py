name = (input('ФИО: ')).split()
fio = f'{name[0][0]}{name[1][0]}{name[2][0]}'
l = len(name[0])+len(name[1])+len(name[2])+2
print(f'Инициалы: {fio}.')
print(f'Длина (символов): {l}')