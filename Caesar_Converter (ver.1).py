#!/usr/bin/python3

import os
import sys

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

OFFSET = 4

new_message = []

if os.path.exists("message.txt"):
    with open("message.txt", "r") as in_file:
        message = in_file.read()
else:
    print("There is no \"message.txt\" file!")
    sys.exit()

for letter in message:
    if letter == " ":
        print(" ", end='')
        new_message.append(" ")
    elif letter == "!":
        print("! ", end='')
        new_message.append("! ")
    elif letter == "\n":
        print("\n", end='')
        new_message.append("\n")
    else:
        decoded = alphabet.index(letter.lower())
        decoded = decoded - OFFSET
        old_text = message.index(letter)
        new_text = alphabet[decoded]
        print(new_text, end='')
        new_message.append(new_text)

with open("new_message.txt", "w") as out_file:
    out_file.write(str("".join(new_message)))
