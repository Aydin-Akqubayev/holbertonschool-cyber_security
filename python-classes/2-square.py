#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square class with size validation and area method"""

    def __init__(self, size=0):
        """Initialize a square with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
