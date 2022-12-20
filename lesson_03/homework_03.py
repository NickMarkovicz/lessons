# Пользователь делает вклад в размере 2130 рублей сроком на 5 лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Рассчитать сумму на счету пользователя по окончании вклада и вывести на печать,
# если в конце каждого года ему начисляется бонус в размере 120 рублей.


# Importing "sleep" for a e s t h e t i c
from time import sleep


# Defining function
def deposit(money, years):
    for i in range(years):
        money += (money * 0.1) + 120

    return money


# Asking info required to do calculations
money = int(input(f"Input amount of $ for deposit: "))
years = int(input(f"Input years for depositing: "))
# Showing user the info
print(f"Calculating...")
sleep(2)
print(f"You will have ${deposit(money, years)} in {years} years")
