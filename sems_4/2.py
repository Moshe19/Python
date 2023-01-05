#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите число N: '))
list = []
i = 2
num = N
while i <= N:
    if N%i == 0:
        list.append(i)
        N //= i
    else:
        i += 1

print(f'Простые множители числа {num}: {list}')