# Задание 2

from random import randint

first_list_len = randint(2, 10)
print(f"Формируем случаный список длины {first_list_len}")
first_list = []
for i in range(0, first_list_len):
    first_list.append(randint(1, 100))

print(f"Первоначальный список: {first_list}")

last_list = [first_list[i + 1] for i in range(len(first_list) - 1) if first_list[i + 1] > first_list[i]]

print(f"Требуемый список: {last_list}")
