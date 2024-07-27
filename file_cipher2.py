import time
import os
import sys
import transposition_cipher as tc

def main():
    """
    Performs a double transposition encryption, followed by a double-transposition decryption using the same keys.
    """
    file_name = "frankenstein"
    input_file = file_name+".txt"
    encrypted_file = file_name+"_encrypted.txt"
    decrypted_file = file_name+"_decrypted.txt"

    key1 = 'maryshelly'
    key2 = 'frankenstein'
    
    # If the input file does not exist, terminate the program early.
    if not os.path.exists(input_file):
        print(f'The file {input_file} does not exist. Quitting...')
        sys.exit()

    # Read in the message from the input file:
    with open(input_file) as f:
        content = f.read()

    #Measure how long the encryption / decryption takes:
    start_time = time.time()

    #Perform two transposition encryptions using key1 and key2.
    encrypted = tc.encrypt(key2, tc.encrypt(key1, content))

    #Perform two transposition decryptions using key1 and key2.
    decrypted = tc.decrypt(key1, tc.decrypt(key2, encrypted))

    #Calculate the total time for both operations.
    total_time = round(time.time() - start_time, 2)
    print(f'Total time: {total_time} seconds.')

    # Write the encrypted and decrypted files.
    with open(encrypted_file, 'w') as f:
        f.write(encrypted)

    with open(decrypted_file, 'w') as f:
        f.write(decrypted)

if __name__ == '__main__':
    main()