# Importing
from random import randint
from math import floor


# Defining function
def solution(area):
    panels = [int(floor(area ** 0.5) ** 2)]  # Making a list with one element inside: the largest square possible
    area -= panels[0]  # Subtracting the largest square out of total area
    if area == 0:
        return panels  # Returning list as is, if area is a perfect square
    else:
        for i in range(int(area / 1)):  # Filling up empty space with 1x1 solar panels
            panels.append(1)
    return panels


area = randint(1, 1000000)
print(f"Given area is: {area}")
print(f"Solar panels:")
print(f"""Square of {solution(area)[0]} tiles: {solution(area).count((solution(area)[0]))}x
Square of {solution(area)[1]} tiles: {solution(area).count((solution(area)[1]))}x""")  # Largest square + 1x1 squares
