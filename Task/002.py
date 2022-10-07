# Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.


def prime_factors(count):
    factors = list()
    while count % 2 == 0 or count % 3 == 0 or count % 5 == 0:
        if count % 2 == 0:
            factors.append(2)
            count /= 2
        elif count % 3 == 0:
            factors.append(3)
            count /= 3
        elif count % 5 == 0:
            factors.append(5)
            count /= 5
    if count > 1:
        factors.append(round(count))
    print(f'Простые множители числа N:', factors)

print('Задайте натуральное число N:')
prime_factors(int(input()))