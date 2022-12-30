#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number * abs(1/number)
lastdg = str(number)[-1]
lastdg = int(num*int(lastdg))
if lastdg > 5:
    print("Last digit of {} is {} and is greater than 5".format(number,lastdg))
elif lastdg < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,lastdg))
else:
    print("Last digit of {} is {} and is 0".format(number,lastdg))



