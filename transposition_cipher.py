import math

def is_key_valid(key, message):
    """
    Checks if a key is valid:
    1. Length less than half of message
    2. No repeated letters in key
    """
    # Check if length of key is less than half that of message.
    if len(key) > len(message)//2:
        print(f'ERROR: Invalid Key: {key}\nKey is too long for message\nMaximum length of key: {len(message)//2} characters.\nCurrent key length: {len(key)} characters.')
        return False
    
    # Check if key contains repeat characters.
    for char in key:
        if key.count(char) > 1:
            print(f'ERROR: Key {key} cannot contain repeated characters.')
            return False
    
    return True

def encrypt(key, message):
    """
    Encrypts a message using transposition cipher.
    """
    # Check if key is valid
    if is_key_valid(key, message) == False:
        return False
    
    # Create a dictionary using letters from key
    lines = dict.fromkeys(key, '')

    # Main loop for transposition cipher:
    i = 0
    for char in message:
        lines[key[i]] += char
        
        # Cycle to the next letter in the key, or back to the start if at the end.
        if i == len(key) - 1:
            i = 0
        else:
            i += 1

    # Arrange each line alphabetically based on key.
    sorted_lines = [lines[letter] for letter in sorted(key)]
    return ''.join(sorted_lines)


def decrypt(key, message):
    """
    Decrypts a message using a transposition cipher.
    """
    # Check if key is valid
    if is_key_valid(key, message) == False:
        return False

    sorted_key = sorted(key)
    num_columns = math.ceil(len(message) / len(key))
    num_blanks = num_columns*len(key) - len(message)
    if num_blanks > 0:
        blank_letters = key[-num_blanks:]
    else:
        blank_letters = ''
    
    # Create a dictionary using letters from key
    lines = dict.fromkeys(key, '')

    # Fill in the transposition cipher matrix by letter in key alphabetically.
    row = 0
    col = 1
    for char in message:
        lines[sorted_key[row]] += char
        if col == num_columns or (col == num_columns - 1 and sorted_key[row] in blank_letters):
            col = 1
            row += 1
        else:
            col += 1
    
    # Rearrange the matrix in the order the key letters appear:
    sorted_lines = [lines[letter] for letter in key]

    # Read down the columns and across the rows to create the message:
    row = 0
    col = 0
    decrypted = ''
    for i in range(len(message)):
        decrypted += sorted_lines[row][col]
        if row == len(key) - 1:
            row = 0
            col += 1
        else:
            row += 1

    return decrypted


def main():
    key = 'dogs'
    message = 'Poopy the magic schnoodle'
    m1 = encrypt(key, message)
    m2 = decrypt(key, m1)
    
    print(f'{message} encrypts to: {m1}')
    print(f'{m1} decrypts to: {m2}')
    

if __name__ == '__main__':
    main()