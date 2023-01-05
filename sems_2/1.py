# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def sum_digits(numbers):
  return sum(map(int, numbers.replace('.','').replace('-','').replace(',','')))

numbers = input('Введите любое число: ')
print(f'Сумма цифр в числе {numbers} равнва: {sum_digits(numbers)}')