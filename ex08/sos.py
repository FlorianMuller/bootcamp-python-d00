import sys
import re

MORSE_CODE = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}


def to_morse(msg):
    if re.fullmatch(r"[a-zA-Z0-9 ]*", msg):
        return " ".join([MORSE_CODE[letter] for letter in msg.upper()])
    else:
        return "ERROR"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(to_morse(" ".join(sys.argv[1:])))
