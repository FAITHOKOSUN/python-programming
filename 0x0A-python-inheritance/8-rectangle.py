#!/usr/bin/python3

bg = __import__('7-base_geometry').BaseGeometry

class Rectangle(bg):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
