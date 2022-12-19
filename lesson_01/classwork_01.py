def task_01():

    # Creating default values
    a, b, c, d, e = (17 / 2 * 3 + 2), (2 + 17 / 2 * 3), 19 % 4 + 15 / 2 * 3, ((15 + 6) - 10 * 4), (17 / 2 % 2 * 3)
    print(f"Old numbers: {a, b, c, d, e}")
    print()

    # Changing default values
    a, b, c, d, e = (17 / (2 * 3) + 2), (2 + 17 / (2 * 3)), 19 % (4 + 15) / 2 * 3, (((15 + 6) - 10) * 4), (17 / 2 % (2 * 3))
    print(f"New numbers: {a, b, c, d, e}")
    print()

    # Creating "friends" var
    friend_1, friend_2, friend_3 = 22, 34, 66
    average = (friend_1 + friend_2 + friend_3) / 3
    print(f"Average age is: {average}")
    print()

task_01()