# Задание 6.
from random import randint
from itertools import count, cycle

x = int(input(
    "Введите целое положительное число. Программа выведет все числа, начиная с этого и до числа в три раза большим: "))

for el in count(x):
    if el > x * 3:
        break
    else:
        print(el)

first_list_len = randint(2, 10)
print(f"Формируем случаный список длины {first_list_len}")
first_list = []
for i in range(0, first_list_len):
    first_list.append(randint(1, 100))
print(first_list)
i = 0

for el in cycle(first_list):
    if i >= len(first_list):
        break
    else:
        print(el)
        i += 1
