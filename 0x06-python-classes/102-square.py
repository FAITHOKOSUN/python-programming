#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int or type(value) != float:
            raise TypeError("size must be a number")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        first = self.area
        second = other.area
        return first == second

    def __ne__(self, other):
        first = self.area
        second = other.area
        return first != second

    def __gt__(self, other):
        first = self.area
        second = other.area
        return first > second

    def __ge__(self, other):
        first = self.area
        second = other.area
        return first >= second

    #def __lt__(self, other):
     #   first = self.area
      #  second = other.area
       # return first < second

    def __le__(self, other):
        first = self.area
        second = other.area
        return first <= second
