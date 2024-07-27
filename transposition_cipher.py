import math
import numpy as np

def get_ordinals(key, reverse = False):
    """
    Returns a dictionary with each letter's position in the key string matched with its ordinal.
    If the reverse option is True, the ordinal values are keys and letter position is the value.
    """
    ordinals = np.argsort(np.argsort(list(key)))

    if reverse == True:
        return {index : value for index, value in enumerate(ordinals)}
    else:
        return {value : index for index, value in enumerate(ordinals)}


def encrypt(key, message):
    ordinals = get_ordinals(key)
    lines = ['']*len(key)

    i = 0
    for char in message:
        lines[ordinals[i]] += char
        i += 1
        if i == len(key):
            i = 0

    return ''.join(lines)


def decrypt(key, message):
    ordinals = get_ordinals(key, True)
    num_cols = len(key)
    num_rows = math.ceil(len(message) / len(key))
    num_blanks = num_cols*num_rows - len(message)

    # Create a matrix empty strings to fill in one character at a time.
    matrix = np.empty((num_rows, num_cols), str)
    
    # The col and row variables point to where in the grid the next 
    # character in the encrypted message will go:
    col = 0
    row = 0

    for char in message:
        matrix[row][ordinals[col]] = char
        row += 1
        # If there are no more rows OR we're at a shaded box, go back to the first row and the next col:
        if (row == num_rows) or (row == num_rows - 1 and ordinals[col] >= num_cols - num_blanks):
            col += 1
            row = 0

    plaintext = ''
    for row in matrix:
        word = ''.join(row)
        plaintext += word

    return plaintext


def main():
    key = 'Diablo'
    message = 'There is no cow level!'

    m1 = encrypt(key, message)
    print(f'{message} encrypts to: {m1}')
    m2 = decrypt(key, m1)
    
    print(f'{m1} decrypts to: {m2}')
    

if __name__ == '__main__':
    main()