# Задание 1.

from sys import argv


def salary(productivity, salary_per_hour, bonus):
    return round(float(productivity) * float(salary_per_hour) + float(bonus), 2)

try:
    file, productivity, salary_per_hour, bonus = argv
except ValueError:
    print("Неправильно введены параметры")
    exit()

sal = salary(productivity, salary_per_hour, bonus)

print(f"Зарплата = {sal}")
