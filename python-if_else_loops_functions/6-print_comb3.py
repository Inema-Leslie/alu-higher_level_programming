#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i:
            print("{:d}{:d}".format(i, j),
                  end=", " if [i, j] != [8, 9] else None)
