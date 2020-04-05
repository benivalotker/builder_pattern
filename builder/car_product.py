from .abstract_builder import Director, Builder
from collections import defaultdict

# product - the main object type
class Car():
    def __init__(self):    
        self.type = None
        self.color = None
        self.year = None


    def __repr__(self):
        return "{}-{}-{}".format(self.type, self.color, self.year)

    # ----------- add more method for car object -----------

# ConcreteBuilder - builder functionallety
class ConcreteCar(Builder):
    def __init__(self):
        self.constructed_object = Car()
        
    def add_color(self, color):
        self.constructed_object.color = ' color: {}'.format(color)
    
    def add_type(self, type):
        self.constructed_object.type = ' type: {}'.format(type)
    
    def add_year(self, year):
        self.constructed_object.year = ' year: {}\n'.format(year)

    # ----------- add more unit for car builder (depend builder abstract unit) -----------


# ConcreteDirector - control the builder
class DirectorCar(Director):
    def __init__(self):
        Director.__init__(self)

    def construct(self, cars):
        self._builder.add_type(cars.get('type'))
        self._builder.add_color(cars.get('color'))
        self._builder.add_year(cars.get('year'))
