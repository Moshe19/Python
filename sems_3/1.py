# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [int(x) for x in input('Введите список чисел через пробел:\n').split()]
sum = 0

for i in range(len(list)):
    if i%2 != 0:
        sum += list[i]

print(f'{list}\nСумма элементов данного списка, стоящих на нечетной позиции равна {sum}')     