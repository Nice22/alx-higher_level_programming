#!/usr/bin/python3
# Nice22
def print_arg(argv):
    a = len(argv) - 1
    if a == 0:
        print("{:d} argument.".format(a))
        return
    else:
        if a == 1:
            print("{:d} argument:".format(a))
        else:
            print("{:d} arguments:".format(a))
        i = 1
        while i <= a:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
