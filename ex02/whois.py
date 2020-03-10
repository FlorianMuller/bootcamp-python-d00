import sys


def main():
    try:
        nbr = int(sys.argv[1])

        if nbr == 0:
            print("I'm Zero.")
        elif (nbr % 2) == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except ValueError:
        print("ERROR")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    elif len(sys.argv) > 2:
        print("ERROR")
