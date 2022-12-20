# Найти значение выражений:
# x = 17 / 2 * 3 + 2
# x = 2 + 17 / 2 * 3
# x = 19 % 4 + 15 / 2 * 3
# x = (15 + 6) - 10 * 4
# x = 17 / 2 % 2 * 3

# Расставить скобки так, чтобы значение выражений поменялось.
# Создать три переменные, содержащие возраст трех ваших друзей,
# в качестве имен переменных использовать имена друзей, найти сумму и вывести ее на экран.
# Создать еще одну переменную равную среднему арифметическому возрасту, и вывести это значение на экран.


# Defining function
def classwork_01():
    # Creating default values
    a, b, c, d, e = (17 / 2 * 3 + 2), (2 + 17 / 2 * 3), 19 % 4 + 15 / 2 * 3, ((15 + 6) - 10 * 4), (17 / 2 % 2 * 3)
    print(f"Old numbers: {a, b, c, d, e}")
    print()

    # Changing default values
    a, b, c, d, e = (17 / (2 * 3) + 2), (2 + 17 / (2 * 3)), 19 % (4 + 15) / 2 * 3, (((15 + 6) - 10) * 4), (
                17 / 2 % (2 * 3))
    print(f"New numbers: {a, b, c, d, e}")
    print()

    # Creating "friends" var
    friend_1, friend_2, friend_3 = 22, 34, 66
    average = (friend_1 + friend_2 + friend_3) / 3
    print(f"Average age is: {average}")
    print()


# Calling 'classwork_01' function
classwork_01()
