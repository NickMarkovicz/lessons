# Напишите программу, которая принимает текст и выводит два слова:
# наиболее часто встречающееся и самое длинное, в идеале не использовать библиотечные функции.

# Defining function
def longest_and_most_frequent(text):
    # Defining vars required
    text = text.split()
    garbage = ["и", "или", "а", "о", "в"]
    longest_length = 0
    longest_length_word = ""
    most_frequent_count = 0
    most_frequent_word = ""
    for word in text:  # Iterating every word in the text given
        if word in garbage:  # Filtering useless words
            continue
        if len(word) > longest_length:  # New longest word
            longest_length = len(word)
            longest_length_word = word
        if text.count(word) > most_frequent_count:  # New frequent word
            most_frequent_count = text.count(word)
            most_frequent_word = word
    # Results
    print(f"""The longest word in the text is: {longest_length_word}
The most frequent word in the text is: {most_frequent_word}""")


# Asking for text
text = input(f"Input some text: ")
# Calling out function for print
longest_and_most_frequent(text)
