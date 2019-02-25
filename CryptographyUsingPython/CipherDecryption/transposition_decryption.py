#!/usr/bin/env python3
import pyperclip


def main():
    message = 'Lsim p e yoummorasi.rmpyfinene l  ndtdmiyttt tu s ehitisI dxenyntpsut gpgr'
    key = 8
    plain_text = decrypt_message(key, message)
    print(plain_text + ' |')
    pyperclip.copy(plain_text)


def decrypt_message(key, message):
    pass
