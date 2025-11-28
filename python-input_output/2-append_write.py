#!/usr/bin/python3
''' Append the file'''


def append_write(file, text):

    '''Practice append function with'''

    with open(file, 'a') as f:
        f.write(text)

    return len(text)
