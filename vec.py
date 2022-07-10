import this


class Vec:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def setXY(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f"({self.__x}, {self.__y})"

    def __add__(self, other):
        return Vec(self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        return Vec(self.__x - other.__x, self.__y - other.__y)
    
