# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.


# Defining function
def numbers_qube(n):
    count, summary = 0, 0
    while count < n:
        count += 1
        for i in range(1, n + 1):
            summary += (i ** 3)
    return summary


# Calling out function for print
n = int(input(f"Input number: "))
print(numbers_qube(n))
