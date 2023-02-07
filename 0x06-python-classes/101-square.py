#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int\
                or type(value[1]) != int or value[0] < 0 or value[1] < 0:
                    raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def __str__(self):
        if self.__size == 0:
            print()
        ans = ""
        ans += ("" * self.__position[1])
        ans+= "\n"

        for i in range(self.__size):
            ans += ("" * self.__position[0])
            ans += ("#" * self.__size)
            if i != self.__size - 1:
                ans += "\n"
        return ans
