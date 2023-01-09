# Написать функцию, которая будет вызывать задержку выполнения программы случайным образом от 1 до 5 секунд.
# Написать декоратор, который будет выводить на печать время выполнения этой функции (end_time - start_time).

# Importing
from time import sleep
from random import randint
from datetime import datetime


# Defining decorator
def decorator(func):
    def exec_time():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        print(end_time - start_time)
    return exec_time


# Defining function
@decorator
def delayed():
    sleep(randint(1, 5))
    print(f"Hi")


if __name__ == "__main__":
    delayed()

