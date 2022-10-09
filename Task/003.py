# Задайте последовательность цифр. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


import random

print("Введите число элементов списка: ")
len_list = int(input())
list = []

if len_list < 0:
       print("Error")
      
for i in range (len_list):
    list.append(random.randint(1, len_list))
print(list)


def uniq_elem(list):
    
    result = []
    dict = {}.fromkeys(list, 0)

    for i in list:
        dict[i] += 1

    for j in dict:
        if dict[j] == 1:
            result.append(j)

    return result

print(uniq_elem(list))

# import numpy 

# from collections import Counter 

# items = numpy.random.randint(10, size = 10)
# items_set = list(items[:10])
# print(*items_set)

# dictionary = Counter(items_set)
# result = [i for i in dictionary if dictionary[i] == 1]

# print(*result)
# не работает