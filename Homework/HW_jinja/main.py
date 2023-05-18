from jinja2 import Environment, FileSystemLoader

homework = [
    {'lesson':'Геометрия','task':'458,459,461'},
    {'lesson':'Литература','task':'Обломов с.123-200'},
    {'lesson':'История','task':'п.12,табл.2'}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(hw=homework, title = 'Домашнее задание')

print(msg)

