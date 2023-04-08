from math import sqrt


class Pair:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def change1(self):
        return self._a

    @change1.setter
    def change1(self, new_a):
        if isinstance(new_a, (int, float)):
            self._a = new_a

    @property
    def change2(self):
        return self._b

    @change2.setter
    def change2(self, new_b):
        if isinstance(new_b, (int, float)):
            self._b = new_b

    def get_summ(self):
        return self._a + self._b

    def get_product(self):
        return self._a * self._b

    def pair_info(self):
        print(f'Сумма чисел a и b: {self.get_summ()}')
        print(f'Произведение чисел a и b: {self.get_product()}')


class Right_Triangle(Pair):
    def get_hypotenuse(self):
        return round(sqrt(self._a ** 2 + self._b ** 2), 2)

    def get_area(self):
        return self.get_product() / 2

    def get_info(self):
        print(f'Гипотенуза треугольника ABC: {self.get_hypotenuse()}')
        print(f'Площадь треугольника ABC: {self.get_area()}')


p1 = Pair(5, 8)
p1.pair_info()
p1.change1 = 9
p1.pair_info()
p1.change2 = 10.5
p1.pair_info()

tr = Right_Triangle(5, 8)
tr.get_info()
