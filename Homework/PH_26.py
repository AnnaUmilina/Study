class Clock:
    DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec == other.sec
        # if self.sec == other.sec:
        #     return True
        # return False

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        if self.sec < other.sec:
            return True
        return False

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        if self.sec <= other.sec:
            return True
        return False

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        if self.sec > other.sec:
            return True
        return False

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        if self.sec >= other.sec:
            return True
        return False

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec % other.sec)


c1 = Clock(600)
c2 = Clock(200)
c3 = Clock(300)
if c1 == c2:
    print("Время равно")
else:
    print("Время разное")

if c1 < c2:
    print("c1 < c2 True")
else:
    print("c1 < c2 False")

if c1 <= c2:
    print("c1 <= c2 True")
else:
    print("c1 <= c2 False")

if c1 > c2:
    print("c1 > c2 True")
else:
    print("c1 > c2 False")

if c1 >= c2:
    print("c1 >= c2 True")
else:
    print("c1 >= c2 False")

print('*' * 40)
print('c1:', c1.get_format_time())
c5 = c1 - c2
print('c1 - c2:', c5.get_format_time())
c6 = c1 * c2
print('c1 * c6:', c6.get_format_time())
c7 = c1 // c2
print('c1 // c2:', c7.get_format_time())
c8 = c1 % c2
print('c1 % c2:', c8.get_format_time())
c1 -= c2
print('c1 -= c2:', c1.get_format_time())
c1 *= c2
print('c1 *= c2', c1.get_format_time())
c1 //= c2
print('c1 //= c2:', c1.get_format_time())
c1 %= c2
print('c1 %= c2:', c1.get_format_time())
