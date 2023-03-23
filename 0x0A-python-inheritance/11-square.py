#!/usr/bin/python3

bg = __import__('9-rectangle').Rectangle

class Square(bg):
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def __str__(self):
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__, self.__size, self.__size)

    def print(self):
        print("[{:s}] {:d}/{:d}".format(self.__class__.__name__, self.__size, self.__size))
