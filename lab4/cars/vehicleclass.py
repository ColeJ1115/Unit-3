class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_status = False

    def start_engine(self):
        self.engine_status = True
        print('Starting Engine...')

    def make_noise(self):
        print('Beep Beep!')


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__( make, miles, price)
        self.cargo = False

    def load_cargo(self):
        self.cargo = True

class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print('Vroom Vroom!!!')

