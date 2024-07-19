# Transposition Cypher Decryption

import math
import pyperclip

def main():
    message = 'Cenoonommstmme oo snnio. s s c'
    key = 8

    plaintext = decrypt_message(key, message)

    # Print with a | pipe character after it in case
    # there are spaces at the end of the decrypted message:
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decrypt_message(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list of strings.
    # First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    num_columns = math.ceil(len(message) / key)
    # The number of "rows" in our grid:
    num_rows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    num_shaded_boxes = num_columns*num_rows - len(message)

    # Each string in plaintext represents a column in the grid:
    plaintext = [''] * num_columns

    # The column and row variables point to where in the grid the next 
    # character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 #point to the next column

        # If there are no more columns OR we're at a shaded box, go back 
        # to the first column and the next row:
        if (column == num_columns) or (column == num_columns - 1 and row >= num_rows - num_shaded_boxes):
            column = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()