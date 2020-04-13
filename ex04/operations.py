import sys


def do_operation(nb1, nb2):
    try:
        return (nb1 + nb2, nb1 - nb2, nb1 * nb2, nb1 / nb2, nb1 % nb2)
    except ZeroDivisionError:
        return (nb1 + nb2, nb1 - nb2, nb1 * nb2, None, None)


def print_operation(nb1, nb2):
    res = do_operation(nb1, nb2)

    print(
        f"Sum:          {res[0]}\n"
        f"Difference:   {res[1]}\n"
        f"Product:      {res[2]}\n"
        f"Quotient:     {res[3] or 'ERROR (div by zero)'}\n"
        f"Remainder:    {res[4] or 'ERROR (modulo by zero)'}"
    )


def print_usage():
    print(
        "Usage: python operations.py <number1> <number2>\n"
        "Example:\n"
        "    python operations.py 10 3"
    )


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_usage()
    elif len(sys.argv) == 2:
        print("InputError: not enough arguments\n")
        print_usage()
    elif len(sys.argv) == 3:
        try:
            print_operation(int(sys.argv[1]), int(sys.argv[2]))
        except ValueError:
            print("InputError: only numbers\n")
            print_usage()
    elif len(sys.argv) > 2:
        print("InputError: too many arguments\n")
        print_usage()
