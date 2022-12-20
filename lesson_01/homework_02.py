# Создать список, состоящий из отдельных единичных символов,
# преобразовать список в строку, инвертировать строку и вывести на печать.


# Defining function
def list_to_string(array):
    return "".join(array)


# Creating array of length 5
array = [input(f"Input element #{i} out of 5: ") for i in range(1, 5 + 1)]

# Calling for print
print(f"Your list as a string: {list_to_string(array)}")
