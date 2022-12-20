# Найти в списке ниже количество не уникальных элементов:
# my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]


# Defining function
def find_non_unique(my_list):
    my_set = set(my_list)
    return len(my_list) - len(my_set)


# Calling function
my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
print(f"Non-unique values: {find_non_unique(my_list)}")
