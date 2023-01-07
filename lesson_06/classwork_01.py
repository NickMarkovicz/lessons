# Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
# Написать две функции, одна переводит слово с английского на русский,
# где слово - это входной параметр, вторая функция - с русского на английский.


dictionary = {
    "apple": "яблоко",
    "car": "машина"
}


def translate_to_english(word):  # Translating to English
    for eng, rus in dictionary.items():
        if word != rus:
            continue
        else:
            print(f"Слово {rus} на английском: {eng}")
            return
    print(f"Слово не найдено")


def translate_to_russian(word):  # Translating to Russian
    if word in dictionary:
        print(f"Word \"{word}\" in Russian: {dictionary.get(word)}")
    else:
        print(f"Word not found")


# Calling out functions for print
translate_to_russian(input(f"Input a word: ").lower())
translate_to_english(input(f"Введите слово: ").lower())
