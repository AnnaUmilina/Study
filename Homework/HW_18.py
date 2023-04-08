# lst = [-2, 3, 8, -11, -4, 6]
#
# def negative_number(num):
#     if not num:
#         return 0                           # возвращается на проверку условия num[0] < 0
#     else:
#         count = negative_number(num[1:])   # в стек сохраняются числа из списка(все)  #-2 3 8 -11 -4 6
#         if num[0] < 0:                     # проверка 0(из return), 6, -4 (добавляет в count) и т.д.
#             count += 1
#         return count                       # этот return возвращает значение в вызоы функции [1:], т.е. в count = negative...
#
#
# print(negative_number(lst))

sum = 'hello my dear husband'


def remove_char(s):
    return s.split()[1:-2]


print(remove(sum))
