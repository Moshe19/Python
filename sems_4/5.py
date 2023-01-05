#  Даны два файла, в каждом из которых находится запись многочлена. 
#  Задача - сформировать файл, 
#  содержащий сумму многочленов.

import glob
import re 


f1 = open('file_1.txt', 'r')
f2 = open('file_2.txt', 'r')
out = open('sum.txt', 'a')
summ = 0

pol_file = glob.glob("*.txt")

with open("result.txt", "wb") as pol:
    for f in pol_file:
        with open(f, "rb") as infile:
            pol.write(infile.read())

def convert_pol(pol): 
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range(len(pol)):
        if pol[i] == 'x':
            pol[i] = '1'
    pol = pol[::-1]
    return pol

numbers = pol.read() 
numbers = re.findall(r'[+-^]?\d+', numbers) 
numbers = [int(x) for x in numbers] 

for x in numbers:
    summ += x

out.write(str(summ)) 

f1.close()
f2.close()
out.close()