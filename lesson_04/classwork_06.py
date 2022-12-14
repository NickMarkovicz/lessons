# Вывести в порядке возрастания все простые числа,
# расположенные между n и m (включая сами числа n и m), а также количество x этих чисел.


# Defining function
def increasing_numbers(n, m):
    array = []
    for i in range(n, m + 1):
        count = 0
        for k in range(2, i + 1):
            if i % k == 0:
                count += 1
        if count == 1:
            array.append(i)

    return array


# Calling out function for print
n, m = int(input(f"Input number #1: ")), int(input(f"Input number #2: "))
print(f"Wrong numbers!") if n > m else print(f"""You sorted list: {sorted(increasing_numbers(n, m))}
Amount of numbers is: {len(increasing_numbers(n, m))}""")
