#!/usr/bin/python3
if __name__ == "__name__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    #count = len(argv) - 1
    

    #if count != 3:
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        op = ['+','-','*','/']

        a = int(argv[1])
        b = int(argv[3])

        if argv[2] == op[0]:
            print("{:d} + {:d} = {:d}".format(a,b, add(a,b)))
        elif argv[2] == op[1]:
            print("{:d} - {:d} = {:d}".format(a,b, sub(a,b)))
        elif argv[2] == op[2]:
            print("{:d} * {:d} = {:d}".format(a,b, mul(a,b)))
        elif argv[2] == op[3]:
            print("{:d} / {:d} = {:d}".format(a,b, div(a,b)))
        elif argv[2] not in op:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
