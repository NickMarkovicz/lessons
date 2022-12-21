# Найти значение выражений:
# x = 17 / 2 * 3 + 2
# x = 2 + 17 / 2 * 3
# x = 19 % 4 + 15 / 2 * 3
# x = (15 + 6) - 10 * 4
# x = 17 / 2 % 2 * 3

# Расставить скобки так, чтобы значение выражений поменялось.


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


# Calling 'classwork_01' function
classwork_01()
