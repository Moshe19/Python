# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

def write_file(st):
    with open('file_1.txt', 'w') as data:
        data.write(st)

max_val=100
k = int(input('Введите натуральную степень k: '))

koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
poly_1=' + '.join([f'{(j," ")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])

poly_1=poly_1.replace('x^1 + ', ' x + ')
poly_1=poly_1.replace('x^0 ', ' ')
poly_1+=(' ','1')[poly_1[-1]==' +']
poly_1=(poly_1, poly_1[:-2])[poly_1[-2:]==' ^1']

print(poly_1+'= 0')
write_file(poly_1+'= 0')

# код для второго многочлена для 5 задачи

def write_file(st):
    with open('file_2.txt', 'w') as data:
        data.write(st)

max_val=100
k = int(input('Введите натуральную степень k: '))

koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
poly_2=' + '.join([f'{(j," ")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])

poly_2=poly_2.replace('x^1 + ', ' x + ')
poly_2=poly_2.replace('x^0 ', ' ')
poly_2+=(' ','1')[poly_2[-1]==' +']
poly_2=(poly_2, poly_2[:-2])[poly_2[-2:]==' ^1']

print(poly_2+'= 0')
write_file(poly_2+'= 0')