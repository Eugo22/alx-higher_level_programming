#!/usr/bin/python3


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # Printing the result of addition
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Printing the result of subtraction
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Printing the result of multiplication
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Printing the result of division
    print("{} / {} = {}".format(a, b, div(a, b)))
