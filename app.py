from flask import Flask, render_template, flash
from flask_socketio import SocketIO
from utils.assets import color_cases, load_bishop_moves
import random

app = Flask(__name__)
socketio = SocketIO(app=app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/colors')
def colors():
    return render_template('colors.html')


@app.route('/bishop_moves')
def bishop_moves():
    return render_template('bishop_moves.html')


@socketio.on('check_color')
def check_color(data):
    if color_cases[data['square']] == data['color']:
        response = 'Good!'
    else:
        response = 'Wrong!'

    flash(response)
    new_square = random.choice(list(color_cases.keys()))
    score = -1 + 2 * (response == 'Good!')

    socketio.emit('color_checked',
                  {
                      'new_square': new_square,
                      'response': response,
                      'score': score,
                      'old_square': data['square']
                  }
                  )


@socketio.on('check_bishop_move')
def check_bishop_move(data):
    old_stop = data['old_stop']
    old_start = data['old_start']
    decision = data['decision']
    bishop_moves = load_bishop_moves()

    available_moves = bishop_moves[old_start]
    if ((old_stop in available_moves) and (decision == 1)) or ((old_stop not in available_moves) and (decision == 0)):
        response = 'Good!'
        score = 1
    else:
        response = 'Wrong!'
        score = -1
    flash(response)
    new_start = random.choice(list(color_cases.keys()))
    if random.uniform(0, 1) > .6:
        new_stop = random.choice(list(bishop_moves[new_start]))
    else:
        new_stop = random.choice(list(color_cases.keys()))

    socketio.emit('bishop_move_checked',
                  {
                      'new_start': new_start,
                      'new_stop': new_stop,
                      'response': response,
                      'score': score,
                      'old_start': old_start,
                      'old_stop': old_stop
                  }
                  )


if __name__ == '__main__':
    socketio.run(app)
