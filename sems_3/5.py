# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

def Fibonacci(n):
    if n in [1,2]:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        n1, n2 = 1, -1
        for i in range(2, n):
            n1, n2 = n2, n1 - n2
        return n2

list = [0]
k = int(input('Введите число: '))

for x in range(1, k+1):
    list.append(Fibonacci(x))
    list.insert(0, NegaFibonacci(x))

print(list)
