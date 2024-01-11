#!/usr/bin/python3
def no_c(my_string):
    updated_str = my_string[:]

    for i in my_string:
        if i != 'c' and i != 'C':
            updated_str += i
        return (updated_str)
