"""
Wingna Tsoi
CS 5001 Fall22
Programming #2 test function for check_valid_row() and check_valid_column
"""
import chessboard


def test_check_row(row, expected):
    """
    Test 1:
    :param row: 10
    :param expected: False
    :param actual: False

    Test 2:
    :param row: ONE
    :param expected: True
    :param actual: True

    Test 3:
    :param row: 2
    :param expected: True
    :param actual: True
    """
    actual = chessboard.check_valid_row(row)
    print("Row: " + str(row) + ", Expected: "
          + expected + ", Actual: " + str(actual))


def test_check_column(column, expected):
    """
        Test 1:
        :param column: k
        :param expected: False
        :param actual: False

        Test 2:
        :param column: A
        :param expected: True
        :param actual: True

        Test 3:
        :param column: b
        :param expected: True
        :param actual: True
        """
    actual = chessboard.check_valid_column(column)
    print("Column: " + column + ", Expected: "
          + expected + ", Actual: " + str(actual))


test_check_row(10, "False")
test_check_row("1", "True")
test_check_row(2, "True")

test_check_column("k", "False")
test_check_column("A", "True")
test_check_column("b", "True")
