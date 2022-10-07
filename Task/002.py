# Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.


def prime_list(num):
    list = []
    div = 2
    while num > 1:
        if num % div == 0:
            list.append(div)
            num //= div
        else:
            div += 1
    return list        


print("Задайте натуральное число:")
print(prime_list(int(input())))
