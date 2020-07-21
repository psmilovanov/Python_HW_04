# Задание 7




def fact(n):
    k = 1
    for el in range(n):
        k *= (el + 1)
        yield k


n = int(input("Введите число n: "))

for el in fact(n):
    print(el)
