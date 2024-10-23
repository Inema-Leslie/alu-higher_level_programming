#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last *= -1

if last > 5:
    st = "and is greater than 5"
elif last == 0:
    st = "and is 0"
else:
    st = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last} {st}")
