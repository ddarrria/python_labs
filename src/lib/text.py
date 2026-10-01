import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    '''Нормализует текст

    Args:
        text: Исходный текст
        casefold: Перевод букв в строчный вид (True)
        lower: Перевод букв в нижний регистр (False)
        yo2e: Замена ли ё/Ё на е/Е

    Returns:
        text: Обработанный текст
    '''

    if casefold == True:
        text = text.casefold()
    if casefold == False:
        text = text.lower()
    if yo2e== True:
        text = text.replace('ё','е').replace('Ё','Е')
    text = ' '.join(text.split())
    return text


def tokenize(text: str) -> list[str]:

    ''' Разбивает текст в "токены"

    Args:
        text: Исходный текст 

    Returns:
        r: Список слов (токенов)
    '''

    r = []
    for m in re.finditer(r'\w+(-\w+)*',text):
        word = m.group()
        r.append(word)
    return r


def count_freq(tokens: list[str]) -> dict[str, int]:

    '''Считает количество повторений токенов

    Args:
        tokens: Список слов (токенов)

    Returns:
        r: Словарь: слово, количество повторений
    '''

    r = {}
    for i in tokens:
        if i in r:
            r[i] +=1
        else:
            r[i] = 1
    return r


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    '''Выводит топ  слов по частоте

    Args:
        freq: Словарь: слово, количество повторений
        n: Количество элементов в топе

    Returns:  Список кортежей  (слово, количество повторений)
    '''

    
    return sorted(freq.items(), key = lambda item : (-item[1], item[0]))[:n]
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
print(top_n(count_freq(["a","b","a","c","b","a"]), n =2))
print(top_n(count_freq(["bb","aa","bb","aa","cc"]), n=2 ))





if __name__ == '__main__':
    print(normalize("ПрИвЕт\nМИр\t"))
    print(normalize("ёжик, Ёлка" ))
    print(normalize("Hello\r\nWorld" ))
    print(normalize("  двойные   пробелы  " ))

    print(tokenize("привет мир" ))
    print(tokenize("hello,world!!!" ))
    print(tokenize("по-настоящему круто" ))
    print(tokenize("2025 год" ))
    print(tokenize("emoji 😀 не слово" ))

    print(count_freq(["a","b","a","c","b","a"]))
    print(count_freq(["bb","aa","bb","aa","cc"]))
    print(top_n(count_freq(["a","b","a","c","b","a"]), n =2))
    print(top_n(count_freq(["bb","aa","bb","aa","cc"]), n=2 ))

    