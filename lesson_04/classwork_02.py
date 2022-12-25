# Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n (n вводится с клавиатуры).


# Defining function
def aliquot():
    n = int(input(f"Input main number: "))
    return [i for i in range(1, 101) if i % n == 0]


# Calling out function for print
print(f"{aliquot()}")
