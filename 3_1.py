# Глобальная переменная для подсчета вызовов
calls = 0

# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1

# Функция для работы со строкой
def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    return len(string), string.upper(), string.lower()

# Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    # Преобразуем строку и элементы списка в нижний регистр для игнорирования регистра
    return string.lower() in (item.lower() for item in list_to_search)

# Вызов функций для проверки
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

# Вывод общего количества вызовов
print(calls)