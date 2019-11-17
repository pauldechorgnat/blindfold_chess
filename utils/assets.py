cases = [
    [letter + str(i) for i in range(1, 9)]
    for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
]

colors = [
    [0 if (i + j) % 2 == 0 else 1  for i in range(8)]
    for j in range(8)
]
color_cases = {
    cases[i][j]: colors[i][j] for i in range(8) for j in range(8)
}

if __name__ == '__main__':
    import pprint
    pprint.pprint(cases)
    pprint.pprint(colors)
    pprint.pprint(color_cases)
