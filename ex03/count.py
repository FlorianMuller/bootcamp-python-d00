import string


def text_analyzer(*argv):
    """Count the number of uppercase letter, lowercase letter, punctuation and
space in a text"""

    if len(argv) <= 1:
        if len(argv) == 0:
            text = input("What is the text to analyse?\n>> ")
        elif len(argv) == 1:
            text = argv[0]

        stats = {"uppercase": 0, "lowercase": 0, "punctuation": 0, "space": 0}
        for c in text:
            if c in string.ascii_uppercase:
                stats["uppercase"] += 1
            elif c in string.ascii_lowercase:
                stats["lowercase"] += 1
            elif c in string.punctuation:
                stats["punctuation"] += 1
            elif c.isspace():
                stats["space"] += 1

        print(
            f"The text contains {len(text)} characters:\n\n"
            f"- {stats['uppercase']} upper letters\n\n"
            f"- {stats['lowercase']} lower letters\n\n"
            f"- {stats['punctuation']} punctuation marks\n\n"
            f"- {stats['space']} spaces"
        )
    else:
        print("ERROR")


if __name__ == "__main__":
    text_analyzer(
        "Python 2.0, released 2000, introduced features like List "
        "comprehensions and a garbage collection system capable of "
        "collecting reference cycles."
    )
    print("")

    text_analyzer(
        "Python is an interpreted, high-level, general-purpose programming "
        "language. Created by Guido van Rossum and first released in 1991, "
        "Python's design philosophy emphasizes code readability with its "
        "notable use of significant whitespace."
    )
    print("")

    # No parameter
    text_analyzer()
    print("")

    # too many parameter
    text_analyzer("Python", "2.0")
    print("")

    # Documentation
    print(text_analyzer.__doc__)
