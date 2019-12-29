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
                           title='Knight Moves I exercise',
                           moves=knight_moves)


@app.route('/knight_moves2')
def knight_two_steps_moves_exercise():
    return render_template('knight_moves_two_steps.html',
                           title='Knight Moves II exercise',
                           moves=knight_two_steps_moves)


@app.route('/test')
def test():
    return render_template('visualization_test.html')




@socketio.on('new_game_visualization')
def generate_new_game_visualization():
    pgn, fens = parse_pgn('static/PGN1.pgn')
    print('new_game_visualization')
    print(pgn)

    socketio.emit('new_game_render', {'pgn': pgn, 'fens': fens})


if __name__ == '__main__':
    socketio.run(app, debug=True)
