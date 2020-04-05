from abc import abstractmethod

# director
class Director():
    def __init__(self):
        self._builder = None
    
    
    def set_builder(self, builder):
        self._builder = builder    
    

    @abstractmethod
    def construct(self, field_list): pass
    

    def get_constructed_object(self):
        return self._builder.constructed_object


# abstract builder
class Builder():
    def __init__(self):
        self.constructed_object = None
    

    @abstractmethod
    def add_color(self, color): pass    
    

    @abstractmethod
    def add_type(self, types): pass    
    
    
    @abstractmethod
    def add_year(self, year): pass
