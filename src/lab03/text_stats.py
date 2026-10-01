import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.lib.text import normalize, tokenize, count_freq, top_n

flag = 1 # для табличного вывода

def rez_text():
    text = sys.stdin.read()
    if text.strip() == '':
        raise ValueError('Текст не введен')
    norma = normalize(text)
    token = tokenize(norma)
    cf = count_freq(token)
    top = top_n(cf)
    word = len(token)
    unique = len(set(token))
    print(f'Всего слов: {word}')
    print(f'Уникальных слов: {unique}')
    print(f'Топ-5:')
    if not flag:
        for w,c in top:
            print(f'{w}:{c}')
    else:
        max_len = max(max([len(w) for w, c in top]), len('слово'))
        head = f'{"слово":<{max_len}} | частота'
        print(head)
        print('-' * len(head))
        for w, c in top:
            print(f'{w:<{max_len}} | {c}')

if __name__ == '__main__':
    rez_text()

