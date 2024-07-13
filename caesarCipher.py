# Caesar Cipher

import pyperclip

# The string to be encrypted / decrypted:
message = input('What is your message: ')

# The encryption / decription key
key = int(input('What is the encryption key: '))

# Whether the program encrypts or decrypts:
mode = input('Please type "encrypt" or "decrypt": ')

# Every posible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted / decrypted form of the message:
translated = ''

for symbol in message:
    #Note: Only symbols in the SYMBOLS string can be encrypted / decrpted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #Perform the encryption / decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        #Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting / decryptiong:
        translated = translated + symbol
    
# Output the translated string:
print(translated)
pyperclip.copy(translated)