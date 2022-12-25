# Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры.


# Defining function
def sum_of_cubes(n, m):
    return sum(range(n, m + 1))


n, m = int(input(f"Input number #1: ")), int(input(f"Input number #2: "))
# Calling out function for print
print(f"Sum of cubes of all numbers from {n} to {m} is: {sum_of_cubes(n, m)}")
