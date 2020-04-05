import builder

'''
simple builder object
'''
if __name__ == "__main__":
    # get car director
    director = builder.DirectorCar()  

    # get car builder
    car = builder.ConcreteCar() 

    # set car builder to car director
    director.set_builder(car)  

    # car attribute for builder object
    car_attribute = {"type": "BMW",     "color": "BLACK",   "year": 2020,}
        
    # build the car
    director.construct(car_attribute)
    
    # print the object
    print(director.get_constructed_object())
