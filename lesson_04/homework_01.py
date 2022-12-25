# Дан список my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], выведите все элементы, которые меньше 5.


# Defining function
def print_more_than_five():
    # Defining required vars
    array = []
    count = 0
    while True:  # Cycle to check if the input is correct
        count += 1
        element = input(f"Input number #{count} or 'stop' to abort inputting: ")
        if element != 'stop':
            if element.isnumeric():
                element = int(element)
                array.append(element)
            else:
                while True:  # If the input is wrong, the message about wrong input is sent until the input is correct
                    element = input(f"Wrong input! Input a number or 'stop' to stop inputting: ")
                    if element.isnumeric() or element == 'stop':
                        element = int(element)
                        array.append(element)
                        break
                    else:
                        continue
        elif element == 'stop':  # Stopping input at command
            print(f"Input aborted.")
            break

    final_list = []  # Forming a list of element > 5
    for i in range(len(array)):
        if array[i] < 5:
            final_list.append(array[i])

    return final_list


# Calling out function for print
print(f"List of elements < 5: {print_more_than_five()}")
