#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    b = ((-1 * number) % 10) * -1
else:
    b = number % 10
if b > 5:
    print(f"Last digit of {number} is {b} and is greater than 5")
elif b == 0:
    print(f"Last digit of {number} is {b} and is 0")
elif b < 6 and b != 0:
    print(f"Last digit of {number} is {b} and is less than 6 and not 0")
