from flask import Flask, render_template,url_for

app = Flask(__name__)
# app.config['ECRET_KEY'] = 'f5ks9jh756sjh54ea79h'

menu = [
    {'name': 'Главная', 'url': '/main'},
    {'name': 'Войти', 'url': '/enter'},
    {'name': 'Поиск книг', 'url': 'search'},
    {'name': 'Моя библиотека', 'url': 'my_library'}
]


@app.route('/')
def main():
    return render_template('main.html', title='Главная страница', menu=menu)


@app.route('/enter')
def enter():
    return render_template('enter.html', title='Вход', menu=menu)


@app.route('/search')
def search():
    return render_template('search.html', title='Поиск', menu=menu)


@app.route('/my_library')
def my_library():
    return render_template('my_library.html', title='Моя библиотека', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
