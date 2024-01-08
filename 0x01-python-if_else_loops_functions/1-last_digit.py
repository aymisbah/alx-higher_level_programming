#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = number % 10
if(number > 0):
    if(mod < 6 and mod != 0):
        print("Last digit of {:d} is {:d} and is less than 6 and not 0 " .format(number,mod))
    else:
        print("Last digit of {:d} is {:d} and is and is greater than 5 " .format(number,mod))
elif(number < 0):
        mod = number % -10 
        print("Last digit of {:d} is {:d} and is less than 6 and not 0 " .format(number,(mod)))
else:
        print("Last digit of {:d} is {:d} and is 0 " .format(number,mod))
