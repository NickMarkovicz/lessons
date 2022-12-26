# Написать функцию принимающая на вход неопределенное количество аргументов и именованный аргумент func_type.
# В зависимости от func_type вернуть минимальное либо максимальное значение. Написать программу в виде трех функций.


# Defining function
def unknown_amount_of_elements(*array, func_type):
    return max(array) if func_type == "Maximal element" else None


# Calling out function for print
print(f"{unknown_amount_of_elements(1, 2, 5, 10, func_type='Maximal element')}")
