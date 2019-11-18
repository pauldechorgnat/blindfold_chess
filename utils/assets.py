import json
import numpy as np

# images:
# https://images.chesscomfiles.com/chess-themes/pieces/neo/80/wp.png

file_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row_names = ['1', '2', '3', '4', '5', '6', '7', '8']

files = np.tile(np.array(file_names, ndmin=2).T, 8)

cases = [
    [letter + str(i) for i in range(1, 9)]
    for letter in file_names
]

colors = [
    [0 if (i + j) % 2 == 0 else 1 for i in range(8)]
    for j in range(8)
]

color_cases = {
    cases[i][j]: colors[i][j] for i in range(8) for j in range(8)
}

# bishop moves
square_indices = np.tile(np.arange(0, 8), 8).reshape(8, 8)
diagonals = square_indices - square_indices.T
neg_diagonals = diagonals[::-1]


# for bishop_x in range(8):
#     for bishop_y in range(8):
def compute_bishop_moves(path='./bishop_moves.json'):
    bishop_moves = {}
    for bishop_x in range(8):
        for bishop_y in range(8):
            moves = []
            for x in range(8):
                y = x

                if bishop_x + x < 8:
                    if bishop_y + y < 8:
                        moves.append((bishop_x + x, bishop_y + y))
                    if bishop_y - y >= 0:
                        moves.append((bishop_x + x, bishop_y - y))
                if bishop_x - x >= 0:
                    if bishop_y + y < 8:
                        moves.append((bishop_x - x, bishop_y + y))
                    if bishop_y - y >= 0:
                        moves.append((bishop_x - x, bishop_y - y))

            square = file_names[bishop_x] + row_names[bishop_y]
            bishop_moves[square] = [file_names[x] + row_names[y] for x, y in moves if file_names[x] + row_names[y] != square]
    if path is not None:
        with open(path, 'w') as file:
            json.dump(bishop_moves, file)
    return bishop_moves

def compute_knight_moves(path='./knight_moves.json'):
    knight_moves = {}
    for knight_x in range(8):
        for knight_y in range(8):
            moves = []
            for x in [-1, 1]:
                for y in [-2, 2]:
                    if knight_x + x < 8 and knight_x + x >=0:
                        if knight_y + y < 8 and knight_y + y >=0:
                            moves.append((knight_x + x, knight_y + y))
                        if knight_y - y >= 0 and knight_y - y < 8:
                            moves.append((knight_x + x, knight_y - y))
                    if knight_x - x >= 0  and knight_x - x < 8:
                        if knight_y + y < 8 and knight_y + y >=0:
                            moves.append((knight_x - x, knight_y + y))
                        if knight_y - y >= 0 and knight_y - y < 8:
                            moves.append((knight_x - x, knight_y - y))
            for x in [-2, 2]:
                for y in [-1, 1]:
                    if knight_x + x < 8  and knight_x + x >=0:
                        if knight_y + y < 8 and knight_y + y >=0:
                            moves.append((knight_x + x, knight_y + y))
                        if knight_y - y >= 0 and knight_y - y < 8:
                            moves.append((knight_x + x, knight_y - y))
                    if knight_x - x >= 0 and knight_x - x < 8:
                        if knight_y + y < 8 and knight_y + y >=0:
                            moves.append((knight_x - x, knight_y + y))
                        if knight_y - y >= 0 and knight_y - y < 8:
                            moves.append((knight_x - x, knight_y - y))

            square = file_names[knight_x] + row_names[knight_y]
            pprint.pprint(square)
            pprint.pprint(moves)

            knight_moves[square] = list(set([file_names[x] + row_names[y] for x, y in moves if file_names[x] + row_names[y] != square]))
    if path is not None:
        with open(path, 'w') as file:
            json.dump(knight_moves, file)
    return knight_moves

def load_bishop_moves(path='./bishop_moves.json'):
    with open(path, 'r') as file:
        return json.load(file)

def load_knight_moves(path='./knight_moves.json'):
    with open(path, 'r') as file:
        return json.load(file)

if __name__ == '__main__':
    import pprint
    bishop_moves = compute_bishop_moves(path='./bishop_moves.json')
    knight_moves = compute_knight_moves(path='./knight_moves.json')
    pprint.pprint(knight_moves)
