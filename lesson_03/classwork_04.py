# Взять список [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"],
# извлечь элементы со 2-го по 4-й включительно и вывести их в обратном порядке.


# Defining function
def list_in_reverse():
    my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
    return my_list[2:5][::-1]


# Calling function "list_in_reverse" for print
print(list_in_reverse())