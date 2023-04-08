# 1 task
#
# a = ['red', 'green', 'blue']
# b = ['#FF0000', '#008000', '#0000FF']
# x = dict(zip(a,b))
# print(x)

# 2 task

# d = {i: i**3 for i in range(1, 11)}
# print(d)

# 3 task

# a = ['color', 'fruit', 'pet']
# b = ['blue', 'apple', 'dog']
# #1 var
# s = {a: b for a,b in zip(a,b)}
# print(s)
#
# #2 var
# d = dict(zip(a,b))
# print(d)

# 4 task

# def minimal(*arg):
#     return min(arg)
#
#
# print(minimal(21,3))
# print(minimal(2,36,7,74))
# print(minimal(214,74,8,5))
# print(minimal(-14,34,-8,3))

# 5 task

# def summa(*arg):
#     s = [i for i in arg]
#     count = 0
#     for i in s:
#         count += i
#         print(count, end=' ')
#     print()
#
#
# summa(3, 9, 1)
# summa(2, 5, 4, 2)
# summa(3, 5, 10, 6, 3)
