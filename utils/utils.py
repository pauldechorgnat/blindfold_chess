import re
from chess.pgn import read_game
import json


def parse_pgn(path):
    with open(path, 'r') as file:
        game = read_game(file)
    with open(path, 'r') as file:
        pgn_string = file.read()
    # getting the pgn only
    pgn_only = re.split(pattern='\n', string=pgn_string)[-1]
    pgn_moves = re.findall(pattern='[0-9]+\. [a-zA-z0-9\-]\+?[\!\?]* [a-zA-z0-9\-]+[0-9]\+?[\!\?]*', string=pgn_string)
    # pgn_moves = re.findall(pattern='[a-zA-z0-9\-]+\+?[\!\?]*', string=pgn_only)
    pgn_moves = re.split(string=pgn_only, pattern=' ')
    pgn_moves = [' '.join(pgn_moves[i * 3:(i + 1) * 3]) for i in range(int(len(pgn_moves) / 3) + 1)]
    # print(pgn_moves)
    bold_moves = []
    fens = ['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1']
    for move in pgn_moves:
        try :
            number, moves = move.split('.')
            new_move = '<b>' + number + '</b>' + '.' + moves
        except ValueError:
            new_move =  new_move

        bold_moves.append(new_move)
    board = game.board()
    for m in game.mainline_moves():
        board.push(m)
        fens.append(board.fen())
    # print(pgn_string.split('\n'))
    title = list(filter(lambda x: 'Event' in x, pgn_string.split('\n')))[0]
    title = title.replace('.??.??)', ')').replace('[Event \"', '').replace('"]', '')
    print(title)

    data = {
        'title': title,
        'bold_moves': bold_moves,
        'pgn_string': pgn_string,
        'fens': fens
    }
    return data

if __name__ == '__main__':
    data = []
    for i in range(10):
        data.append(parse_pgn('static/PGN{}.pgn'.format(i + 1)))
    with open('./static/pgns.json', 'w') as file:
        json.dump(data, file)