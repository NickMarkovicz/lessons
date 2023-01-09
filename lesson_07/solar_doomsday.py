from random import randint
from math import floor


def solution(area):
    panels = [int(floor(area ** 0.5) ** 2)]
    area -= panels[0]
    if area == 0:
        return panels
    else:
        for i in range(int(area / 1)):
            panels.append(1)
    return panels


area = randint(1, 1000000)
print(f"Given area is: {area}")
print(f"Solar panels:", end=' ')
print(f"{solution(area).count((solution(area)[0]))}x: {solution(area)[0]}, {solution(area).count((solution(area)[1]))}x: {solution(area)[1]}")
