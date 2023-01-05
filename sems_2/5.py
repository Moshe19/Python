# Реализуйте алгоритм перемешивания списка.

import random
def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list
n = int(input('Задайте длинну списка: '))
list = []
for i in range(1, n+1):
    input_value = int(input(f'Введите число {i}: '))
    list.append(input_value)
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)