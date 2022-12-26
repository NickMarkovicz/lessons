# Создать функцию, которая принимает на вход неопределенное количество аргументов
# и возвращает их сумму и максимальное из них.


# Defining function
def sum_and_max_of(array):
    return sum(array), max(array)


array = []
while True:
    element = input(f"Input a number: ")
    if element.isalpha():
        print(f"Not a number. Aborting input.")
        break
    else:
        array.append(int(element))

print(f"""Sum of elements in the list is: {sum_and_max_of(array)[0]}
Maximal element in the list is: {sum_and_max_of(array)[1]}""")
