#!/usr/bin/env python3
import pyperclip


def main():
    message = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    key = 8
    cipher_text = encrypt_message(key, message)
    print(cipher_text + ' |')
    pyperclip.copy(cipher_text)


def encrypt_message(key, message):
    cipher_text = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key
    return ''.join(cipher_text)


if __name__ == '__main__':
    main()
