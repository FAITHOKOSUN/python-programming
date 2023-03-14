class Rectangle:

    """
    Define a rectangle based on 0-rectangle.py
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        per = 2 * (self.__width + self.__height)
        if self.__width ==0 or self.__height ==0:
            return 0
        return per

    def __str__(self):
        str_repr = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for j in range(self.__height):
            for k in range(self.__width):
                str_repr += '#'
            if j != self.__height - 1:
                str_repr += '\n'
        return str_repr

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
