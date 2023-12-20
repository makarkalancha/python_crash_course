"""A class that can be used to represent an electric car."""

from car import Car
from battery import Battery

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # self.battery_size = 75
        self.battery = Battery()
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        # print(f"This car has a {self.battery_size}-kWh battery.")
        # print('hello')
        self.battery.describe_battery()
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")
