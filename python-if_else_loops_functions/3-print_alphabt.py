#!/usr/bin/python3
for char in range(97, 123):
    if char == ord('q') or char == ord('e'):
        continue
    else:
        print("{:c}".format(char), end="")
