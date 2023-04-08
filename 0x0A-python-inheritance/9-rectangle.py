#!/usr/bin/python3

bg = __import__('7-base_geometry').BaseGeometry

class Rectangle(bg):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def print():
        print(f"[{__class__.__name__}] {self.__width}/{self.__height}")

    def __str__(self):
        return f"[{__class__.__name__}] {self.__width}/{self.__height}"
