# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001


from decimal import Decimal


def required_accuracy(count):
    print("Enter the required accuracy '0.0001':")
    count = count.quantize(Decimal(input()))
    print(count)

print ('Enter a real number:')
required_accuracy(Decimal(input()))