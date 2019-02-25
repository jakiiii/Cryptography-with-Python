#!/usr/bin/env python3
import pyperclip


message = "This is a secret message"
key = 13
mode = 'encrypt'
LATTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
# num = 0

message = message.upper()

for symbol in message:
    if symbol in LATTERS:
        num = LATTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

    if num >= len(LATTERS):
        num = num - len(LATTERS)
    elif num < 0:
        num = num + len(LATTERS)
        translated = translated + LATTERS[num]
    else:
        translated = translated + symbol


print(translated)
pyperclip.copy(translated)
