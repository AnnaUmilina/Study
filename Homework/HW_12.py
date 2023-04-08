# # 1 task
# from math import pi
#
# print((lambda r: pi * r ** 2)(2))
# print((lambda a, b: a * b)(10, 13))
# print((lambda a, b, h: (a + b) / 2 * h)(5, 7, 3))

# # 2 task
# print((lambda a, b, c: a * b * c)(2, 5, 5))
# # или
# print((lambda a: lambda b: lambda c: a*b*c)(2)(5)(5))

# # 3 task
# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nicolas', 'final': 98}]
#
# res = sorted(students, key=lambda item: item['final'])  #  в порядке возрастания
# print(res)
# res = sorted(students, key=lambda item: item['final'], reverse = True) # в порядке убывания
# print(res)

# # 4 task
# students = [{'name': 'Jennifer', 'final': 95},
#             {'name': 'David', 'final': 92},
#             {'name': 'Nicolas', 'final': 98}]
#
# res = sorted(students, key=lambda item: item['final'])  #  в порядке возрастания
# print('Минимальный балл у ', res[0]['name'], ' = ', res[0]['final'])
# res = sorted(students, key=lambda item: item['final'], reverse = True) # в порядке убывания
# print('Максимальный балл у ', res[0]['name'], ' = ', res[0]['final'])

# # 5 task
# test = [3, 6, 8, 9, 1, 2]
# lst = []
# for i in range(len(test)):
#     x = test[i]
#     lst.append((lambda a, b: b * a ** 3)(i, x))
# print(lst)

# # 6 task
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
#
# print(list(map(lambda a: a ** 2, nums)))
# print(list(map(lambda a: a ** 3, nums)))
