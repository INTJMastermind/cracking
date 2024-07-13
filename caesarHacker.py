# Casesar Cipher Hacker

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

while True:
    #message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
    message = input('>> ')

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so tha tthe
        # previous iteration's value for translated is cleared:
        translated = ''

        # The rest of the program is almost the same as the Caesar program:

        # Loop through each symbol in message:
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wraparound:
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + SYMBOLS[translatedIndex]
            else:
                # Append the symbol without encrypting / decrypting:
                translated = translated + symbol

        #Display every possible decryption:
        print('Key #%s: %s' % (key, translated))