# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

# from random import choice


# def poly_sum(name_1: str, name_2: str):
#     with open(name_1, "r", encoding="utf-8") as my_f_1, \
#             open(name_2, "r", encoding="utf-8") as my_f_2:
#         first = my_f_1.readlines()
#         second = my_f_2.readlines()

#         if len(first) == len(second):
#             with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
#                 for i, v in enumerate(first):
#                     my_f_3.write(f"{v[:-5]} + {second[i]}")
#         else:
#             print("The contents of the files do not match!")


# # poly_sum(input("Enter the file name 'poly.txt': "), input("Enter the file name 'poly_2.txt': "))
# poly_sum("poly.txt", "poly_2.txt")


from random import randint as rI

def createCoef():
    coef = {}
    degree = int(input("Введите максимальную степень: "))
    for i in range(degree, -1, -1):
        coef[i] = rI(-20,20)
    return coef


def createEquation(coefEquation: dict):
    equation = ''
    first = True

    for i in coefEquation.items():
        if first:
            first = False
            if i[1] < 0:
                equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

    return equation + ' = 0'

def parseEquation(equation: str):
    equation = equation.replace(' + ', ' +').replace(' - ', ' -')
    equation = equation.split()
    equation = equation[:-2]

    dictEquation = {}
    for i in range(len(equation)):
        equation[i] = equation[i].replace('+', '').split('x^')
        dictEquation[int(equation[i][1])] = int(equation[i][0])
    return dictEquation

equation1 = createEquation(createCoef())
equation2 = createEquation(createCoef())

parEq1 = parseEquation(equation1)
parEq2 = parseEquation(equation2)

resultEquation ={}
for i in range(max(len(parEq1), len(parEq2)), -1, -1):
    first = parEq1.get(i)
    second = parEq2.get(i)
    if first != None or second != None:
        resultEquation[i] = (first if first != None else 0) + (second if second != None else 0)

def printEquation(equation: str):
    print(equation.replace(" 1x", "x").replace("x^1", 'x').replace("x^0", ''))

printEquation(createEquation(parEq1))
printEquation(createEquation(parEq2))
printEquation(createEquation(resultEquation))