import sys
import re


def weird_list(string, n):
    return [word for word in re.split(r"[\W|_]+", string) if len(word) > n]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        try:
            print(weird_list(str(sys.argv[1]), int(sys.argv[2])))
        except ValueError:
            print("ERROR")
    pass
