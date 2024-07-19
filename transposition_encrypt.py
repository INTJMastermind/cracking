# Transposition Cipher Encryption

import pyperclip

def main():
    my_message = 'Common sense is not so common.'
    my_key = 8

    ciphertext = encrypt_message(my_key, my_message)

    # Print the encrypted string in ciphertext ot the screen, with
    # a | ("pipe" character ) after it in case there are spaces at
    # the end of the encrypted message:
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the keyboard:
    pyperclip.copy(ciphertext)


def encrypt_message(key, message):
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key

    # Loop through each column in the ciphertext:
    for column in range(key):
        current_index = column

        # Keep looping until current_index goes past the message length
        while current_index < len(message):
            # Place the character at current_index in message at the
            # end of the current column in the ciphertext list:
            ciphertext[column] += message[current_index]

            # Move current_index over:
            current_index += key
    
    # Convert the ciphertext list to a single string value and return it:
    return ''.join(ciphertext)

# If transpositionEncrypt.py is run ( instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()