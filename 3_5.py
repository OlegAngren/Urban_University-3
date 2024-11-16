def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки равна 1, просто возвращаем число
    if len(str_number) == 1:
        return int(str_number)  # единственная цифра

    # Первая цифра в числовом виде
    first = int(str_number[0])

    # Если первая цифра — 0, переходим к следующей цифре
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))  # пропускаем ноль

    # Рекурсивно умножаем первую цифру на результат следующего вызова
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24