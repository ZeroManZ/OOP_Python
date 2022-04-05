# Define a property that must have the same value for every class instance (object)
from oop import vehicle


class Vehicle : 
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self._name = name 
        self._max_speed = max_speed
        self._mileage = mileage

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
        return self


class Bus(Vehicle): 
    pass


class Car(Vehicle): 
    pass

#get,set method

#accessor, mutator method

vehicle = Vehicle('CRB 150', 150, 10)

schoolBus = Bus("SB", 180, 24) 
print("color : ", schoolBus.color, "name :", schoolBus.name, "max_speed", schoolBus.max_speed, "mileage :", schoolBus.mileage)
car_1 = Car("Audi", 240, 30)
print("color :", car_1.color, "name :", car_1.name, "speed :", car_1.max_speed, "mileage : ", car_1.mileage)



# scope accessor 

