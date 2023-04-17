from homework import Parser


def main():
    for i in range(3,10):
        pars = Parser('https://elementy.ru/nauchno-populyarnaya_biblioteka/t/21093/Fizika', 'HW.csv')
        pars.run()

#  Для текстового файла
# def main():
#     for i in range(3,10):
#         pars = Parser('https://elementy.ru/nauchno-populyarnaya_biblioteka/t/21093/Fizika', 'HW.txt')
#         pars.run()


if __name__ == '__main__':
    main()
