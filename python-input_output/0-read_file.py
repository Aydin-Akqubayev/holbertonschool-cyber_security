#!/usr/bin/python3
"""This is practice input output"""


def read_file(text):
    """This function help open file"""

    with open(text, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end= '')
