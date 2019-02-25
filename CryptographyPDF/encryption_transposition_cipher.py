#!/usr/bin/env python3
import pyperclip


def main():
    my_message = input("Encrypt your text: ")
    my_key = 10
    cipher_text = encrypt_message(my_key, my_message)
    print("Cipher Text is: ", cipher_text + '|')
    pyperclip.copy(cipher_text)


def encrypt_message(key, message):
    cipher_text = [''] * key
    for col in range(key):
        position = col
        while position < len(message):
            cipher_text[col] += message[position]
            position += key
    return ''.join(cipher_text)  # Cipher text


if __name__ == '__main__':
    main()
