lst = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
a = []  # prime number
b = []
c = []  # 0 and 1


def maximum():
    for i in lst:
        if i % 2 == 0 or i % 3 == 0 and i != 2 and i != 3:
            a.append(i)
        elif i == 0 or i == 1:
            c.append(i)
        else:
            b.append(i)
    print('Min: ', min(b))
    print('Max: ', max(a))


maximum()


# Сначала сделала вот так, работает, но без функций
# lst = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
# a = []  # prime number
# b = []
#
# for i in lst:
#     if i % 2 == 0 or i % 3 == 0 and i != 2 and i != 3:
#         a.append(i)
#     elif i == 1 or i == 0:
#         print()
#     else:
#         b.append(i)
# print('Min: ', min(b))
# print('Max: ', max(a))


