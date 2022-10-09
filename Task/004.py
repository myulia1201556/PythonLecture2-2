# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от -100 до 100) многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше 
# и так до ноля. Коэффициенты расставляет random, поэтому при коэффициенте 0 
# просто пропускаем данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


from random import choice


def polynomial(num: int):
    if num < 1:
        return 0

    poly = ""
    num_list = range(0, 10)

    with open("poly.txt", "a", encoding="utf-8") as my_f:
        for i in range(num, 0, -1):
            value = choice(num_list)
            if value:
                poly += f"{value}*x^{i} {choice('+-')} "

        my_f.write(f"{poly}{choice(num_list)} = 0\n")


for _ in range(3):
    polynomial(int(input()))