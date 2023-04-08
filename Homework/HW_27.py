class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __add__(self, other):
        return f'({self.x + other.x}, {self.y + other.y}, {self.z + other.z})'

    def __sub__(self, other):
        return f'({self.x - other.x}, {self.y - other.y}, {self.z - other.z})'

    def __mul__(self, other):
        return f'({self.x * other.x}, {self.y * other.y}, {self.z * other.z})'

    def __truediv__(self, other):
        return f'({self.x / other.x}, {self.y / other.y}, {self.z / other.z})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise ValueError('Ключ-строковое значение!')
        if key == 'x':
            return self.x
        elif key == 'y':
            return self.y
        elif key == 'z':
            return self.z
        else:
            print('Error')

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError('Ключ-строковое значение!')
        if not isinstance(value, int):
            raise ValueError('Координата должна быть числом!')
        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        elif key == 'z':
            self.z = value
        else:
            print('Error')


p1 = Point(12, 15, 18)
p2 = Point(6, 3, 9)
print('Координаты 1-й точки:', p1)
print('Координаты 2-й точки:', p2)
p3 = p1 + p2
print('Сложение координат:', p3)
p4 = p1 - p2
print('Вычитание координат:', p4)
p5 = p1 * p2
print('Умножение координат:', p5)
p6 = p1 / p2
print('Деление координат:', p6)
if p1 == p2:
    print('Равенство координат: True')
else:
    print('Равенство координат: False')

print('x =', p1['x'], 'x1 =', p2['x'])
print('y =', p1['y'], 'y1 =', p2['y'])
print('z =', p1['z'], 'z1 =', p2['z'])
p1['x'] = 20
print('Запись значения в коррдинату x:', p1['x'])
