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






if __name__ == '__main__':

   

    # normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"

    # tokenize
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]

    # count_freq + top_n
    freq = count_freq(["a","b","a","c","b","a"])
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]

    # тай-брейк по слову при равной частоте
    freq2 = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
    print( 'все ок!')