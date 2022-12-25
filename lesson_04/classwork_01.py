# Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.


# Importing
from random import randrange


# Defining function
def sum_of_numbers_more_than_10(array):
    return [i for i in array if i > 10]


# Calling out function for print
array = [randrange(101) for i in range(randrange(101))]
print(f"""Your list is: {array}
Length of your list is: {len(array)}""")
print()
print(f"Sum of elements > 10 in your list is: {sum(sum_of_numbers_more_than_10(array))}")
