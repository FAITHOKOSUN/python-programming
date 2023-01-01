#!/usr/bin/python3
def print_last_digit(number):
    num = number * abs(1/number)
lastdg = str(number)[-1]
lastdg = int(num*int(lastdg))
print (lastdg)
