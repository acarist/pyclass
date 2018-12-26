class Car(object):

    wheels = 4
    wheel_price = 100

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def make_car_sound():
        print('VRooooommmm!')

    @classmethod
    def wheel_budget(cls):
        return cls.wheels * cls.wheel_price
