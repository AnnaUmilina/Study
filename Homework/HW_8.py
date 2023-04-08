# 1 task
#
# s = tuple(int(input('->:  ')) for _ in range(int(input('Введите количество значений для сравнения: '))))
# def maximum():
#     a = []
#     print('Тестовые значения:', s)
#     for i in s:
#         if i % 13 == 0 and i > 0:
#             a.append(i)
#     if not a:
#         print('Нет чисел кратные 13')
#     else:
#         print(max(a))
#
#
# maximum()

# 2 task
#
# def search():
#     source_tuple = ('ab', 'abcd', 'cde', 'abc', 'def')
#     print('Исходный кортеж: ', source_tuple)
#     s = input('Введите элемент, который нужно найти: ')
#     source_tuple.count(s)
#     if source_tuple.count(s) > 0:
#         print('Элемент', s, ' найден')
#     else:
#         print('Элемент', s, ' не найден')
#
#
# search()


#3 task
#Никак не смогла получить без повторения элементов

# elements = tuple(input('Введите по порядку, без пробелов элементы кортежа: '),)
# print(elements)
#
# def count_elements():
#     for i in elements:
#         print('Количество ',i,' = ', elements.count(i))
#
#
# count_elements()