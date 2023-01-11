# Задана натуральная степень k. Сформировать случайным образом список \
#     коэффициентов (значения от 0 до 100) многочлена и записать в файл \
#         многочлен степени k.
# Пример:
#     k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0.

import random


def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 101)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))




# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def replace(equation):
    dict = {}
    equation = equation.replace(' - ', ' -').replace(' + ', ' +')
    equation = equation.split()
    equation = equation[:-2]
    for i in range(len(equation)):
        equation[i] = equation[i].replace('+', '').split('x**')
        dict[int(equation[i][1])] = int(equation[i][0])
    return dict

def sumEquation(dict1, dict2):
    dictResult = {}
    maximum = (max(max(dict1), max(dict2)))
    for i in range(maximum, -1, -1):
        first = dict1.get(i)
        second = dict2.get(i)
        if first != None or second != None:
            dictResult[i] = (first if first != None else 0) + (second if second != None else 0)
    return dictResult

def result(dictResult):
    result = ''
    for i in dictResult.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + 'x^' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
        result = result.replace('x^1', 'x').replace('x^0', '').replace('1x^', 'x^')
    return result + ' = 0'


with open('file1.txt', 'r', encoding='utf-8') as text:
    equation = text.readline()
with open('file2.txt', 'r', encoding='utf-8') as text:
    equation2 = text.readline()

print(equation)
print(equation2)

dict1 = replace(equation)
dict2 = replace(equation2)

dictResult = sumEquation(dict1, dict2)
print(dictResult)

print(dict1)
print(dict2)

dictResult = result(dictResult)
print(dictResult)

with open('file3.txt', 'w', encoding='utf-8') as text:
    text.writelines(dictResult)

