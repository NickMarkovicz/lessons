# Дан список стран и городов каждой страны, где ключи - это названия стран, а значения - списки городов в этих странах.
# Написать функцию, которая осуществляет поиск по городу и возвращает страну.
# Оформить в виде программы, которая считывает название города и выводит на печать страну.


# Defining function
def find_country(my_city):
    print(f"Inputted city: {my_city}")
    for country, city in cities.items():
        if my_city in city:
            return country


# Defining required vars
cities = {
    "Canada": ["Toronto", "Vancouver", "Montreal", "Ottawa", "Winnipeg"],
    "USA": ["Los Angeles", "New York", "Washington", "San Francisco", "Las Vegas"]
}


# Calling out function for print
print(f"Country your city located in: {find_country('Toronto')}")
