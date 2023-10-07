#!/usr/bin/python3

def element_at(my_list, idx):

    # Check if the index is within the valid range of the list
    if idx < len(my_list):

        # If it is, return the element at that index
        return my_list[idx]

    else:
        return None
