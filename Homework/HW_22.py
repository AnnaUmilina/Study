from math import pi


class Sphere:
    def __init__(self, radius, volume, area, x, y, z):
        self.__radius = radius
        self.__volume = volume
        self.__area = area
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        if isinstance(new_radius, (int, float)):
            self.__radius = new_radius
        else:
            print('Радиус указывается цифрами')

    @property
    def volume(self):
        return 4 / 3 * pi * self.__radius ** 3

    @property
    def area(self):
        return 4 * pi * self.__radius ** 2

    @property
    def center(self):
        return (self.__x, self.__y, self.__z)

    def set_center(self, new_x, new_y, new_z):
        if isinstance(new_x, (int, float)) and isinstance(new_y, (int, float)) and isinstance(new_z, (int, float)):
            self.__x = new_x
            self.__y = new_y
            self.__z = new_z
        else:
            print('Радиус указывается цифрами')

    def is_point_inside(self, x, y, z):
        return (self.__x - x) ** 2 + (self.__y - y) ** 2 + (self.__z - z) ** 2 < self.__radius ** 2


s1 = Sphere(0.6, 0, 0, 0, 0, 0)
print('Радиус сферы: ', s1.radius)
print('Объём сферы: ', s1.volume)
print('Площадь внешней поверхности сферы: ', s1.area)
print('Координаты центра сферы: ', s1.center)
# s1.set_center(0, 0.2, 0.3)            #никак не смогла через сеттер внести 3 значения, поэтому просто через метод set
# print('Координаты смещенного центра сферы: ', s1.center)
print('Находится ли точка внутри сферы:', s1.is_point_inside(0, -1.5, 0))
s1.radius = 1.6
print('Находится ли точка внутри сферы:', s1.is_point_inside(0, -1.5, 0))
