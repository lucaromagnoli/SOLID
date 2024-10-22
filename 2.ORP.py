"""Open closed principle.

A class should be open for extension but closed for modification.

E.g. If you want to add a new feature to a class, you should not modify the existing class,
but instead create a new class that inherits from the existing class."""
import abc


class Shape(abc.ABC):

    @abc.abstractmethod
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
