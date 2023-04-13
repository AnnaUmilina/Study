def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f'{title}'.center(50, "*"))
            output = func(*args, **kwargs)
            print('*' * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title('Ввод пользовательских данных')
    def initial_data(self):
        print('Действия с фильмами')
        print('1 - добавление фильма\n'
              '2 - каталог фильмов\n'
              '3 - просмотр определенного фильма\n'
              '4 - удаление фильма\n'
              'exit - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    @add_title('Добавление фильма')
    def add_movie(self):
        dict_movie = {
            'название': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'длительность': None,
            'студия': None,
            'актеры': None,
        }

        for key in dict_movie:
            dict_movie[key] = input(f'Введите {key} фильма: ')
        return dict_movie
    @add_title('Каталог фильмов')
    def show_all_movies(self, movies):
        for i, movie in enumerate(movies, start=1):
            print(f'{i}.{movie}')

    def get_user_movie(self):
        user_movie = input('Введите название фильма: ')
        return user_movie

    @add_title('Просмотр определенного фильма')
    def show_single_movie(self, film):
        for key in film:
            print(f'{key} фильма - {film[key]}')

    @add_title('Удаление фильма')
    def remove_single_movie(self, title):
        print(f'Фильм "{title}" был удален')

    def show_incorrect_answer_error(self, answer):
        print(f'Варианта {answer} не существует')

    def show_incorrect_error(self, movie_title):
        print(f'Фильма с названием {movie_title} не существует')
