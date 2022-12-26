# Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
# Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.


# Defining function
def print_name(name):
    print(f"Hello, {name}")


# Calling out function for print
for i in range(5):
    name = input(f"Input name: ")
    print_name(name)
