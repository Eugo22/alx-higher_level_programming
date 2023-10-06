#!/usr/bin/python3
import sys

if __name__ == "__main__":

    num_args = len(sys.argv) - 1

    """Print the number of and list of arguments."""

    start = 's' if num_args != 1 else ''
    ending = '.' if num_args == 0 else ':'
    print("{} argument{}{}".format(num_args, start, ending))
    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
