import re
from chess.pgn import Game
from chess import Board
from chess.pgn import read_game

def parse_pgn(path):
    with open(path, 'r') as file:
        game = read_game(file)
    with open(path, 'r') as file:
        pgn_string = file.read()
    # getting the pgn only
    pgn_only = re.split(pattern='\n', string=pgn_string)[-1]
    pgn_moves = re.findall(pattern='[0-9]+\. [a-zA-z]+[0-9]\+?[\!\?]* [a-zA-z\+]+[0-9]\+?[\!\?]*', string=pgn_string)
    bold_moves = []
    fens = ['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1']
    for move in pgn_moves:
        number, moves = move.split('.')
        new_move = '<b>' + number + '</b>'+ '.' + moves
        bold_moves.append(new_move

        )
    board = game.board()
    for m in game.mainline_moves():

        board.push(m)
        fens.append(board.fen())


    return bold_moves, fens


if __name__ == '__main__':
    m, f = parse_pgn('static/PGN.pgn')
    print(f)
