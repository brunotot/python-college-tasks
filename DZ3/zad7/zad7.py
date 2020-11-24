# Napišite program koji će odrediti da li se zadana točka nalazi u zatvorenom ili
# otvorenom prostoru. Prostor je definiran kao niz stringova u sljedećem primjeru:
#
# prostor = [
#   '....................',
#   '....................',
#   '...###########......',
#   '...#..*......#######',
#   '...#.........#.....#',
#   '...########..#.#...#',
#   '.......#....##.##.##',
#   '.......####....#..#.',
#   '..........######.#..',
#   '....................',
# ]
#
# Točka označena sa „*“ nalazi se u prostoru koji je omeđen znakovima „#“ i može
# se kretati samo po poljima označenima sa „.“ (i to samo po vertikali i horizontali).
# Prostor na slici je otvoren jer se s pozicije točke može izaći iz tog prostora tako da
# se slijedi put po poljima ”.” krenuvši od točke ”*” (može biti više takvih puteva).
# Program samo treba vratiti True ako se točka nalazi u otvorenom prostoru ili False
# ako se nalazi u zatvorenom prostoru. Riješite zadatak rekurzivno!!!


# cw ~ clockwise
# ccw ~ counterclockwise
# fw ~ forward

cw = {
    'RIGHT': 'DOWN',
    'DOWN': 'LEFT',
    'LEFT': 'UP',
    'UP': 'RIGHT'
}

ccw = {
    'RIGHT': 'UP',
    'UP': 'LEFT',
    'LEFT': 'DOWN',
    'DOWN': 'RIGHT'
}


def indices_fw(row, col, looking_towards):
    if looking_towards == 'UP':
        return row - 1, col
    elif looking_towards == 'LEFT':
        return row, col - 1
    elif looking_towards == 'DOWN':
        return row + 1, col
    else:
        return row, col + 1


def indices_cw(row, col, looking_towards):
    if looking_towards == 'UP':
        return row, col + 1
    elif looking_towards == 'LEFT':
        return row - 1, col
    elif looking_towards == 'DOWN':
        return row, col - 1
    else:
        return row + 1, col


def indices_ccw(row, col, looking_towards):
    if looking_towards == 'UP':
        return row, col - 1
    elif looking_towards == 'LEFT':
        return row + 1, col
    elif looking_towards == 'DOWN':
        return row, col + 1
    else:
        return row - 1, col


def is_valid(formatted_matrix, row, col, max_row, max_col):
    return max_row > row >= 0 and max_col > col >= 0 and formatted_matrix[row][col] == '.'


def is_traversed_all_paths(row, col, start_row, start_col, looking_towards):
    return ((row == start_row and col == start_col - 1 and looking_towards == 'RIGHT') or
            (row == start_row and col == start_col + 1 and looking_towards == 'LEFT') or
            (row == start_row - 1 and col == start_col and looking_towards == 'DOWN') or
            (row == start_row + 1 and col == start_col and looking_towards == 'UP'))


def is_exit_found(row, col, max_row, max_col):
    return row == 0 or col == 0 or row == max_row - 1 or col == max_col - 1


def is_matrix_open(formatted_matrix, start_row, start_col, row, col, max_row, max_col, looking_towards):
    if is_exit_found(row, col, max_row, max_col):
        return True
    elif is_traversed_all_paths(row, col, start_row, start_col, looking_towards):
        return False
    else:
        ccw_row, ccw_col = indices_ccw(row, col, looking_towards)
        if is_valid(formatted_matrix, ccw_row, ccw_col, max_row, max_col):
            return is_matrix_open(formatted_matrix, start_row, start_col, ccw_row, ccw_col, max_row, max_col, ccw[looking_towards])
        else:
            fw_row, fw_col = indices_fw(row, col, looking_towards)
            if is_valid(formatted_matrix, fw_row, fw_col, max_row, max_col):
                return is_matrix_open(formatted_matrix, start_row, start_col, fw_row, fw_col, max_row, max_col, looking_towards)
            else:
                return is_matrix_open(formatted_matrix, start_row, start_col, row, col, max_row, max_col, cw[looking_towards])


def format_matrix(old_matrix):
    formatted_matrix = list(filter(lambda elem: elem != len(elem) * '.', old_matrix))
    transposed_formatted_matrix = [''.join(tuples) for tuples in zip(*formatted_matrix)]
    transposed_formatted_matrix = list(filter(lambda elem: elem != len(elem) * '.', transposed_formatted_matrix))
    formatted_matrix = list(filter(lambda elem: elem != len(elem) * '.', transposed_formatted_matrix))
    return [''.join(tuples) for tuples in zip(*formatted_matrix)]


def matrix_open(old_matrix):
    formatted_matrix = format_matrix(old_matrix)
    asterisk_row = [x for x in formatted_matrix if '*' in x][0]
    start_row, start_col = formatted_matrix.index(asterisk_row), asterisk_row.index('*')
    current_row, current_col = start_row, start_col
    max_row = len(formatted_matrix)
    max_col = len(formatted_matrix[0])
    return is_matrix_open(formatted_matrix, start_row, start_col, current_row, current_col, max_row, max_col, 'LEFT')


if __name__ == '__main__':
    matrix = ['....................',
              '....................',
              '...###########......',
              '...#...#..*..#######',
              '...#...#.....#.....#',
              '...########..#.#...#',
              '.......#....##.##.##',
              '.......####....#..#.',
              '..........######.#..',
              '....................']
    print(matrix_open(matrix))
