# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001


from decimal import Decimal

number = input("Введите число: ")
d = input("Введите число с точностью d: ")

def num_precision(num, d):
    num = Decimal(num)
    num = num.quantize(Decimal(d))

    return num

print(num_precision(number, d))    

# from math import pi
# from decimal import Decimal

# num = str(pi)  в данном случае программа работает над числом пи
# num = input("Введите число: ") программа работает с заданным числом пользователя
# d = input("Введите число с точностью d: ")

# print(Decimal(num).quantize(Decimal(d)))

