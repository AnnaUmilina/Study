# name = "Anna"
# print("Hello", name)
# age = 24
# print(age)
# print(id(age))
import random
# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, 'Hello', 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)

# a = '6'
# b = 2
# print(int(a) + b)

# a = 1
# b = 2
# print('a =', a)
# print('b =', b)
# c = a
# a = b
# b = c
# a = a + b
# b = a - b
# a = a - b

# summa = 5 + 7 + 3
# pr = 5 * 7 * 3
# sr = (5 + 7 + 3)/3
# print('Сумма: ', summa, '\nПроизведение: ', pr,  '\nСреднее арифметическое: ', sr)


# num = 4321
# a = num % 10
# print(a)
# b = (num // 10) % 10
# print(b)
# c = (num // 100) % 10
# print(c)
# d = (num // 1000) % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)
#
# num1 = '2'
# num2 = 3
# res = num1 + str(num2)
# print(res)


# print(int(3.8))
# print(round(3.8))
# print(round(3.891, 2))

# name = 'Виктор'
# age = 28
# print('Меня зовут ' , name ,'. мне' , age , 'лет', sep='--')
# print('Я учу Python.')

# name = input('Введите ваше имя: ')
# print('Hello', name)

# a = input('Введите число: ')
# b = input('Укажите степень: ')
# res = int(a)**int(b)
# print(res)

# b1 = True
# b2 = False
# print(b1 + 5)

# print(bool('Python'))
# print(bool('')) # False
# print(bool(' ')) # True

# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input('Введите совй возраст: '))
# if age >= 18:
#     print('Доступ на сайт разрешен')
# else:
#     print('Доступ запрещен')

# a = 15
# b = 5
# if a > b:
#     print('a > b')
# elif b > a:
#     print('a < b')
# else:
#     print('a == b')

# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or b == c or a == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# day = int(input('Введите день недели цифрой: '))
# if day >= 1 and day <= 5:
#     print('рабочий день - ', end='')
#     if day == 1:
#         print('понедельник')
#     if day == 2:
#         print('вторник')
#     if day == 3:
#         print('среда')
#     if day == 4:
#         print('четверг')
#     if day == 5:
#         print('пятница')
# elif day == 6 or day == 7:
#     print('выходной день - ', end='')
#     if day == 6:
#         print('суббота')
#     if day == 7:
#         print('воскресенье')
# else:
#     print('такого дня недели не сущетсвует')

# month = int(input('Введите номер месяца (цифрой): '))
# if month == 12 or month == 1 or month == 2:
#     print('Зима')
# elif 3 <= month <= 5:
#     print('Весна')
# elif 6 <= month <= 8:
#     print('Лето')
# elif 9 <= month <= 11:
#     print('Осень')
# else:
#     print('Ошибка ввода данных')

# n = int(input('Сколько ворон на ветке от 0 до 9: '))
# if 0 <= n <= 9:
#     print('На ветке ', n, end='')
#     if n==1:
#         print(' ворона')
#     elif 2<=n<=4:
#         print(' вороны')
#     elif 5<=n<=9 or n == 0:
#         print(' ворон')
# else:
#     print('Ошибка ввода')

# password = 'moderato'
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print('Пароль не верен')

# day = 'вторник'
# time = 16
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 10, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = int(input('Введите 1 число'))
# b = int(input('Введите 2 число'))
# print(a // b if b != 0 else 'На нуль делить нельзя')

# a = 0
# b = '2a'
# print(a + int(b))

# try:
#     n = int(input('Введите целое число: '))
#     print(n * 2)
# except ValueError:
#     print('Что то пошло не так')

# zn1 = int(input('Введите первое число: '))
# zn2 = int(input('Введите второе число: '))
# try:
#     print(zn1 + zn2)
# except ValueError:
#     print(zn1 + zn2)

# i = 0
# while i < 5:
#     print('i = ', i)
#     i += 1

# i = 2
# while i <= 20:
#     print('i = ', i)
#     i += 2


# x = int(input('Введите количество символов: '))
# i = 0
# while i < x:
#     print('*', end='')
#     i += 1

# try:
#     x = int(input('Количество: '))
#     while x > 0:
#         print('*', end='')
#         x -= 1
# except ValueError:
#     print('Введите число!')

# a = int(input('Начало диапазона: '))
# b = int(input('Конец диапазона: '))
# if a % 2 == 0:
#     a += 1
# sum1 = 0
# while a <= b:
#     sum1 += a
#     a += 2;
# print('Сумма нечетных: ', sum1)

# n = input('Введите целое число: ')
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число: ')
# if n % 2 == 0:
#     print('Четное число!')
# else:
#     print('Нечетное число!')

# i = 0
# while i < 10:
#     if i == 3:
#         i+= 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input('Введите положительное число: '))
#     if n < 0:
# #         break
# m = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     m *= n
# print(m)

# i = 0
# while i < 10:
#     print(i)
#     i +=1
# else:
#     print('Цикл окончен, i = ', i)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print(' Внутренний цикл: j =', j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     print()
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j,'\t\t', end='')
#         j += 1
#     i += 1

# for i in 'Hello', 'red', 'black', 'yellow':
#     print(i)

# print(range(5))

# for i in range(5, 100, 5):
#     print(i, end=' ')
# print()
#
# i = 5
# while i < 100:
#     print(i, end=' ')
#     i += 5

# x = int(input('Введите целое число: '))
# for i in range(1, x+1):
#     if x % i == 0:
#         print(i, end=' ')


# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('-----')

# w = int(input('Введите ширину прямоугольника: '))
# h = int(input('Введите высоту прямоугольника: '))
# for i in range(h):
#     for j in range(w):
#         print('*', end='')
#     print()

# w = int(input('Введите ширину прямоугольника: '))
# h = int(input('Введите высоту прямоугольника: '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# letter = [i for i in "Hello"]
# print(letter)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# s = []
# print(s)
# b = list()
# print(b)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)

# n = list(range(10))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# n = 5
# a = [i * 3 for i in 'Hello']
# print(a)

# a = [0] * int(input('Введите количество элементов списка: '))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('-> '))
# print(a)

# a = [input('-> ')for i in range(int(input('Введите количество элементов списка: ')))]
# print(a)

# nums = [8, 3, 9, 5, 7]
#
# for i in range(len(nums)):
#     print(nums[i], end=' ')
# print()
# for i in nums:
#     print(i, end=' ')

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов списка: ')))]
# summa = 0
# for i in a:
#     if i < 0:
#         summa += i
# print('Сумма отрицательных элементов: ', summa)

# a = list(range(21, 41))
# print(a)
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         odd += 1
#     else:
#         even += i
# print('Четных: ', odd, '\nНечетных: ', even)

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = input('-> ')
#     s.append(x)
# print(s)

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3:  '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3 без остатка')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c= []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 2, 4]
# c = []
#
# if len(b) > len(a):
#     a, b = b, a
#         for i in range(len(a)):
#             c.append(a[i])
#             c.append(b[i])
#         for i in range(len(a), len(b)):
#             c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)


# n = [int(input('Количество элементов списка: '))]
# for num in range(n):
#     x = int(input('-> '))
# ind = int(input('Введите индекс: '))
# n.pop(ind)
# print(n)

# a = [1, 3, 2, 9, 7, 2, 4, 2]
# num = a.count(2)
# print(num)
# ind = a.index(9)
# print(ind)

# import random
#
# print(random.random())
# print(random.randint(2, 9))
# print(random.randrange(9))

# import random as r

# mas = [r.randint(30, 100) for i in range(10)]
# print(mas)

# lst = [4, 5, 2, 7, 4]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# s = [8, 9, 6, 4, 5, 6, 2, 4, 6, 8, 9]
# res = []
#
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
#
# print(res)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)

# lst = []
# # if len(lst) == 0:
# if not lst:
#     print('Список пуст')

from random import randint

# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print('Первый список: ', a)
# print('Второй список: ', b)
# c = a + b
# print('Третий список: ', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print('Элементы двух списков без повторения: ', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print('Список с общими элементами: ', c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# n = int(input("Размер списка: "))
# s = []
# while len(s) < n:
#     num = random.randrange(n)
#     if num not in s:
#         s.append(num)
# print(s)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # print(m)
# # print(m[1][2])
#
# # for row in range(len(m)):
# #     for col in range(len(m[row])):
# #         print(m[row][col], end='\t')
# #     print()
#
# # for row in m:
# #     for col in row:
# #         print(col, end='\t')
# #     print()
#
# w, h = 5, 3
# # matrix = [[x * y for x in range(w)] for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y)

# w, h = 5,3
# matrix = [[randint(10, 100) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# w, h = 3, 4
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print('Количество отрицательных элементов: ')

# w = h = 6
# n = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
#
# s = []
# m = 101
# for i in range(w):
#     s.append(matrix[i][i])
#     if m > matrix[i][i]:
#         m = matrix[i][i]

#
# import math
#
# num1 = math.sqrt(2)

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
#
#
#
# print(time.strftime('%B %d, %Y')

# text = input('Название напоминания: ')
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)


# def hello(name):
#     print('d', name)
#
#
# hello('ira')


# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(2, 5)


# def symbol(count, a, b):
#     # print((a+b) * (count // 2) + a * (count % 2))
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#     # print("".join([a if i % 2 == 0 else b for i in range(count)]))
#
#
# symbol(9, '-', '+')


# def check_password(password):
#     has_upper = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#
#     if len(password) >= 8 and has_upper:
#         return True
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Этот пароль надежный')
# else:
#     print('Это ненадежный пароль')

# def cube(a):
#     return a * a * a
#
#
# for i in range(1,11):
#     print(i, 'в кубе =', cube(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.insert(0, end)
#     lst.append(start)
#     return lst
#
#
# print(change([1,2,3]))
# print(change([9,12,33,54,105]))
# print(change(['s','l','o','n']))


# def get_sum(a, b, c, d):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 7))

# import time
#
# res = time.localtime()
# print(res)

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]

# lst = [10,20,30]
# tpl = (10, 20, 30)

# from random import randint
#
# s = tuple(randint(1, 30) for i in range(20))
# print(s)
#
# w = tuple(2 ** i for i in range(1,13))
# print(w)

# t1 = tuple('Hello')
# t2 = tuple('world')

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1 ) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tuple_parse(tup, num):
#     if not num in tup:
#         return tuple()
#     first = tup.index(num)
#     if not num in tup[first + 1:]:
#         return tup[first:]
#     last = tup.index(num, first + 1)
#     return tup[first:last + 1]
#
#
# print(tuple_parse((1, 2, 3), 8))
# print(tuple_parse((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(tuple_parse((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
#
#
# def tpl_sum(a, b):
#     return tuple(randint(a, b) for i in range(12))
#
#
# t1 = tpl_sum(0, 5)
# print(t1)
# t2 = tpl_sum(-5, 0)
# print(t2)
# print(t1 + t2, (t1 + t2).count(0))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))

# a = list(range(2))
# print(a)
# print(a.__sizeof__())
# b = list(range(100))
# print(b)
# print(b.__sizeof__())


# def get_user():
#     name = 'Noy'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# name1, age1, married1 = get_user()
# print(name1, age1, married1)

# point = (10, 20)
# match point:
#     case (0, 0):
#         print("Точка находится в координатах 0:0")
#     case (x, 0):
#         print("Точка находится в координате", x, "по оси Х и в координате 0 по оси Y")
#     case (0, y):
#         print("!!!Точка находится в координате 0 по оси Х и в координате", y, "по оси Y")
#     case (x, y):
#         print("Точка находится в координате", x, "по оси Х и в координате", y, "по оси Y")
#     case _:
#         print("Это не координаты точки")

# t = [2, 3]
# print("t =", id(t))
# print(id(t[0]))
# t[0] = 5
# print(t)
# print(id(t[0]))
# print("t =", id(t))
# a = 5
# print(id(a))

# Распаковка кортежей#
#
# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t
# print(x, y, z)
# print(lst)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))))
# print(countries)
# print()
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6 ]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# a = 'Я обычная строка'
# b = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
#
#
# def to_set(par):
#     return set(par), len(set(par))
#
# print(to_set(a))
# print(to_set(b))


# s = {'banana', 'apple', 'orange'}
# print('apple' in s)
#
# for i in s:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# b = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# c = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
# print(b)
# print(c)
#
# # если не брать тернарное
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])

# s = {'banana', 'apple', 'orange'}
# s.add(4)
# s.remove(4)
# s.pop()
# print(s)
#
# a = {0,1,2,3}
# b = {4,3,2,1}
# c = a.union(b)
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1.union(s2, s3, s4, s5, s6, s7)
# c = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = 'Hello'
# s2 = 'How are you?'
# a = set(s1) & set(s2)
# for i in a
#     print(i, end = '')

# s1 = 'Python'
# s2 = 'Programming language'
# a = set(s1) - set(s2)
# print(a)


# drawing = {'Marina', 'Genya', 'Sveta'}
# music = {'Kostia', 'Genya', 'Ilya'}
# one_hobby = drawing ^ music
# both_hobby = drawing & music
# drawing = drawing - both_hobby
# print(one_hobby)
# print(both_hobby)
# print(drawing)

# s = frozenset([1,2,3,4,5])
# print(s)
#
# s1 = frozenset({'Hello', 'world'})
# print(s1)

# a = [1,2,3]
# d = {'one': 1, 'two': 2, 'three': 3}
# print(a[0])
# print(d['one'])

# a = [1,2,3]
# c = [1,2,3]
# b = dict(a)
# print(b)

# a = [
#     ['anna@mail.ru', 'Anna'],
#     ['ira@mail.ru', 'Ira'],
#     ['Igor@mail.ru', 'Igor'],
# ]
#
# b = dict(a)
# print(b)

# d = {i: i**2 for i in range(2,7)}
# print(d)

# d = {0: 'text', 'one': 45, (1,2.3): 'tuple', 42: [2,56,8], True: 1}
# print(d)
# # print(d[42][2])
#
# for key in d:
#     print(key, '-> ', d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# s = 1
# for i in d:
#     s *= d[i]
#
# print(s)

# d = dict()
# d[1] = input('->: ')
# d[2] = input('->: ')
# d[3] = input('->: ')
# d[4] = input('->: ')
# d = {i: input('-> ') for i in range(1,5)}
# print(d)
# dislike = int(input('Какой элемент исключить? '))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ',goods[i][1] ,'шт. по ',goods[i][2],'руб', sep='')
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input('Количество товара: '))
#         goods[n][1] = qty
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ',goods[i][1] ,'шт. по ',goods[i][2],'руб', sep='')

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# new_d = {'name': d.pop('name'), 'salary':d.pop('salary')}
#
#
# print(d)
# print(new_d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
#
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep='')

# sales = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4232, 'S': 6786, 'E': 4738, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3908, 'S': 3645, 'E': 8821, 'W': 2451},
# }
#
# print(sales)
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep='')
#
# person = input('Имя: ')
#
# region = input('Регион: ')
# print(sales[person][region])
# new_data = int(input('Новое значение: '))
# sales[person][region] = new_data
# print(sales[person])

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print({v : k for k, v in d.items()})
#
# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)

# one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}

# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '-> ', v1)
#     print(k2, '-> ', v2)

# pairs = [(1, 'a'), (2, 'b'),(3, 'c'), (4, 'd')]
# a,b = zip(*pairs)
# print(a)
# print(b)

# d = {'c': 3, 'a': 1, 'b': 2, 'd': 4}
# w = {k: v for k, v in d.items()}
# print(w)
# for i, j in d.items():
#     if len(d) <= 2:
#         print(i, ":", j)

# d = {'a': 1, 'b': 2, 'c': 3}
# count = 0
# for i in d:
#     print(i, ':', d[i])
#     count += 1
#     if count == 2:
#         break

# value = int(input("-> "))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# value = list(d.keys())
# print(value)
# value = list(d.values())
# print(value)
# value = list(d.items())
# print(value)


# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []  # d['two'] = []
#         s = i  # s = 'two'
#     else:
#         d[s].append(i)  # d['two'] = [10, 20]
#
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = dict(zip(b, a))
# print(d)


# b = [12, 1, 2]
# d = list(zip(b))
# print(d)


# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = [2.0, 4.6, 7.5]
#
# d = list(zip(a, b, c))
# print(d)


# one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# obj = {
#     'one': {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'},
#     'two': {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# }
# print(obj)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# one = {'apple': 0.4, 'orange': 0.35, 'pepper': 0.6}
# two = {'pepper': 0.8, 'onion': 0.55}
# print({**one, **two})


# {{'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55}}
# {'apple': 0.4, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}

# data = ['a', 'b', 'c', 'd']
#
# for i in data:
#     print(i, end=" ")
# print()
# for i in range(len(data)):
#     print(i, end=" ")
# print()
# #
# j = 1
#
# for i in data:
#     print(j, ":", i)
#     j += 1

# for j, i in enumerate(data, 100):
#     print(j, ":", i)

# n = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# for j, (i, v) in enumerate(n.items(), 100):
#     print(j, ":", i, "->", v)


# a = [1, 2, 3]
# b = [4, *a, 5, 6]
# print(b)


# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(3, 2))
# print(func(3, 4, 6, 9, 5))
# print(func())

# def to_dict(*lst):
#     return {i:i for i in lst}
#
#
# print(to_dict(1,2,3,4))
# print(to_dict('gray', (2,17), 3.11, -4))

# def to_ch(*arg):
#     return[i for i in arg if i < sum(arg)/ len(arg)]
#
#
# print(to_ch(1,2,3,4,5,6,7,8,9))
# print(to_ch(3,6,1,9,5))

# def func(a, *args):
#     return a, args
#
#
# print(func(5))

#
# def print_scores(student, *scores):
#     print('\nStudent Name: ', student, end=', scores: ')
#     a, b = None, ''
#     for score in scores:
#         a = str(score) + ', '
#         b += a
#     print(b[:-2])
#
#
# print_scores('Kate',100,95,88,92,99)
# print_scores('Rick',96,20,33,56)
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or (only_add and i % 2):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))

# def func(**date):
#     for key, value in date.items():
#         print(key, 'is', value)
#     print()
#
# func(name='Irina', surname='Sharma', age=22, phone=123456789)
# func(name='Igor', surname='Wood', email='igor@mail.ru', country='Russia',age=22, phone=9991258476)
# my_dict = {'one': 'first'}
#
#
# def db(**date):
#     # for key, value in date.items():
#     #     my_dict[key] = value
#     # return my_dict
#     my_dict.update(**date)
#
#
# print(db(k1=22, k2=31, k3=11, k4=91))
# print(db(name='Bob', age=31, weight=61, eyes_color='grey'))

# def func(*args, **data):
#     print(args[0], data)
#
# func(5,4,8,9,k1=22, k2=31, k3=11, k4=91)


# name = 'Tom'   #глобальная переменная
#
# def hi():
#     global name
#     name = 'Sam'  #локальные переменные
#     surname = 'John'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
# hi()
# bye()


# i = 5
#
# def func(arg=i):
#     print(arg)
#
# i = 6
# func()

# def add_two(a):
#     x = 2
#
#     def add_some():
#         return a + x
#
#     return add_some()
#
# print(add_two(3))

# def outer_func():
#     def inner_func():
#         print('Hello, world')
#
#     inner_func()
#
# outer_func()

# x = 25
#
# def fn():
#     global t
#     a = 30
#     t = a
#
#
# fn()
# z = x + t
# print(z)


# def func(city):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return wrap
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()

#
# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print('A = ', A(students))
# print('B = ', B(students))
# print('C = ', C(students))
# print('D = ', D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# obj1()


# Анонимные функции

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x**2+y**2)(2, 5))

# summ = lambda a, b, c=3: a + b + c
#
# print(summ(10, 20, 30))
# print(summ(10, 20))

# func = lambda *args:args
#
# print(func(1, 2, 3, 4, 5))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#      print(t('abc_'))


# def inc(n):
#     return lambda x: n + x
#
# f = inc(42)
# print(f(3))
#
# inc1 = (lambda n: lambda x: n + x)
#
# f3 = inc1(42)
# print(f3(3))
#
# def inc2(n):
#     def wrap(x):
#         return n + x
#
#     return wrap
#
# f1 = inc2(42)
# print(f1(3))

# print((lambda x: lambda y: lambda z: x + y + z)(2)(4)(6))

# players = [
#     {'name': 'Anton', 'last name': 'Birukov', 'raiting': 9},
#     {'name': 'Alex', 'last name': 'Bodnya', 'raiting': 10},
#     {'name': 'Fedor', 'last name': 'Sidorov', 'raiting': 4},
#     {'name': 'Mihail', 'last name': 'Semenov', 'raiting': 6}
# ]
#
# res = sorted(players, key = lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key = lambda item: item['raiting'])
# print(res)
#
# res = sorted(players, key = lambda item: item['raiting'], reverse = True)
# print(res)
#
# d = {'b': 15, 'a': 3, 'c': 7}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(a[0](12, 3))

# a = {'one': lambda x: x - 1, 'two': lambda x: x - 3, 'three': lambda x: x}
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda : print('Понедельник'),
#     2: lambda : print('Вторник'),
#     3: lambda : print('Среда'),
#     4: lambda : print('Четверг'),
#     5: lambda : print('Пятница'),
#     6: lambda : print('Суббота'),
#     7: lambda : print('Воскресенье')
# }
#
# d[3]()

# m = lambda a, b: a if a > b else b
# print(m(2, 5))

# m = lambda a,b,c: a if a < b and a < c else b if b < c and b < a else c
# print(m(19,18,15))

# map()

# def mul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lst2 = set(map(mul, lst))
# print(lst2)

# t = (2.88, -1.75, 100.03)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)


# filter(func,iterable)

# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66,90,68,59,76,50,88,74,81,65]
# res = list(filter(lambda s: s>75, b))
# print(res)

# from random import randrange

# lst = [randint(1,40)for i in range(10)]
# print(lst)
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst2)

# nums = [45,55,60,37,100,105,220]
# res = list(filter(lambda x: x%15 == 0, nums))
# print(res)

# m = list(map(lambda x: x**2, filter(lambda x: x%2, range(10))))
# print(m)

# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am super')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# @my_decorator
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# func_test()
# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# @bold
# def hello():
#     return 'text'
#
# print(hello())

# def cnt(fn):
#     count = 0
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции: ', count)
#     return wrap
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('Hi', arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first,second, last):
#     print('Меня зовут', first,second, last)
#
#
# print_full_name('Ирина',"Назарова")
# print_full_name("Виктор", "Федерович", "Назаров")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print(a + b)

#
# @decor("Разность:", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#
#         return wrap
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     return 'Некорректный тип данных'
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 'Doge'))

# def multiplay(args1):
#     def wrapper(return_num):
#         def wrap(num):
#             return args1*num
#         return wrap
#     return wrapper
#
#
# @multiplay(3)
# def return_num(num):
#     return num
# print(return_num(5))

# s = 5
# print(s)

# a = 5
# print('Hello')
# print(a)

#
# print((int('18')))
#
# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(18))

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print('q' in e)
#
# print(e[0])

# s = 'Python'
# s = s[:3] + 't' + s[4:]
# print(s)


# def change_char_to_str(s, c_old, c_new):
#     s2 = ''
#     for i in range(len(s)):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#     return s2
#
#
# str1 = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = change_char_to_str(str1, 'N', 'P')
# print(str1)
# print(str2)

# print('C:\\folder\\file.txt')

# name = 'Дмитрий'
# age = 25
# print(f'Меня зовут {name}, мне {age} лет')

# s = '''<div>
#     <p> Text </p>
# </div>
# '''
# print(s)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n**2
#
# print(square(5))
#
# print(square.__doc__)

# import math
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
# print(cylinder(2,4))
# print(cylinder.__doc__)

# print(ord('a'))

# while True:
#     n = input('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# my_str = 'Test string for me'
# arr = [ord(x) for x in my_str]
# print('ASCII code: ', arr)
# arr = [sum(arr) // len(arr)] + arr
# print('Среднее арифметическое: ', arr)
# arr += [ord(x) for x in input('-> ')[:3] if ord(x) not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) -1)

# print(chr(33))
# print(chr(8364))


# a = 122
# b = 97
# if a > b:
#     a, b == b, a
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# print('apple' == 'Apple')
# print('apple' > 'Apple')

# s = 'hello, WORLD! I am learning Python'
# print(s.capitalize())
# print(s.lower())


# str = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения'
# a = str[:str.find('о') + 1]
# b = str[str.find('о') + 1:str.rfind('о')]
# c = str[str.rfind('о'):]
# print(a + b.replace('о', 'О') + c)

# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print('..'.join(['1', '99']))

# a = input("-> ").split()
# print(a)

# a = input('Введите ФИО: ').split()
# print(f'{a[0]} {a[1][0]}. {a[2][0]}.')

import re

#
# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = '2023'
# # print(re.findall(reg, s))
# # print(re.search(reg, s))
#
# print(re.findall(reg, s))

# __________________________Flag________________________________________

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = 'hello world'
# print(re.findall(r'\w+', text, re.DEBUG))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 200000 - счёта.'
# reg = 'я'
# print(re.findall(reg,s, re.IGNORECASE))

# text = """
# one
# two
# """

# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall(r'one$', text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+
# @
# [a-z.-]+
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON
# """
# reg = '(?mi)^python'
# print(re.findall(reg, text))

# def valid_name(name):
#     return re.findall('^[a-z0-9_-]{3,16}$', name, re.I)
#
# print(valid_name('Python_master'))
# print(valid_name('Pyt'))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# # reg = '<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# s = 'Петр, Ольга и Виталий'
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = 'int = 4, float = 4.0, double = 8.0f'
# reg = r'(?:int|double)\s*=\s*\d+[.\w]*'
# print(re.findall(reg, s))

# # s = '127.0.0.1'
# s = '192.168.255.255'
# # reg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# reg = r'(?:\d{1,3}\.){3}\d{1,3}'
# print(re.findall(reg, s)[0])
#
# s = "World2016, PS6, AI5"
# reg = r'[a-z]+\d*'
# print(re.findall(reg, s, re.I))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# s = input('Введите текущую дату по шаблону "22-08-2021": ')
# reg = r'(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19\d\d|20\d\d)'
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
#
#
# count = 0
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
# print(re.sub(r"\s*(\w*)\s*", repl_find, text))

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     # print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):  # 15
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # convert[15] = 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] = 'E'
#
#
# print(to_str(254, 16))

# print(names[0])
# print(isinstance(names[0], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# print(names)


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))
#
# names = ["Adam", ["Bob", ["Chet", "Cat", "aaa"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# count = 0
# for i in names:
#     if isinstance(i, list):
#         for j in i:
#             if isinstance(j, list):
#                 # for k in j:
#                 #     count += 1
#                 count += len(j)
#             else:
#                 count += 1
#     else:
#         count += 1
# print(count)

# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0] + union(s[1:]))  # 'Bob' + Chet'
#     return s[:1] + union(s[1:])  # ['Adam']
#
#
# print(union(names))


# def remove(text):  #
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])  # HelloWorld! + ""
#
#
# print(remove(" Hello\tWorld! "))


# Линейный (последовательный) поиск

# def seq_search(s, item):
#     found = False  # True
#     pos = 0  # 2
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found


# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(lst)
# print(seq_search(lst, 32))
# print(seq_search(lst, 3))

# def seq_search(s, item):
#     found = False  #
#     pos = 0  # 3
#     stop = False  # True
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:  # 8 > 3
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# lst.sort()
# print(lst)
# print(seq_search(lst, 32))
# print(seq_search(lst, 3))

from random import randint
import time

#
# def seq_search(s, item):
#     found = False  #
#     pos = 0  # 3
#     stop = False  # True
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:  # 8 > 3
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
# # lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# lst = [randint(1,99) for i in range(100000)]
# start = time.monotonic()
# print(seq_search(lst, 0))
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# -------бинарный поиск--------


# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
#
# print(binary_search(lst, 1))
# print(binary_search(lst, 3))


# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
#
# lst = [randint(1,99) for i in range(10000)]
# start = time.monotonic()
# # print(lst)
# bubble(lst)
# # print(lst)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     left = merge_sort(a[:n//2] )
#     right = merge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#
#     return res
#
# # array = [8, 2, 6, 4, 5]
# # print(array)
# array = [randint(1,99) for i in range(10000)]
# start = time.monotonic()
# array = merge_sort(array)
# print(array)
#
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# ______сортировка шелла_________
# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#     return s
#
#
#
#
# a = [10, 21,9,14,67,44,26,87]
# print(a)
# shell_sort(a)
# print(a)

# ___________Быстрая сортировка______________

# def quick_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1) // 2]
#
#         low = [i for i in a if i < x]
#         eq = [i for i in a if i == x]
#         hi = [i for i in a if i > x]
#         a = quick_sort(low) + eq + quick_sort(hi)
#
#     return a
#
#
# lst = [9, 5, -3, 4, 7, 8, -8]
# print(lst)
# lst = quick_sort(lst)
# print(lst)

# Файлы

# f = open('text.txt', 'r')
# print(f)
# print(*f)
# f.close()

# f = open('text.txt', 'a +')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.77]
#
# with open(file_name, 'w+') as my_file:
#     my_file.write('\t'.join(map(str, lst)))
#
# with open(file_name, 'r+') as my_file:
#     new_lst = my_file.read().split('\t')
#
# print(len(new_lst))
# print(f'Sum = {sum(map(float, new_lst))}')
#
# with open('text.txt', 'w+') as file:
#     file.write('После врача на плановом осмотре, мужчина понимает')
#
# def longest_world(file):
#     with open(file, 'r') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         print(w)
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
# print(longest_world('text.txt'))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write (text)
#
# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия - ')
#         fw.write(line)

# ================Модуль ОС или Os.Path========================

# import os


# print(os.getcwd())
#
# print(os.listdir())
# print(os.listdir('..'))
#
# os.mkdir('folder')

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         print(file_path)
#         open(file_path, 'w').close()
#
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')

# def print_tree(root, topdown):
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх"}')
#     for root, dirs, fl in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)(
#         print(fl)
#     print('-' * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)
# import time
# file_path = r'Work\F2\F21\f212.txt'
# if os.path.exists(file_path):
#     print(os.path.basename(file_path), end = ' ')
#     print('(' + os.path.dirname(file_path) + ')')
#     print('Время последнего доступа к файлу:', time.strftime('%d.%m.%Y, %H:%M:%S',time.localtime(os.path.getatime(file_path))))
# else:
#     print(f'Файл {file_path} не существует!')

# print(os.path.isfile(r'D:\pythonProject\Work\F2\F21\f211.txt'))
# print(os.path.isdir(r'D:\pythonProject\Work\F2\F21'))

# dir_name = 'Work'
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f'{obj} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{obj} - dir')

# ______________ООП________________

# class Point:
#     x = 1
#     y = 1
#
# p1 = Point()
# Point.x = 100
# p1.x = 20
# print(p1.x, p1.y)
#
# p2 = Point()
# print(p2.x, p2.y)
#
# print(p1.__dict__)
# print(p2.__dict__)
# print(Point.__dict__)

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(selfself):
#         print('Hello')
#
# p1 = Point()
# p1.set_coord()

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print('Персональные данные '.center(40, '*'))
#         print(
#             f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\n'
#             f'Город: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first, birthday, phone, country, city, address):
#         self.name = first
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_birthday(self, val):
#         self.birthday = val
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_name('Маргарита')
# print(h1.get_name())
#
# h1.set_birthday('25.03.2000')
# print(h1.get_birthday())
#
# h1.set_phone('55-17-26')
# print(h1.get_phone())
#
# h1.set_country('Сербия')
# print(h1.get_country())
#
# h1.set_city('Краснодар')
# print(h1.get_city())
#
# h1.set_address('Проспект Героев, 18')
# print(h1.get_address())

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         print('Инициализатор')
#         self.name = name
#         self.surname = surname
#     def print_info(self):
#         print('Данные сотрудника: ', self.name, self. surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника: ', self.skill, '\n')
#
#
# p1 = Person('Виктор', 'Резник')
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person('Анна', 'Долгих')
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     def __init__(self, x,y):
#         self.x = x
#         self.y = y
#         print('Экземпляр класса создан!')
#
#     def __del__(self):
#         print('Экземпляо класса удален!')
#
#
# p1 = Point(5, 10)
# print(p1.x, p1.y)
# # del p1
# p1 = 5
# print(p1.__dict__)

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(15, 20)
# p3 = Point(20, 40)
# print(Point.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Инициализация робота: {self.name}')
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'выключается!')
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#         else:
#             print(f'Работающих роботов осталось {Robot.k}')
#     def say_hi(self):
#         print(f'Приветствую!Меня зовут: {self.name}')
#
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print(f'Численность роботов: {Robot.k}')
#
# droid2 = Robot('C-3PO')
# droid1.say_hi()
# print(f'Численность роботов: {Robot.k}')
#
# droid3 = Robot('TP-4PO')
# droid1.say_hi()
# print(f'Численность роботов: {Robot.k}')
#
# print('\nЗдесь роботы могут проделать какую-то работу.\n\n'
#       'Роботы закончили свою работу. Давайте их выключим.')
#
# del droid1
# del droid2
# del droid3
# print(f'Численность роботов: {Robot.k}')

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_coord(self):
#         return self.__x, self.__y
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_coord(12,8.3)
# print(p1.get_coord)
# p1.x = 100
# p1.y = 'abc'
# print(p1.x, p1.y)
# import math
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = self.__width = 0
#         if Rectangle.__check_value(length) and Rectangle.__check_value(width):
#             self.__length = length
#             self.__width = width
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__width * self.__length
#
#     def get_perimetr(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#     def get_draw(self):
#         print(('*' * self.__width + '\n') * self.__length)
#
#
# a = Rectangle(4, 12)
# a.set_width(9)
# a.set_length(3)
# print('Длина прямоугольника: ', a.get_length())
# print('Ширина прямоугольника: ', a.get_width())
# print('Площадь прямоугольника: ', a.get_area())
# print('Периметр прямоугольника: ', a.get_perimetr())
# print('Гипотенуза прямоугольника: ', a.get_hypotenuse())
# a.get_draw()

# class Point:
#     __slots__ = ["__x", "__y", "z"]
#     count = 0
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(Point.count)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __get_x(self):
#         return self.__x
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.x = 25
# print(p1.x)
# # p1.__set_x(15)
# # print(p1.__get_x())
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 25
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# p1.old = 31
# print(p1.old)
# del p1.old
# print(p1.__dict__)

# class Point:
#     __count = 0
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#     @staticmethod
#     def get_count():
#         return Point.__count
#
# #    get_count = staticmethod(get_count())
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
# print(Change.inc(10))
# print(Change.dec(10))

# class Counter:
#     @staticmethod
#     def max_counter(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def min_counter(a, b, c, d):
#         return min(a, b, c, d)
#     @staticmethod
#     def sr_counter(a, b, c, d):
#         return (a+b+c+d) / 4
#     @staticmethod
#     def f_counter(x):
#         count = 1
#         for i in range(1,x + 1):
#             count *= i
#         return count
#
#
#
# print(Counter.max_counter(3, 5, 7, 9))
# print(Counter.min_counter(3, 5, 7, 9))
# print(Counter.sr_counter(3, 5, 7, 9))
# print(Counter.f_counter(5))
# import math
#
#
# class Area:
#     count = 0
#     @staticmethod
#     def triangle_area(a, b, c):
#         Area.count += 1
#         p = (a + b + c) / 2
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#
#
# print('Площадь треугольника по формуле Герона: ', Area.triangle_area(3, 4, 5))
# print('Площадь треугольника через основание и высоту: ', Area.triangle_area2(6, 7))
# print('Площадь квадрата: ', Area.square_area(7))
# print('Площадь прямоугольника: ', Area.rect_area(2,6))
# print('Вызов площади: ', Area.get_count())


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <=12 and year <=3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '40.01.2021',
#     '12.31.2022'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print(f'Неправильная дата или формат строки с датой')

# date = Date.from_string('23.10.2022')
# print(date.string_to_db())
# ----------------------------------------------
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счёт #{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print('Проценты начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно сняты!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def print_info(self):
#         print('Информация о счёте')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.set_usd_rate(2)
# acc.convert_to_usd()
# acc.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(5000)
# print()
# acc.add_money(5000)

# ----------------------------------------------
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall("[А-яё-]", fio))  # ВолковИгорьНиколаевич
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def info(self):
#         return self.__fio, self.__old, self.__password, self.__weight
#
#     @info.setter
#     def info(self, *args):
#         # print(args[0][0])
#         self.verify_fio(args[0][0])
#         self.verify_old(args[0][1])
#         self.verify_weight(args[0][3])
#         self.verify_ps(args[0][2])
#
#         self.__fio = args[0][0]
#         self.__old = args[0][1]
#         self.__password = args[0][2]
#         self.__weight = args[0][3]
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData("Волков Игорь Николаевич", 21, "1234 567890", 80.8)
# # p1.fio = "Соболев Игорь Николаевич"
# p1.old = 26
# p1.password = "9876 543210"
# p1.weight = 90.4
# p1.info = "Соболев Игорь Николаевич", 35, "7834 567890", 98.8
# print(*p1.info)
# print(p1.__dict__)


# Наследование

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Инициализатор класса Prop")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         print("Переопределенный инициализатор Line")
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")


# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()

# print(line._width)
# print(line.__dict__)
# rect = Rect(Point(30, 40), Point(70, 90))
# rect.draw_rect()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.area())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(3, 40), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(1, 2), Point(10, 20))
# rect.set_coord(Point(30.8, 40), Point(100.8, 200))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольника:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.border = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return ' '.join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))
# Перегрузка методов
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print('Координата должна быть целым числом')
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целыми числами")
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(3, 40), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10,20))
# line.draw_line()
#

# Абстрактные методы
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод draw()')
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     # def draw(self):
#     #     print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10,10), Point(20,10)))
# figs.append(Rect(Point(50,50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()
#
# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print('Нарисовать щахматную фигуру')
#
#     @abstractmethod
#     def move(self):
#         pass
#
# class Queen(Chess):
#     def move(self):
#         print('Ферзь перемещен на у2е3')
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()
# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())
# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#
# print('*'*50)
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')

# Интерфейсы

# from abc import ABC, abstractmethod
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child')
#
# class GrandChild(Child):
#     def display2(self):
#         print('GrandChild')
#
# # gc = Child()
# gc = GrandChild()

# Вложенные классы
#
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print('Я метод внешнего класса')
#
#     class MyInner:
#         def __init__(self, inner_name):
#             self.inner_name = inner_name
#
# out = MyOuter('Внешний')
# inner = out.MyInner('внутренний')
# print(out.name)
# print(inner.inner_name)
#
# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Lightgreen'
#             self.code = '024avc'
#
#         def display(self):
#             print('Name', self.name)
#             print('Code', self.code)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core i7'
#
#
# comp = Computer()
# print(comp.name)
# my_os = comp.os
# my_cpu = comp.cpu


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('In Base Class')
#
#     class Inner:
#         def display1(self):
#             print('Inner of Base Class')
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of SubClass')
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.sleep()
# beast.play()

# outer = Out()
# outer.show()
# class AA:
#     def __init__(self):
#         print("Инициализатор АA")
#
#
# class A:
#     def __init__(self):
#         print("Инициализатор А")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор C")
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициализатор D")
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)

# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Style:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Style")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color, width):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         # Style.__init__(self, color, width)
#         super().__init__(color, width)
#
#
# class Line(Pos, Style):
#     # def __init__(self, sp: Point, ep: Point, color, width):
#     #     Style.__init__(self, color, width)
#     #     Pos.__init__(self, sp, ep)
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
# print(Line.mro())


# Миксины (примеси)

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="log.txt")
#
#
# sub = MySubClass()
# sub.display("Эта строка будет напечатана и сохранена в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_log()
#
# n1 = NoteBook("HP", 1.5, 35000)
# n1.save_log()


# Перегрузка операторов

# Число секунд в одном дне: 24 * 60 * 60 = 86400

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c4 = Clock(300)
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")

# c3 = c1 + c2 + c4  # c3 = Clock(100 + 200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c4.get_format_time())
# print(c3.get_format_time())
# c2 += c1
# print(c2.get_format_time())

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#             # return "Неверный индекс"
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[9])
# print(s1.marks[2])

# ........................................................
# __slots__

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__z')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.z = math.sqrt(x * x + y * y)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         self.__z = value
#
#
# p1 = Point(5, 8)
# print(p1.z)
# p1.z = 10
# print(p1.__dict__)

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 8)
# p2 = Point2D(5, 8)
# print('p1 = ', p1.__sizeof__())
# print('p2 = ', p2.__sizeof__())

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     pass
#
#
# p3 = Point3D(10, 20)
# p3.z = 30
# print(p3.z)


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a,b):
#         return self.func(a,b)**2
#
# @Power
# def func(a,b):
#     return a*b
#
# print(func(2,3))
#
# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self,func):
#         def wrap(a,b):
#             return func(a,b)**self.arg
#         return wrap
#
# @Power(3)
# def func1(a,b):
#     return a*b
#
# print(func1(2,2))
#
#
# import requests
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(response)
#

# import csv

# csv.DictReader() - считывает данные как словарь

# with open('data.csv') as f:
#     fn = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=';', fieldnames=fn)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {" ,".join(row)}')
#         print(f'\t{row["Имя"]} - {row["Профессия"]}. Родился в {"Год рождения"} году')
#         count += 1
#     print(f'Всего в файле {count} строки')

# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя', '9', '15'])
#     writer.writerow(['Саша', '5', '12'])
#     writer.writerow(['Маша', '11', '18'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

# with open('sw_data1.csv', 'w') as f:
#     names = ['Имя', 'Возраст']
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     writer.writeheader()
#     writer.writerow({'Имя': 'Саша', 'Возраст':6})
#     writer.writerow({'Имя': 'Маша', 'Возраст':15})
#     writer.writerow({'Имя': 'Вова', 'Возраст':14})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_data.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# ----------------парсинг---------------

# pip install beautifulsoup4

from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find('div', string='Alena').find_parent(class_='row')
# row = soup.find('div', id='whois3').find_next_sibling()
# print(row)

# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois')
#     if 'Copywriter' in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(row)

# def get_salary(s):
#     pattern = r'\d+'
#     res = re.findall(pattern, s)[0]
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all('div', {'data-set': 'salary'})
# for i in row:
#     get_salary(i.text)

# import requests


# res = requests.get('https://ru.wordpress.org/')
# print(res.status_code)
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title').text
#     print(p1)
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         write = csv.writer(f, delimiter=';', lineterminator='\r')
#         write.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("article")
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a").get("href")
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find('span', class_="rating-count").find("a").text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# import requests
# from bs4 import BeautifulSoup
#
# res = requests.get('https://ru.wordpress.org/')
# print(res.status_code)
import requests
from bs4 import BeautifulSoup
import csv

#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
# def write_csv(data):
#     with open('plugins1.csv', 'a', encoding='utf-8') as f:
#         write = csv.writer(f, delimiter=';', lineterminator='\r')
#         write.writerow((data['name'], data['url'], data['snippet'],data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all('article', class_='plugin-card')
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find('h3').find('a').get('href')
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_='entry-excerpt').text.strip()
#         except ValueError:
#             snippet = ''
#
#         try:
#             active = el.find('span', class_='active-installs').text.strip()
#         except ValueError:
#             active = ''
#
#         try:
#             c = el.find('span', class_='tested-with').text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             c = ''
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(5,26):
#         url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# from parse import Parser
#
#
# def main():
#     pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
#     pars.run()
#     pars.save()
#
#
# if __name__ == '__main__':
#     main()

import socket


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen()

    while True:
        client_socket, abbr = server_socket.accept()
        request = client_socket.recv(1024)

        print(f'Клиент: {abbr} => \n{request}\n')


if __name__ == '__main__':
    run()
