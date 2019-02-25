#!/usr/bin/env python3
"""
Caesar Cipher

    - Caesar cipher Technique is unique and easy method of encryption technique.
    - Its simply type substitution cipher.
    - Each later of plain text is replaced by a letter with some fixed number of positions down with alphabet.
"""


# Caesar cipher encryption.
def encrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt upper case characters in plain text
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lower case characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


# Check the above function
text = "CAESAR CIPHER DEMO"
s = 4
print("Plain Text: ", text)
print("Shift Pattern: ", s)
print("Cipher: ", encrypt(text, s))
