# task 1
from math import sqrt, pi
from random import randint

# try:
#     figure = int(input('Выберитe фигуру: \n1-Треугольник\n2-Прямоугольник\n3-Круг\n:'))
#     for i in range(1,4):
#         if figure == 1:
#             a = int(input('Введите сторону a: '))
#             b = int(input('Введите сторону b: '))
#             c = int(input('Введите сторону c: '))
#             p = (a + b + c) / 2
#             print('Площадь треугольника = ', round(sqrt(p * (p - a) * (p - b) * (p - c)), 2))
#             break
#         elif figure == 2:
#             a = int(input('Введите сторону a: '))
#             b = int(input('Введите сторону b: '))
#             print('Площадь прямоугольника = ', round(a * b, 1))
#             break
#         elif figure == 3:
#             r = int(input("Введите радиус окружности: "))
#             print('Площадь круга = ', round(pi * r**2, 2))
#             break
#         else:
#             print('Вводить цифрты только 1, 2 или 3!')
#             break
# except:
#     print('Ошибка, вводить только цифры от 1 до 3')

# 2 task
#
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# for i in matrix:
#     for j in i:
#         print(j, end='\t')
#     print()
#
# print('\n')
# for j in range(4):
#     for i in range(3):
#         print(matrix[i][j], end='\t')
#     print()

# 3 task
# w = h = 6
# matrix = [[randint(0, 10) for x in range(w)] for y in range(h)]
#
# for i in matrix:
#     for j in i:
#         print(j, end='\t')
#     print()
#
# list = [randint(0, 10) for i in range(6)]
# print(list)
# print('\n')
#
#
# for i in range(len(matrix)):
#     if i % 2 == 0:
#         matrix[i].clear()
#         for j in list:
#             matrix[i].append(j)
#         for q in matrix[i]:
#             print(q, end='\t')
#         print()
#     else:
#         for o in matrix[i]:
#             print(o, end='\t')
#         print()




