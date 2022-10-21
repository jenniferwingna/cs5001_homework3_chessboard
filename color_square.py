"""
Wingna Tsoi
CS 5001 Fall22
Programming #2 Determine the color of a specific coordinates on the chessboard
"""
import chessboard


def black_or_white(row, column):
    # Firstly, check the validity of row and column
    if chessboard.check_valid_column(column) is True \
            and chessboard.check_valid_row(row) is True:
        # Then, check the data type of row
        # (there are two different procedure for int and string)
        if isinstance(row, int):
            """The ord() function returns an integer 
              representing the Unicode character.
              For column b, d,f and h, they are identical in color, i.e. BLACK
              Their ord(column) and row are divisible by 2"""
            if ord(column) % 2 == 0 and row % 2 == 0:
                return "BLACK"
            else:
                return "WHITE"
        else:
            """
            if row is not int, then convert it from string to int
            """
            row_int = int(row)
            if ord(column) % 2 == 0 and row_int % 2 == 0:
                return "BLACK"
            else:
                return "WHITE"
    else:
        return False


print(black_or_white("8", "b"))
