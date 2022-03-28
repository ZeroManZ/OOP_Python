# write a python program to create a vehicle class with max_speed and mileage instance attribute
class vehicle : 
    def __init__(self,max_speed,mileage) :
        self.max_speed = max_speed
        self.mileage = mileage 

model_X = vehicle(240,18)
print(model_X.max_speed,model_X.mileage)