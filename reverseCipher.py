# Reverse Cipher

message = input('Enter message: ')
translated = ''

i = len(message)-1
while i >= 0:
    translated = translated + message[i]
    i = i-1

print(translated)

decoded = ''

i = len(translated)-1
while i >= 0:
    decoded = decoded + translated[i]
    i = i-1

print(decoded)

