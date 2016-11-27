#!/usr/bin/python3

import os


# Colours and format of fonts.
class color:
    GREEN = "\033[92m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"


def decoration():
    """
    Decoration "dash-line" text separator.
    """
    print("-" * 70)  # Default width = 70, fitted to the console.


def open_file():
    """
    Search if the filename, which was inputted by user, is in the script's directory.
    NOT FOUND: Display help annotations and ask user repeatedly about correct filename.
    FOUND: Read text from selected file and display it's content as "old_message".
    """
    while True:
        decoration()
        input_file = input("Type a name of text file with message to convert: ")
        # Alternatively method to: "if os.path.exists(input_file):"
        try:
            with open(input_file, "r") as in_file:
                old_message = in_file.read()
                decoration()
                print(color.GREEN + "File found!" + color.END)
                decoration()
                print(color.BOLD + "ORIGINAL MESSAGE:\n\n" + color.END + old_message, end='')
            return input_file, old_message

        except FileNotFoundError:
            decoration()
            print(color.RED + "There is no \"{}\" file in the following directory!".format(input_file) + color.END)
            decoration()
            print(color.RED + "NOTE #1: Don't forget about obligatory file's extension \".txt\"" + color.END)
            decoration()
            print(color.RED + "NOTE #2: Your file must be in the same directory as python script!" + color.END)


def decryption(old_message):
    """
    Caesar's encoding-decoding algorithm (shift letter index by "n" position).
    """
    characters = [" ", "!", "?", ",", ".", ":", "/", "\n"]
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    new_message = []

    while True:
        try:
            decoration()
            offset = int(input("Type a number of Caesar's shift (0-26): "))  # For "message.txt" default offset = 4.

            if offset in range(0, 27):  # Allowed numbers is from range 0 to 26.
                decoration()
                print(color.BOLD + "TRANSLATED MESSAGE:\n" + color.END)
                # Leave unchanged non-literal characters from list "characters".
                for letter in old_message:
                    if letter in characters:
                        print(letter, end='')
                        new_message.append(letter)  # Append them directly.
                    else:

                        # Leave the uppercase letters from input message as uppercase.
                        if letter.isupper():
                            converted = alphabet.index(letter.lower())  # Compare any "letter" from "old_message" to "alphabet" which contains only lowercase.
                            converted -= offset
                            old_text = old_message.index(letter)
                            new_text = alphabet[converted].upper()  # Read new lowercase letter from "alphabet" and change it to uppercase.
                            new_message.append(new_text)

                        # Leave the lowercase letters from input message unchanged as lowercase.
                        if letter.islower():
                            converted = alphabet.index(letter.lower())  # Compare any "letter" from "old_message" to "alphabet" which contains only lowercase.
                            converted -= offset
                            old_text = old_message.index(letter)
                            new_text = alphabet[converted].lower()  # Readability: It may be written without "lower()". Lower is just lower.
                            new_message.append(new_text)
                        print(new_text, end='')
                decoration()
                return new_message

            else:
                decoration()
                print(color.RED + "INDEX ERROR: Type a number from range 0 to 26!" + color.END)

        except ValueError:
            decoration()
            print(color.RED + "VALUE ERROR: Type an integer number only!" + color.END)


def save_file(input_file, new_message):
    """
    Creating a new file with converted message in it.
    New filename is basing on the previous input file.
    """
    new_file = "new_{}".format(input_file)  # Apply extension ".txt" to the filename, because in the input filename extension was obligatory.
    with open(new_file, "w") as out_file:
        out_file.write(str("".join(new_message)))
        print(color.GREEN + "File saved as: {}!".format(new_file) + color.END)
        decoration()


def main():
    decoration()
    print("""    Welcome to the "Python Caesar Converter"!

    This program helps you to encode-decode
    any text message from a file, using the
    ancient method called: Caesar's algorithm""")
    # Search for input filename. Read text from specified file. Return it as "old_message".
    input_file, old_message = open_file()
    # Encode or decode text message and create new one in empty list "new_message".
    new_message = decryption(old_message)
    # Save the newly created text message to the file "new_OriginalFileName.txt".
    save_file(input_file, new_message)

if __name__ == "__main__":
    main()
