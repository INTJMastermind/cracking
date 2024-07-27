import math

def get_ordinals(key):
    """
    Returns a list with the ordinal values of the key in alphabetical order
    """
    sorted_keys = sorted(key)
    ordinals = []
    for letter in key:
        index = sorted_keys.index(letter)
        ordinals.append(index)
        sorted_keys[index] = 0

    return ordinals


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
    ordinals = get_ordinals(key)
    num_columns = len(key)
    num_rows = math.ceil(len(message) / len(key))
    num_blanks = num_columns*num_rows - len(message)

    # Each string in plaintext represents a column in the grid:
    plaintext = [[None]*num_columns for i in range(num_rows)]
    
    # The column and row variables point to where in the grid the next 
    # character in the encrypted message will go:
    column = 0
    row = 0

    for symbol in message:
        plaintext[row][ordinals.index(column)] = symbol
        row += 1 #advance to the next row

        # If there are no more rows OR we're at a shaded box, go back 
        # to the first row and the next column:
        if (row == num_rows) or (row == num_rows - 1 and ordinals.index(column) >= num_columns - num_blanks):
            column += 1
            row = 0

    text = ''
    for row in plaintext:
        while None in row:
            row.remove(None)
        word = ''.join(row)
        text += word

    return text


def main():
    key = 'armymen'
    message = 'GEEKS FOR GREEKS'

    m1 = encrypt(key, message)
    print(f'{message} encrypts to: {m1}')
    m2 = decrypt(key, m1)
    
    print(f'{m1} decrypts to: {m2}')
    

if __name__ == '__main__':
    main()