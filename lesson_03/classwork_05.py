# Создать переменную, содержащую сторону квадрата,
# создать новый список, в котором будут:
# 1. Периметр квадрата;
# 2. Площадь квадрата;
# 3. Диагональ квадрата.


# Importing square root from math
from math import sqrt


# Defining function
def mathematics(a):
    return a * 4, a ** 2, a * sqrt(2)


# Defining var "a"
a = int(input("Input size of a square's side: "))

# Calling different tuple elements of "mathematics" function return result for print
print(f"""Perimeter: {mathematics(a)[0]}
Square: {mathematics(a)[1]}
Diagonal: {mathematics(a)[2]}""")
