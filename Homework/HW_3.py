# 1 задание
#
# num = input('Введите количество символов: ')
# typ = input('Введите тип символа: ')
# orc = int(input('0 - горизонтальная\n1 - вертикальная\nВыберите ориентацию линий:  '))
# try:
#     num = int(num)
#     if orc == 0:
#         print(typ * num)
#     elif orc == 1:
#         i = 0
#         while i < num:
#             print(typ)
#             i += 1
#     else:
#         print('Ошибка. Можно вводить только 0 и 1')
# except:
#     print('Ошибка ввода')
#
# # 2 задание
#
# symbol1 = input('Введите первый символ: ')
# symbol2 = input('Введите второй символ: ')
# vvod1 = int(input('Введите ширину прямоугольникa: '))
# vvod2 = int(input('Введите высоту прямоугольникa: '))
# s1 = 0
# s2 = 0
# if vvod2 % 2 == 1:
#     print(symbol1 * vvod1)
#     while s1 < vvod2 / 2 - 1:
#         print(symbol2 * vvod1)
#         print(symbol1 * vvod1)
#         s1 += 1
#         s2 += 1
# else:
#     while s1 < vvod2 / 2:
#         print(symbol1 * vvod1)
#         s1 += 1
#         print(symbol2 * vvod1)
#         s2 += 1


# 3 задание

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
#
# a = num1 if num2 < num1 else num2 if num2 > num3 else num3
# print('Максимальное значение: ', a)

# 4 задание

# try:
#     oper = int(input('Выберите операцию: \n1 - "r" - применяет унарный минус к операнду\n2 - "+" - сложение'
#                  '\n3 - "-" - вычитание\n4 - "/" - деление\n5 - "*" - умножение'
#                  '\n6 - "%" - деление по модулю(остаток от деления)\n7 - "<" - минимальное из двух чисел'
#                  '\n8 - ">" - максимальное из двух чисел\nВведите цифру: '))
#     if oper == 1:
#         num1 = int(input("Введите число: "))
#         print(-num1)
#     elif 1 < oper <= 8:
#         num1 = int(input("Введите первое число: "))
#         num2 = int(input("Введите второе число: "))
#         if oper == 2:
#             print(num1 + num2)
#         elif oper == 3:
#             print(num1 - num2)
#         elif oper == 4:
#             print(num1 / num2)
#         elif oper == 5:
#             print(num1 * num2)
#         elif oper == 6:
#             print(num1 % num2)
#         elif oper == 7:
#             print(num1 if num1 < num2 else num2)
#         elif oper == 8:
#             print(num1 if num1 > num2 else num2)
#     else:
#         print('Ошибка при выборе операции')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except:
#     print('Ошибка ввода')

# Дополнительное зада

# size = int(input('Введите размер поля: '))
# symbol = int(input('Введите количество символов: '))
# i = 0
# if size % 2 == 1:
#     j = 0
#     while j < symbol:
#         print('*' * symbol, end = '')
#         print()
#         j += 1
#     while i < size:
#         q = 0
#         while q < symbol:
#             print(' ' * symbol, end = '')
#             print()
#             print('*' * symbol, end='')
#             print()
#             q += 1
#         i += 1
# else:
#     while i < size:
#         print(' ' * symbol, end = '')
#         print()
#         i += 1

