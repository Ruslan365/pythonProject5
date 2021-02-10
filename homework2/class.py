from abc import ABC, abstractmethod, abstractproperty
from abc import ABC, abstractmethod, abstractproperty

class Vehicle:
    type_name = None
    def __init__(self, price, weight, lift_capacity):
        self.weight = weight
        self.lift_capaciti = lift_capacity
        self.price = price
        Vehicle.TOTAL_OBJECTS = Vehicle.TOTAL_OBJECTS + 1
    TOTAL_OBJECTS = 0
    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)

class Plane(Vehicle):
    type_name = "самолет"
    def __init__ (self, price, weight, lift_capaciti, max_hight):
        super().__init__(price, weight, lift_capaciti)
        self.max_hight = max_hight

class Car(Vehicle):
    type_name = "автомобиль"
    def __init__(self,price, weight, lift_capaciti,wheel_quantity):
        super().__init__(price, weight, lift_capaciti)
        self.wheel_quantity = wheel_quantity

class Ship(Vehicle):
    type_name = "корабль"
    def __init__(self):
        super().__init__(price, weight, lift_capaciti,displacement)
        self.displacement = displacement

class Light_car(Car):
    type_name = "порше"

    def __init__(self, price, weight, lift_capaciti,wheel_quantity, speed):
        super().__init__(price, weight, lift_capaciti,wheel_quantity)
        self.speed = speed

class Sailing_ship(Ship):
    type_name = "титаник"
    pass

class Military_plane(Plane):
    type_name = "ави"
    pass

demo1 = Military_plane(0,1,2,3)
print (demo1.price, demo1.weight, demo1.lift_capaciti, demo1.max_hight)
demo2 = Light_car(0,1,2,3,4)
print (demo2.price, demo2.weight, demo2.lift_capaciti, demo2.wheel_quantity,demo2.speed )
demo3 = Car(0,1,2,3)
print (demo3.price, demo3.weight, demo3.lift_capaciti, demo3.wheel_quantity)

Vehicle.total_objects()
