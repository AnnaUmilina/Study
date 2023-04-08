lst1 = [5, 9, 6, 7]
lst2 = [3, 11, 8]
lst3 = [2, 4]
lst4 = [10, 1, 12]
sort = int(input('1 - сортировка по убыванию\n2 - сортировка по возрастанию\n-> '))


def des(a, q):     #возвращает отсортированный список
    if len(a) > 1:
        x = a[(len(a) - 1) // 2]  # x-основное значение в середине списка

        low = [i for i in a if i < x]  # всё, что меньше осн знач
        eq = [i for i in a if i == x]  # само осн знач остается в центре списка
        hi = [i for i in a if i > x]  # все, что больше
        if q == 1:  # по убыванию
            a = des(hi, 1) + eq + des(low, 1)
        elif q == 2:  # по возрастанию
            a = des(low, 2) + eq + des(hi, 2)
    return a


def home_sort(a, b, c, d, s):   #соединяет в общий список и передает в др функцию на сортировку
    lst = a + b + c + d
    if s == 1:
        print(des(lst, 1))
        return des(lst, 1)  # вызов функции по убыванию
    elif s == 2:
        print(des(lst, 2))
        return des(lst, 2)  # вызов функции по возрастанию
    else:
        print('Ошибка, метод сортировки можно выбрать только "1" или "2"')
        return s


def search_item(lst, item):   #поиск значения в отсортированном списке
    found = False
    pos = 0
    while pos < len(lst) and not found:
        if lst[pos] == item:   # в pos попадают последовательные элементы по индексам из списка
            found = True     # если элемент по индексу пос равен самому элементу
        else:
            pos += 1   # последовательное увеличение индекса в списке на 1
    if found == True:
        return f'Значение {item} найдено'
    else:
        return f'Значение {item} не найдено'
item1 = int(input('Введите значение для поиска: '))
print((search_item((home_sort(lst1, lst2, lst3, lst4, sort)), item1)))
