#!/usr/bin/python3
"""Defines a class Sqr"""


class Square:
    """
    Class that defines properties of sqr by: (based on 0-square.py).

    Attributes:
        size: size of a sqr (1 side).
    """
    def __init__(self, size):
        """Creates new instances of sqr.

        Args:
            size: size of the sqr.
        """
        self.__size = size
