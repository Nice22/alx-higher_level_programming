#!/usr/bin/python3
# Nice22
def simple_delete(my_dict, key=""):
    if key in my_dict:
        del my_dict[key]
    return (my_dict)
