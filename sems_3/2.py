#  Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from random import randint


number = int(input('Введите размер списка: '))
list = []
list_2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        result = list[i] * list[number]
        list_2.append(result)
        i += 1

print(list)
print(list_2)

