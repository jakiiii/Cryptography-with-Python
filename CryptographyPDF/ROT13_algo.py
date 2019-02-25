#!/usr/bin/env python2
"""
ROT13 cipher refers to the abbreviated form Rotate by 13 places.
It is a special case of Caesar Cipher in which shift is always 13.
"""

from string import maketrans


rot13trans = maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                       'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')


# Function to translate plain text
def rot13(text):
    return text.translate(rot13trans)


def main():
    txt = "ROT13 Algorithm"

    print(rot13(txt))


if __name__ == "__main__":
    main()
