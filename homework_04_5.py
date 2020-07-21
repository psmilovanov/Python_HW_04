# Задание 5

from functools import reduce


def my_multiplcation(el, next_el):
    return el * next_el


list = [el for el in range(100, 1001) if (el % 2 == 0)]

print(reduce(my_multiplcation, list))
