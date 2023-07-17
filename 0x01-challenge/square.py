#!/usr/bin/python3
"""module for square class"""

class square():
    """class square """
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """class instantiation"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string representation"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """creating a square object"""
    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())