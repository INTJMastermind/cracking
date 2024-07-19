# Transposition Cipher Test

import random
import sys
import transposition_encrypt
import transposition_decrypt

def main():
    random.seed(42) # Set the random "seed" to a static value.

    for i in range(20): # Run 20 tests.
        # Generate random messages to test.

        # The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message to a list to shuffle it:
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) # Convert the list back to a string.

        print(f'Test #{i+1}: {message[:50]}')

        # Check all possible keys for each message:
        for key in range(1, int(len(message)/2)):
            encrypted = transposition_encrypt.encrypt_message(key, message)
            decrypted = transposition_decrypt.decrypt_message(key, message)

            # If the decryption doesnt match the original message, display an error message and quit:
            if message != decrypted:
                print(f'Mismatch with key {key} and message {message}.')
                print(f'Decrypted as {message}')
                sys.exit()
            
    print('Transposition cipher test passed.')

if __name__ == '__main__':
    main()