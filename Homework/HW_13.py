def decor(fn):
    def wrap(*args):
        count = 0
        for i in args:
            count += 1
        print('Среднее арифметическое чисел: ', fn(*args) / count)

    return wrap


@decor
def summa(*arg):
    j = 0
    for i in arg:
        j += i
    print('Сумма чисел: ', j)
    return j

summa(2,4,7,9)
summa(5,6,9,10,12)
summa(2,65,89,4,1,9)