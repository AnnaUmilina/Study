class Car:
    print(' Данные автомобиля '.center(40, '*'))

    def __init__(self, model, year, manufacturer, power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price
    def get_car(self):
        print(f'Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\n'
              f'Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}')
        print('=' * 40)


c = Car('X7 M50i', '2021', 'BMW', '530 л.с.', 'white', '10790000')
c.get_car()
