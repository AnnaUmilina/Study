import re


def phone_number(num):
    return re.findall(r'\+*7[\s(]*\d{3}\)*\s*\d{3}(?:[\s-]*\d\d){2}', num)


print(phone_number('+7 499 456-45-78'))
print(phone_number('+74994564578'))
print(phone_number('7 (499) 456 45 78'))
print(phone_number('7 (499) 456-45-78'))
