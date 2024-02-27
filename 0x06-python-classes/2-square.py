#!/usr/bin/python3
"""Defines a class Sqr"""


class Square:
    """
    Class that defines properties of sqr by: (based on 1-square.py).

    Attributes:
        size: size of a sqr (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of sqr.

        Args:
            size: size of the sqr (1 side).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
