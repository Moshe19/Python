# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

list = [int(x) for x in input('Задайте список чисел через пробел:\n').split()]

new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)

print(new_list)
