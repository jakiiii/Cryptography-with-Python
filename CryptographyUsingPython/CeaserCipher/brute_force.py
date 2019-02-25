#!/usr/bin/env python3


message = 'ABCH HKHEL KHJNK DFGAS OFSX'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '


for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        num = LETTERS.find(symbol)
        num = num - key
        if num < 0:
            num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol


print("#{key}, {translated}".format(key=key, translated=translated))
