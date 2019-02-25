#!/ust/bin/env python3


message = "You can secret a message when the message is in yourself."
translated = ''

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1


print(translated)
