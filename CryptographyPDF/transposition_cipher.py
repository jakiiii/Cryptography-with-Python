#!/usr/bin/env python3


def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]


def encode(key, plaintext):
    order = {
        int(val): num for num, val in enumerate(key)
    }

    cipher_text = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                cipher_text += part[order[index]]
            except IndexError:
                continue
    return cipher_text


print(encode('3214', 'HELLO WORLD'))
