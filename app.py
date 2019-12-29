from flask import Flask, render_template
import json

app = Flask(__name__)

with open('static/colors.json', 'r') as file:
    color_cases = json.load(file)

with open('static/bishop_moves.json', 'r') as file:
    bishop_moves = json.load(file)

with open('static/knight_moves.json', 'r') as file:
    knight_moves = json.load(file)

with open('static/knight_two_steps_moves.json', 'r') as file:
    knight_two_steps_moves = json.load(file)

with open('static/pgns.json', 'r') as file:
    pgns = json.load(file)


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
    return render_template('visualization_test.html',
                           pgns=pgns)


if __name__ == '__main__':
    app.run(debug=True)
