# Написать функцию month_to_season(), которая принимает 1 аргумент: номер месяца,
# и возвращает название сезона, к которому относится этот месяц. Например, передаем 2, на выходе получаем "Winter".


# Defining function
def month_to_season(num):
    year = {
        "Winter": [12, 1, 2],
        "Spring": [3, 4, 5],
        "Summer": [6, 7, 8],
        "Autumn": [9, 10, 11]
    }

    for season, month in year.items():
        if num in month:
            return season


# Month
num = int(input(f"Input month number: "))
# Calling out function for print
print(f"{month_to_season(num)}")
