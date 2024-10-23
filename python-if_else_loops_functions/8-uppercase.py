#!/usr/bin/python3
def uppercase(str):
    for i in str:
        letter = ord(i)
        if 97 <= ord(i) <= 123:
            letter = ord(i) - 32

        print("{:c}".format(letter), end="")

    print("")
