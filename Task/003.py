# Задайте последовательность цифр. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


import random

def InputNum(inputText):
    is_Ok = False
    while not is_Ok:
        try:
            number = int(input(f'{inputText}'))
            is_Ok = True
        except ValueError:
            print('Введено не число!')
    if number > 0:
        return number
    else:
        print('Negative value of the number of numbers!')

def NewList(number):
    l = []
    i=0
    print(f'Лист: ', end='')
    while i < number:
        l.append(random.randint(1, 9))
        i += 1
    print(l)
    i = 0
    new_list = []
    while i < number:
        ind = l.index(l[i])
        try:
            ind2 = l.index(l[i], ind+1, number)
        except ValueError:
            new_list.append(l[i])
        i += 1
    print('Неповторяющиеся числа:')
    print(new_list)


number = InputNum('Введите число: ')
NewList(number)