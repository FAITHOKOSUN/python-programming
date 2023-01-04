#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1

    if count == 0:
        print("{} arguments".format(count))
    elif count == 1:
        print("{} argument".format(count))
    else:
        print("{} argument".format(count))
        for argument in range(count):
            print("{}: {}".format(argument +1 , argv[argument+1]))
    
