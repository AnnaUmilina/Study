# # 1 task

# st = 'I am learning Python. hello, WORLD!'
# first = st.find('h')
# last = st.rfind('h')
# print(st[:first] + st[last + 1:])

# # 2 task

# st = 'I am learning Python. hello, WORLD!'
# first = st.find('h')
# last = st.rfind('h')
# betw = st[first + 1: last]
# print(st[:first + 1] + betw[::-1] + st[last:])

# # 3 task (без replace не смогла сделать)

# str = input('Введите строку: ')
# pst = input('Её заменяемая подстрока: ')
# new = input('Новая подстрока: ')
# print(str.replace(pst, new))

# # 4 task

# poem = '''Ежевику для ежат
# Принесли два ежа.
# Ежевику еле-еле
# Ежата возле ели съели. '''
# st = ''
# lst = []
# for i in range(len(poem)):
#     if poem[i] == ' ' or poem[i] == '\n':
#         lst.append(st)
#         st = ''
#         continue
#     else:
#         st += poem[i]
# print(lst)
# count = 0
# for i in lst:
#     if i.find('е') == 0 or i.find('Е') == 0:
#         count += 1
# print('Количество слов: ', count)
