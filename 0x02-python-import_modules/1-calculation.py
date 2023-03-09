#!/usr/bin/python3
# Nice22
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    i = 10
    a = 5
    print("{:d} + {:d} = {:d}".format(i, a, add(i, a)))
    print("{:d} - {:d} = {:d}".format(i, a, sub(i, a)))
    print("{:d} * {:d} = {:d}".format(i, a, mul(i, a)))
    print("{:d} / {:d} = {:d}".format(i, a, div(i, a)))
