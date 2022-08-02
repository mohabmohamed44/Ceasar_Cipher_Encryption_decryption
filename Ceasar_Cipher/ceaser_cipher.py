""" Caesar Cipher, is a shift cipher that uses addition and subtraction to encrypt or decrypt letters """

try:
    # pyperclip copies text from clipboard
    import pyperclip
except ImportError:
    pass #If pyperclip is not installed, do nothing, it is not a big deal

# Every possible letter that can be encrypted or decrypted
# (!) you can add numbers  and punctuation marks to encrypt those symbols as well.

SYMBOLS = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'

print("Caesar Cipher to encrypt or decrypt letters, symbols & punctuation")
print('The caesar cipher encrypts the letter by shifting them over by a')
print('Key number. for example,a key 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on')
print()

# let the user enter if they are encrypting or decrypting:
while True: # keep asking the user until the enters (e) for encrypt or (d) for 
    print('Do you want to (e)ncrypt or (d)ecrypt')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# let the user enter the key to use: 
while True: # keep asking until the user enter a valid key.
    maxKey = len(SYMBOLS) - 1
    print("Please enter the key (0 to {}) to use.".format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# let the user enter the message to encrypt/decrypt:
print('enter the message to {}.'.format(mode))
message = input('> ')

# caesar cipher only work on uppercase letters:
message = message.upper()

# stores the encrypted or decrypted form of message:
translated = ''

# encrypt/decrypt each symbol in message:
for symbol in message:
    if symbol in SYMBOLS:
        # get the encrypted (or decrypted) number for the symbol.
        num = SYMBOLS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # Handle the wrap-around if num is larger than the length of SYMBOLS or less than Zero:
        if num >= len(SYMBOLS):
            num = num -len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        # Just add the symbol without encrypting or decrypting
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen:
print(translated)


try:
    pyperclip.copy(translated) # copy
    print('full {}ed text copied to the clipboard.'.format(mode))
except:
    pass # Donothing of pyperclip was not installed.
