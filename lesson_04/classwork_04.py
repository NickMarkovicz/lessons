# Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.


# Importing
from random import randrange


# Defining function
def printing_random_numbers():
    while True:
        randon_number = randrange(1, 11)
        print(f"Input a number: {randon_number}")
        if randon_number == 7:
            print(f"Number 7 was randomized, aborting printing.")
            break


# Calling out function for print
printing_random_numbers()
