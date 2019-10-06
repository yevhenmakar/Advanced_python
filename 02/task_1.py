class Vehicle:

    NUM_OF_DOORS = 4
    FUEL_TYPE = 'Gas'

    def move(self):
        print('Car drives')

    def brake(self):
        print('Car braking')

    def set_fuel(self, value):
        self._fuel += value

    def get_fuel(self):
        return self._fuel

    def set_brand(self, value):
        self._brand = value

    def get_brand(self):
        return self._brand

    def set_engine(self, value):
        self._engine = value

    def get_engine(self):
        return self._engine

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def __str__(self):
        return f'Brand is {self._brand} and engine as {self._engine}'


class Car(Vehicle):

    def __init__(self, brand, engine, color):
        self._brand = brand
        self._engine = engine
        self._color = color
        self._fuel = 0

    def move(self):
        print('Move about 100 km/h')


class Van(Vehicle):

    NUM_OF_DOORS = 6

    def __init__(self, brand, engine, color):
        self._brand = brand
        self._engine = engine
        self._color = color
        self._fuel = 0

    def move(self):
        print('Move about 60 km/h')

