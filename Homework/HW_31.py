import csv

with open('data2.csv') as f:
    file_reader = csv.reader(f, delimiter=';')
    count = 0
    for row in file_reader:
        if count == 0:
            print(f'Файл содержит столбцы: {" ,".join(row)}')
            count += 1
        else:
            print(f'\t{row[0]} - производитель: {row[1]} - модель: {row[2]} - местоположение: {row[3]}')
