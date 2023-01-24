# Chess Pieces. Program to check if a cell is threaten by a chess piece


def is_threaten_king(ori_row, ori_col, dest_row, dest_col):
    """
    This function hecks if the  (dest_row, dest_col)
    is threaten by a KING in position (ori_row, ori_col)


    Parameters
    ----------
    ori_row, ori_col, dest_row, dest_col: integer
      1<= ori_row, ori_col, dest_row, dest_col <= 8
    """
    return ori_row-1 <= dest_row and dest_row <= ori_row+1 and \
        ori_col-1 <= dest_col and dest_col <= ori_col+1 and \
        (ori_row != dest_row or ori_col != dest_col)


def is_threaten_rook(ori_row, ori_col, dest_row, dest_col):
    """
    This function hecks if the  (dest_row, dest_col)
    is threaten by a ROOK in position (ori_row, ori_col)


    Parameters
    ----------
    ori_row, ori_col, dest_row, dest_col: integer
      1<= ori_row, ori_col, dest_row, dest_col <= 8
    """
    return (ori_row == dest_row or \
        ori_col == dest_col) and \
        (ori_row != dest_row or ori_col != dest_col)



def is_threaten_bishop(ori_row, ori_col, dest_row, dest_col):
    """
    This function hecks if the  (dest_row, dest_col)
    is threaten by a BISHOP in position (ori_row, ori_col)


    Parameters
    ----------
    ori_row, ori_col, dest_row, dest_col: integer
      1<= ori_row, ori_col, dest_row, dest_col <= 8
    """
    return (ori_row-ori_col == dest_row-dest_col or \
        ori_row+ori_col == dest_row+dest_col) and \
        (ori_row != dest_row or ori_col != dest_col)


def is_threaten_queen(ori_row, ori_col, dest_row, dest_col):
    """
    This function hecks if the  (dest_row, dest_col)
    is threaten by a QUEEN in position (ori_row, ori_col)


    Parameters
    ----------
    ori_row, ori_col, dest_row, dest_col: integer
      1<= ori_row, ori_col, dest_row, dest_col <= 8
    """
    return is_threaten_bishop(ori_row, ori_col, dest_row, dest_col) or \
        is_threaten_rook(ori_row, ori_col, dest_row, dest_col)



def is_threaten_knight(ori_row, ori_col, dest_row, dest_col):
    """
    This function hecks if the  (dest_row, dest_col)
    is threaten by a KNIGHT in position (ori_row, ori_col)


    Parameters
    ----------
    ori_row, ori_col, dest_row, dest_col: integer
      1<= ori_row, ori_col, dest_row, dest_col <= 8
    """
    return (abs(ori_row - dest_row) == 2 and \
             abs(ori_col - dest_col) == 1) or \
           (abs(ori_row - dest_row) == 1 and \
             abs(ori_col - dest_col) == 2)


def is_threaten(piece, ori_row, ori_col, dest_row, dest_col):
    """
    This is the main function that checks if the cell (dest_row, dest_col)
    is threaten  by the piece in position (ori_row, ori_col)

    Parameters
    ----------
      piece: char
            'K': King
            'Q': Queen
            'R': Rook
            'B': Bishop
            'N': Knight
      ori_row: integer
             1<= ori_row<8
      ori_col: char
             a char from 'a' to 'h'
      dest_row: integer
             1<= dest_row<8
      dest_col: char
             a char from 'a' to 'h'
    """
    dest_col_int = ord(dest_col) - ord('a') + 1
    ori_col_int = ord(ori_col) - ord('a') + 1

    if piece == 'K':
        return is_threaten_king(ori_col_int, ori_row, \
                                dest_col_int, dest_row)
    elif piece == 'Q':
        return is_threaten_queen(ori_col_int, ori_row, \
                                 dest_col_int, dest_row)
    elif piece == 'R':
        return is_threaten_rook(ori_col_int, ori_row, \
                                dest_col_int, dest_row)
    elif piece == 'B':
        return is_threaten_bishop(ori_col_int, ori_row, \
                                  dest_col_int, dest_row)
    elif piece == 'N':
        return is_threaten_knight(ori_col_int, ori_row, \
                                  dest_col_int, dest_row)
    else:
        raise Exception('Unknown piece \'{0}\''.format(piece))


def test(func, row, col):
    for d_row in range(1,9):
        for d_col in range(1,9):
            if func(row, col, d_row, d_col):
                print('*', end="")
            else:
                print("-", end="")
        print()


def test_king(row, col):
    test(is_threaten_king, row, col)


def test_bishop(row, col):
    test(is_threaten_bishop, row, col)


def test_rook(row, col):
    test(is_threaten_rook, row, col)


def test_queen(row, col):
    test(is_threaten_queen, row, col)


def test_knight(row, col):
    test(is_threaten_knight, row, col)


def test_is_threaten(piece, row, col):
    for d_row in range(1,9):
        print('{0}:'.format(d_row), end='')
        for d_col_int in range(8):
            d_col = chr(d_col_int + ord('a'))
            if is_threaten(piece, row, col, d_row, d_col):
                print('*', end='')
            elif row == d_col  and col == d_col:
                print(piece, end='')
            else:
                print("-", end='')
        print()
    print("  abcdefgh")



CELLS=[\
       [1, 'a'], \
       [4, 'a'], \
       [4, 'b'], \
       [4, 'g'], \
       [4, 'h'], \
       [7, 'e'], \
       [8, 'e'], \
       [8, 'h'] ]

PIECES = ['K', 'Q', 'N', 'R', 'B']


def gen_tests():
    count = 0
    for piece in PIECES:
        print('\n----------\nTesting {0}\n----------'.format(piece))
        for cell in CELLS:
            test_is_threaten(piece, cell[0], cell[1])
