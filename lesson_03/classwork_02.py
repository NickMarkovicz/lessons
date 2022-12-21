# Создать три переменные, содержащие возраст трех ваших друзей,
# в качестве имен переменных использовать имена друзей, найти сумму и вывести ее на экран.
# Создать еще одну переменную равную среднему арифметическому возрасту, и вывести это значение на экран.


# Defining function
def average_age(friends):
    return sum(friends) / 3


# Creating "friends" var
friends = [int(input(f"Input age of friend #{i}: ")) for i in range(1, 3 + 1)]
print(f"Average age is: {int(average_age(friends))} years")
