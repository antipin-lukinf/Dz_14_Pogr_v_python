# Задание №1
# 📌 Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

# Задание №2
# 📌 Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import doctest
from string import ascii_lowercase


def removal_chars(text: str) -> str:
    """
    >>> removal_chars('FFFggggY5') == 'fffggggy'
    True
    >>> removal_chars('sss   hhHH7&8') ==  'ssshhhh'
    True
    >>> removal_chars('5 6 9 8 7  )))))   ') == '          '
    False
    """
    result = ''
    for ch in text.lower():
        if ch in ascii_lowercase + '':
            result += ch

    return result


if __name__ == '__main__':
    doctest.testmod(verbose=True)
