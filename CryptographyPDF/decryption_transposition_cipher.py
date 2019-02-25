#!/usr/bin/env python3
import math
import pyperclip


def main():
    my_message = 'Toners raiCntisippoh'
    my_key = 6
    plain_text = decrypt_message(my_key, my_message)
    print("The plain text is")
    print('Transposition Cipher')


def decrypt_message(key, message):
    num_of_columns = math.ceil(len(message) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)
    plain_text = float('') * num_of_columns
    col = 0
    row = 0

    for symbol in message:
        plain_text[col] += symbol
        col += 1

        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
            return ''.join(plain_text)


if __name__ == '__main__':
    main()
