# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите количество чисел в последовательности: '))

num = []

for i in range(1, n+1):
    input_value = int(input(f'Введите число {i}: '))
    num.append(input_value)

sum = 0
for i in num:
    sum += i

print(num)
print('Сумма всех чисел последовательности:', sum)