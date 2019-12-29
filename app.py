from flask import Flask, render_template, flash
from flask_socketio import SocketIO
from utils.assets import color_cases, load_bishop_moves, load_knight_moves, load_knight_two_steps_moves
from utils.utils import parse_pgn
import random

app = Flask(__name__)
socketio = SocketIO(app=app)

bishop_moves = load_bishop_moves()
knight_moves = load_knight_moves()
knight_two_steps_moves = load_knight_two_steps_moves()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/colors')
def colors_exercise():
    return render_template('colors.html',
                           colors=color_cases,
                           title='Square Color exercise')


@app.route('/bishop_moves')
def bishop_moves_exercise():
    return render_template('bishop_moves.html',
                           title='Bishop Moves exercise',
                           moves=bishop_moves)


@app.route('/knight_moves')
def knight_moves_exercise():
    return render_template('knight_moves.html',
                           title='Knight Moves I exercise')


@app.route('/knight_moves2')
def knight_two_steps_moves_exercise():
    return render_template('knight_moves_two_steps.html',
                           title='Knight Moves II exercise')


@app.route('/test')
def test():
    return render_template('visualization_test.html')


@socketio.on('check_knight_move')
def check_knight_move(data):
    old_stop = data['old_stop']
    old_start = data['old_start']
    decision = data['decision']

    available_moves = knight_moves[old_start]
    if ((old_stop in available_moves) and (decision == 1)) or ((old_stop not in available_moves) and (decision == 0)):
        response = 'Good!'
        score = 1
    else:
        response = 'Wrong!'
        score = -1
    flash(response)
    new_start = random.choice(list(color_cases.keys()))
    if random.uniform(0, 1) > .6:
        new_stop = random.choice(list(knight_moves[new_start]))
    else:
        new_stop = random.choice(list(color_cases.keys()))

    socketio.emit('knight_move_checked',
                  {
                      'new_start': new_start,
                      'new_stop': new_stop,
                      'response': response,
                      'score': score,
                      'old_start': old_start,
                      'old_stop': old_stop
                  }
                  )


@socketio.on('check_knight_two_steps_move')
def check_knight_two_steps_move(data):
    old_stop = data['old_stop']
    old_start = data['old_start']
    decision = data['decision']

    available_moves = knight_two_steps_moves[old_start]
    if ((old_stop in available_moves) and (decision == 1)) or ((old_stop not in available_moves) and (decision == 0)):
        response = 'Good!'
        score = 1
    else:
        response = 'Wrong!'
        score = -1
    flash(response)
    new_start = random.choice(list(color_cases.keys()))
    if random.uniform(0, 1) > .6:
        new_stop = random.choice(list(knight_two_steps_moves[new_start]))
    else:
        new_stop = random.choice(list(color_cases.keys()))

    socketio.emit('knight_two_steps_move_checked',
                  {
                      'new_start': new_start,
                      'new_stop': new_stop,
                      'response': response,
                      'score': score,
                      'old_start': old_start,
                      'old_stop': old_stop
                  }
                  )


@socketio.on('new_game_visualization')
def generate_new_game_visualization():
    pgn, fens = parse_pgn('static/PGN1.pgn')
    print('new_game_visualization')
    print(pgn)

    socketio.emit('new_game_render', {'pgn': pgn, 'fens': fens})


if __name__ == '__main__':
    socketio.run(app, debug=True)
