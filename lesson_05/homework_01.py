# Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
# В результате ее работы на печать выводятся значения переданных переменных,
# но только если они не равны None. Получим, например, следующее сообщение:
#     Переданы аргументы: var1 = 2, var3 = 10.


# Defining function
def three_args(**array):
    list_of_items = []
    for key, value in array.items():
        if value is not None:
            list_of_items.append(f"{key} = {value}")
    print("Переданы значения: ", end="")
    print(*list_of_items, sep=', ', end='.')


# Calling out function
three_args(var1=5, var2='example', var3=True)
