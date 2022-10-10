# Задайте последовательность цифр. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

from collections import Counter 
from random import randint

len_list = int(input("Введите количество элементов списка: "))


def creat_list(len_list):
    return [randint(-len_list, len_list) for i in range(len_list)]


input_list = creat_list(len_list)
output_list = [len_list for len_list, v in Counter(input_list).items() if v == 1]

print(input_list)
print(output_list)


# import random

# print("Введите число элементов списка: ")
# len_list = int(input())
# list = []

# if len_list < 0:
#        print("Error")
      
# for i in range (len_list):
#     list.append(random.randint(1, len_list))
# print(list)


# def uniq_elem(list):
    
#     result = []
#     dict = {}.fromkeys(list, 0)

#     for i in list:
#         dict[i] += 1

#     for j in dict:
#         if dict[j] == 1:
#             result.append(j)

#     return result

# print(uniq_elem(list))
