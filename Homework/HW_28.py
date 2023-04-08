class Valid:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Длина стороны должна быть положительным числом')
        setattr(instance, self.name, value)


class Triangle:
    a = Valid()
    b = Valid()
    c = Valid()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def info(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return f'Треугольник со сторонами {self.a, self.b, self.c} существует'
        return f'Треугольник со сторонами {self.a, self.b, self.c} не существует'


t1 = Triangle(2, 5, 6)
# t1.c = 12
# print(t1.c)
print(t1.info())
t2 = Triangle(5, 2, 8)
print(t2.info())
t3 = Triangle(7, 3, 6)
print(t3.info())
