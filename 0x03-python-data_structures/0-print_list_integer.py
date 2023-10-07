#!/usr/bin/python3

# Define the function print_list_integer that takes a list as input
def print_list_integer(my_list=[]):

    # Iterate through each item in the list
    for num in my_list:

        # Check if the item is an integer
        if isinstance(num, int):

            print("{}".format(num))
