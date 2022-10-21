"""
Wingna Tsoi
CS 5001 Fall22
Homework 3 Programming #2
Design function to check the validity of row and column

"""


def check_valid_row(row):
    # if the data type of row is int
    if isinstance(row, int):
        # determine whether value of row is fall between 1 and 8
        # both side included
        return 8 >= row >= 1
        # if the data is not int
    else:
        """determine whether input is a string """
        return row == "1" or row == "2" or row == "3" \
            or row == "4" or row == "5" or row == "6" \
            or row == "7" or row == "8"


def check_valid_column(column):
    # convert the column(string) to lower case
    column = column.lower()
    """determine whether the column equal to 
    any of the following string (from "a" to "h")"""
    return column == "a" or column == "b" \
        or column == "c" or column == "d" \
        or column == "e" or column == "f" \
        or column == "g" or column == "h"



