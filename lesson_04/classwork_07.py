# Пользователь вводит с клавиатуры числа до тех пор,
# пока не введет любой строчный символ, из этих чисел составляется первый список.
# Далее таким же образом вводятся второй и третий списки. Вывести на экран список,
# элементы которого есть в первых двух списках, но отсутствуют в третьем.


# Defining function
def non_unique_elements():
    array_1, array_2, array_3 = [], [], []

    print(f"LIST #1")
    while True:
        n = input(f"Input a number or a symbol to abort inputting: ")
        if n.isnumeric():
            array_1.append(n)
        else:
            print(f"Non-numeric symbol was inputted!")
            print(f"List #1: {array_1}")
            break

    print(f"LIST #2")
    while True:
        n = input(f"Input a number or a symbol to abort inputting: ")
        if n.isnumeric():
            array_2.append(n)
        else:
            print(f"Non-numeric symbol was inputted!")
            print(f"List #2: {array_2}")
            break

    print(f"LIST #3")
    while True:
        n = input(f"Input a number or a symbol to abort inputting: ")
        if n.isnumeric():
            array_3.append(n)
        else:
            print(f"Non-numeric symbol was inputted!")
            print(f"List #3: {array_3}")
            break

    final_list = []

    for i in array_1:
        if i in array_2 and i not in array_3:
            final_list.append(i)

    return final_list


print(f"List of elements in List #1 & #2 and not in List #3: {non_unique_elements()}")
