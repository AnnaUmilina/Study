class Student:
    def __init__(self, name):
        self.name = name
        self.info = self.Info()

    def show(self):
        print(self.name, '=>', end=' ')

    class Info:
        def __init__(self):
            self.model = 'HP'
            self.processor = "i7"
            self.memory = '16'

        def show(self):
            print(f'{self.model}, {self.processor}, {self.memory}')


s = Student('Владимир')
s.show()
i = s.info
i.show()

s2 = Student('Роман')
s2.show()
i2 = s2.info
i2.show()
