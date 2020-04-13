import sys


def reverse_strings(arg_lst):
    string = " ".join(arg_lst).swapcase()[::-1]
    print(string)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        reverse_strings(sys.argv[1:])
