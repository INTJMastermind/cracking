import time
import os
import sys
import transposition_encrypt
import transposition_decrypt

def main():
    input_filename = "frankenstein_encrypted.txt"
    output_filename = "frankenstein_decrypted.txt"

    my_key = 10
    my_mode = 'decrypt' # Set to 'encrypt' or 'decrypt'

    # If the input file does not exist, terminate the program early.
    if not os.path.exists(input_filename):
        print(f'The file {input_filename} does not exist. Quitting...')
        sys.exit()

    # If output file already exists, give the user a chance to quit.
    if os.path.exists(output_filename):
        print(f'This will overwrite the file {output_filename}. (C)ontinue or (Q)uit?')
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    
    # Read in the message from the input file:
    with open(input_filename) as file_obj:
        content = file_obj.read()

    print(f'{my_mode}ing...')

    #Measure how long the encryption / decryption takes:
    start_time = time.time()
    if my_mode == 'encrypt':
        translated = transposition_encrypt.encrypt_message(my_key, content)
    elif my_mode == 'decrypt':
        translated = transposition_decrypt.decrypt_message(my_key, content)
    total_time = round(time.time() - start_time, 2)
    print(f'{my_mode}ion time: {total_time} seconds.')

    with open(output_filename, 'w') as output_file_obj:
        output_file_obj.write(translated)

    print(f'Done {my_mode}ing {input_filename} ({len(content)} characters).')
    print(f'{my_key}ed file is {output_filename}')

if __name__ == '__main__':
    main()