from model import MovieModel
from view import UserInterface


class Controller:
    def __init__(self):
        self.name_movie = MovieModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None  # ответ пользователя
        while answer != 'exit':
            answer = self.user_interface.initial_data()  # метод возвращ ответ пользователя
            self.working_with_answer(answer)  # работа с ответом пользователя

    def working_with_answer(self, answer):
        if answer == '1':
            movie = self.user_interface.add_movie()    #возвращает словарь с данными о фильме от пользователя
            self.name_movie.add_film(movie)    #вызов метода,который добавляет словарь, сохранивщейся от пользователя
        elif answer == '2':
            movies = self.name_movie.get_all_films()
            self.user_interface.show_all_movies(movies)
        elif answer == '3':
            movie_title = self.user_interface.get_user_movie()
            try:
                film = self.name_movie.get_single_film(movie_title)
            except KeyError:
                self.user_interface.show_incorrect_error(movie_title)
            else:
                self.user_interface.show_single_movie(film)
        elif answer == '4':
            movie_title = self.user_interface.get_user_movie()   #словарь с данными об 1 фильме
            try:
                title = self.name_movie.remove_film(movie_title)     #удаляет сл-рь с опр фил-м внутри общего списка ф-в
            except KeyError:
                self.user_interface.show_incorrect_error(movie_title)
            else:
                self.user_interface.remove_single_movie(title)
        elif answer == 'exit':
            self.name_movie.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)