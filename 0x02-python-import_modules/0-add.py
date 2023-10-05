#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    # call the add function and print the result in the specified format
    print("{} + {} = {}".format(a, b, add(a, b)))
