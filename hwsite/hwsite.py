from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cource.db'
db = SQLAlchemy(app)

menu = [{'name': 'Главная', 'url': '/'},
        {'name': 'Добавить статью', 'url': '/register'}]


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Course {self.id}>'


@app.route('/', methods=['POST', 'GET'])
def main():
    courses = Course.query.order_by(Course.date_created.desc()).all()
    return render_template('main.html', title='Главная', courses=courses, menu=menu)


@app.route('/delete/<int:id>')
def delete(id):
    course_to_delete = Course.query.get_or_404(id)
    try:
        db.session.delete(course_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f'Не удалось удалить задачу {e}'


@app.route('/programme/<int:id>', methods=['POST', 'GET'])
def programme(id):
    course = Course.query.get_or_404(id)
    if request.method == 'POST':
        course.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'Не удалось обновить задачу {e}'
    else:
        return render_template('programme.html', course=course, menu=menu)


@app.route('/register', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        course_name = request.form['name']
        course_title = request.form['title']
        course_content = request.form['content']
        new_article = Course(content=course_content, name=course_name, title=course_title)
        try:
            db.session.add(new_article)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'Не удалось добавить вашу задачу {e}'
    else:
        return render_template('register.html', title='Добавить статью', menu=menu)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
