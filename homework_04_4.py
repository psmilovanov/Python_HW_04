# Задание 4

first_list = [7, 8, 12, 7, 44, 44, 13, 9]
print(first_list)

final_list = [first_list[i] for i in range(len(first_list)) if (first_list.count(first_list[i]) == 1)]

print(final_list)
