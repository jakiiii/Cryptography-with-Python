#!/usr/bin/env python3
"""
Algorithm of Reverse Cipher

    - Reverse cipher used a pattern of reversing the string of plan text to convert of reverse text.
    - The process of encryption and decryption is same.
    - The decrypt cipher text, the user simply needs to reverse the cipher text to get the plain text.
"""

# Reverse cipher encryption.
message = "This is program to explain reverse cipher."
translated = ''  # Cipher text is stored in this variable

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print("The cipher encrypt text is: ", translated)


# Reverse cipher decryption.
message = ".rehpic esrever nialpxe ot margorp si sihT"
translated = ''
i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print("The cipher decrypt text is: ", translated)
