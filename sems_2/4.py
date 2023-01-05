# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
with open('file.txt','r') as position:
    while True:
        s = input('Укажите позицию для вычисления: ')
        if s == '':
            break
        position.write(f'{s}\n')
    position.close()
    result = 1
    f = open('file.txt', 'r')
    for line in f:
        if line == '':
            break
        result = numbers[int(f.readline())] * numbers[int(f.readline(2))]
    f.close()

print(result)