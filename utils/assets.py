# images:
# https://images.chesscomfiles.com/chess-themes/pieces/neo/80/wp.png

import numpy as np

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

bishop_moves = {}

# for bishop_x in range(8):
#     for bishop_y in range(8):
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
        # print(square, len(bishop_moves[square]))

if __name__ == '__main__':
    import pprint

    # pprint.pprint(files)
    # pprint.pprint(cases)
    # pprint.pprint(colors)
    # print(square_indices)
    # print(diagonals[::-1])
    # pprint.pprint(bishop_moves)
    # pprint.pprint(color_cases)
