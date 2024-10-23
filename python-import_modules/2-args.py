#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    ln = len(args) - 1
    print("{} {}".format(ln, "argument:" if ln == 1
                         else "arguments:" if ln > 1 else "arguments."))
    if ln > 0:
        for i in range(1, len(args)):
            print("{}: {}".format(i, args[i]))
