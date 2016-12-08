from flask import Flask, render_template

from blueprints.movies import movies
from blueprints.series import series

from model.mongo import Movies
from model.mongo import Series

from blueprints.users import users
from model.mongo import Users

app = Flask(__name__)

app.movies = Movies()
app.users = Users()
app.series = Series()

app.secret_key = 'sergnop84q9hbvgu'

@app.route('/')
def hello_world():
    return 'Hello, Continous Integration!'

@app.route('/index')
def index():
    return render_template('index.html')

app.register_blueprint(movies, url_prefix='/movies')

app.register_blueprint(series, url_prefix='/series')

app.register_blueprint(users, url_prefix='/users')

if __name__ == '__main__':
    app.run()
