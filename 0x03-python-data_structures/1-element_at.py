#!/usr/bin/python3

def element_at(my_list, idx):

    if idx < 0:
        return None

    # Check if the index is within the valid range of the list
    if idx < len(my_list):

        return my_list[idx]
