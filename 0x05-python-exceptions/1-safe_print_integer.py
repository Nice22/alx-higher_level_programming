#!/usr/bin/python3
# Nice22
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
