from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO
from utils.assets import color_cases
from utils.bootstrap import change_version
import random

app = Flask(__name__)
# bs = Bootstrap(app=app)
# app = change_version(app)
socket = SocketIO(app=app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/colors')
def colors():
    return render_template('colors.html')

@socket.on('check_color')
def check_color(data):
    print(data)
    if color_cases[data['square']] == data['color']:
        response = 'Good!'
    else:
        response = 'Wrong!'

    flash(response)
    new_square = random.choice(list(color_cases.keys()))
    score = -1 + 2 * (response == 'Good!')

    socket.emit('color_checked',
                {
                    'new_square': new_square,
                    'response': response,
                    'score' : score,
                    'old_square': data['square']
                }
                )


if __name__ == '__main__':
    socket.run(app, debug=True)