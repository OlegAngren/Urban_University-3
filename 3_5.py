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
    remaining_result = get_multiplied_digits(int(str_number[1:]))
    if remaining_result == 0:  # Пропускаем умножение на ноль
        return first
    return first * remaining_result


# Пример использования
result = get_multiplied_digits(40203)
print(result)  # Ожидаемый вывод: 24

# Пример с нулями на конце
result = get_multiplied_digits(40500)
print(result)  # Ожидаемый вывод: 20

''' Что изменено:
Добавлена проверка if remaining_result == 0, чтобы избежать умножения на ноль.
При встрече конечных нулей они игнорируются, так как уже не влияют на результат умножения.'''