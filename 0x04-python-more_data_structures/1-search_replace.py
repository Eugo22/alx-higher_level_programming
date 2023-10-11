#!/usr/bin/python3

def search_replace(my_list, search, replace):

    return [y if y != search else replace for y in my_list]
