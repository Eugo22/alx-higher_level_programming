#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:

        if x == 0:
            return 0

        else:

            print(my_list[0], end=' ')

            return 1 + safe_print_list(my_list[1:], x-1)

    except IndexError:

        return 0
