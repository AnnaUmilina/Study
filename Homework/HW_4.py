# 1 задание
num = 64
n = 0
for i in range(1,101):
    a = int(input('Введите число от 1 до 100: '))
    if a == num:
        print('Вы угадали загаданное число с ',n + 1 , 'раза')
        break
    elif 101 > a > num:
        print('Загаданное число меньше')
    elif 0 < a < num:
        print('Загаданное число больше')
    elif a == 0:
        print('Жаль, что Вам надоело. Игра окончена!')
        break
    else:
        print('Введите число строго от 1 до 100!')
    n += 1

# 2 задание

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов списка: \nn= ')))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=' ')


# 3 задание

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# for i in a:
#     q = 0
#     for j in a:
#         if j == i:
#             q += 1
#     if q == 1:
#         print(i, end = ' ')
#         q = 0

# 4 задание
# a = int(input('Введите высоту: '))
# for i in range(a):
#       q = a - i
#       print('*' * q)

