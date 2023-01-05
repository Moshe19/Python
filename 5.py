# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def inputNumbers(x):
    xy = ["x", "y"]
    a = []
    for i in range(x):
        number  = False
        while not number:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                number = True
            except ValueError:
                print("Введите целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5) 
    lengthSegment = int(lengthSegment * 100) 
    lengthSegment = float(lengthSegment/100) 
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")