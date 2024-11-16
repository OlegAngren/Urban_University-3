def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру для корректного сравнения
    root_word = root_word.lower()
    same_words = []

    # Перебираем слова из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем, содержится ли root_word в слове или слово в root_word
        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)

    # Возвращаем список подходящих слов
    return same_words

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # Ожидаемый вывод: ['richiest', 'orichalcum', 'richies']
print(result2)  # Ожидаемый вывод: ['Able', 'Disable']