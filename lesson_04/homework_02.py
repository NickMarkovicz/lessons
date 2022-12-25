# Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран.
# Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево.


# Defining function
def is_palindrome(s):
    return 'Inputted word is a palindrome.' if s == s[::-1] else 'Inputted word is not a palindrome.'


# Asking for a correct input
s = input(f"Input a word: ")
if s.isalpha() is (not True):
    while True:
        s = input(f"Wrong input! Input a word: ")
        if s.isalpha() is (not True):
            continue
        else:
            break


# Calling out function for print
print(f"{is_palindrome(s)}")
