#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    res = 0
    for i in args:
        res += int(i)
    print(res)
