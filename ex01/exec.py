import sys


def main():
    string = " ".join(sys.argv[1:]).swapcase()[::-1]
    print(string)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    pass
