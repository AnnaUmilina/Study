class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f'Счёт #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.num} принадлежащий {self.surname} был закрыт')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate


    @staticmethod
    def convert(value, rate):
        return value * rate

    @staticmethod
    def commission(val):
        perc = val*0.05
        return perc+val

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}.')

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}.')

    def print_balance(self):
        print(f'Текущий баланс {self.value} {Account.suffix}')

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print('Проценты начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f'Сумма для снятия с коммиссией 5% составила :{val} {Account.suffix}.\nНа вашем балансе недостаточно средств')
        else:
            self.value -= val
            print(f'Сумма для снятия с коммиссией 5% составила:{val} {Account.suffix}.\n{val} {Account.suffix} были успешно сняты!')
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()

    def print_info(self):
        print('Информация о счёте')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 20)




acc = Account('12345', 'Долгих', 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.set_usd_rate(2)
acc.convert_to_usd()
acc.set_eur_rate(3)
acc.convert_to_eur()
print()
acc.edit_owner('Дюма')
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(acc.commission(100))
print()
acc.withdraw_money(acc.commission(5000))
print()
acc.add_money(5000)
print()

