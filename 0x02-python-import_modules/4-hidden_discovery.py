#!/usr/bin/python3
# Nice22

import hidden_4

if __name__ == "__main__":
    """a program that prints all the names
    defined by the compiled module"""
    for h in dir(hidden_4):
        if h[:2] != "__":
            print("{:s}".format(h))
