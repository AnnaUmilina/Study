money = int(input('Введите количество копеек от 1 до 99: '))
if 1 <= money <= 99:
    print('У вас', money, end='')
    if money % 10 == 1 and money !=11:
        print(' копейка')
    elif 2 <= money <= 4 or 22 <= money <= 94:
        if money % 10 == 2 or money % 10 == 3 or money % 10 == 4:
            print(' копейки')
        else:
            print(' копеек')
    else:
        print(' копеек')
else:
    print('Некорректные данные')
