# 1 вариант, глобальная
# s = 0
#
#
# def area_parallelepiped(a,b,c):
#     global s
#     s = 2 * (a * b + a * c + b * c)
#
#     def area_rectangle():    # функция не используется
#         s1 = a * b
#         s2 = a * c
#         s3 = b * c
#     area_rectangle()
#     return s
#
#
# print(area_parallelepiped(2, 4, 6))
# print(area_parallelepiped(5, 8, 2))
# print(area_parallelepiped(1, 6, 8))

# 2 вариант, локальная

# def area_parallelepiped(a, b, c):
#     def area_rectangle():
#         s1 = a * b
#         s2 = a * c
#         s3 = b * c
#         s = 2 * (s1 + s2 + s3)
#         return s
#
#     print(area_rectangle())
#
#
# area_parallelepiped(2, 4, 6)
# area_parallelepiped(5, 8, 2)
# area_parallelepiped(1, 6, 8)

# 3 вариант, нелокальная
#
# def area_parallelepiped(a, b, c):
#     s = 2 * (a * b + a * c + c * b)
#
#     def area_rectangle():
#         nonlocal s
#         s1 = a * b
#         s2 = a * c
#         s3 = c * b
#         s = 2 * (s1 + s2 + s3)
#
#     area_rectangle()
#     return s
#
#
# print(area_parallelepiped(2, 4, 6))
# print(area_parallelepiped(5, 8, 2))
# print(area_parallelepiped(1, 6, 8))
