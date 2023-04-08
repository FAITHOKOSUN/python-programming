#!/usr/bin/python3

bg = __import__('9-rectangle').Rectangle

class Square(bg):
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
