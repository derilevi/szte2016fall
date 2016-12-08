from flask import Flask, render_template, jsonify

from blueprints.movies import movies
from blueprints.series import series
from blueprints.users import users

from model.mongo import Movies
from model.mongo import Series
from model.mongo import Users
from model.mongo import Health

app = Flask(__name__)

app.movies = Movies()
app.users = Users()
app.series = Series()
app.health = Health()

app.secret_key = 'sergnop84q9hbvgu'


@app.route('/')
def hello_world():
    return 'Hello, Continous Integration!'


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/health')
def health():
    h = {'health': True}
    h.update({'database_connection': app.health.check_connection()})
    for k, v in h.items():
        if not v:
            h['health'] = False
            break
    return jsonify(h)

app.register_blueprint(movies, url_prefix='/movies')

app.register_blueprint(series, url_prefix='/series')

app.register_blueprint(users, url_prefix='/users')

if __name__ == '__main__':
    app.run()
