#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number == 0:
    val = "{} is zero".format(number)
elif number > 0:
    val = "{} is positive".format(number)
else:
    val = "{} is negative".format(number)

print(val)
