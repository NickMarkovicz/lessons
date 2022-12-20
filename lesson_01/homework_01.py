# Дано выражение x = 2 + 2 * 2 - 2 / 2,
# расставить скобки таким образом, чтобы значение x было равно 2,
# найти два варианта решения задачи.


# Defining function as the first solution
def equals_two_option1():
    return (2 + 2 * 2 - 2) / 2


# Defining function as the second solution
def equals_two_option2():
    return (2 + (2 * 2 - 2)) / 2


# Calling function "equals_two_option2" for print
print(f"""First solution result: {int(equals_two_option1())}
Second solution result: {int(equals_two_option2())}""")
