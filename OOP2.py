class Car:
    def __init__(self, make, model, year, odometer, fuel=70):
            self.make = make
            self.model = model
            self.year = year
            self.odometer = 0
            self.fuel = fuel

    def drive(self, distance):
        self.distance = distance
        fuel_existence = self.fuel * 10 / distance
        print(fuel_existence) 

    def __add_distance(self):
        self.odometer += self.distance
        print(self.odometer)

    def __subtract_fuel(self):
        if self.fuel - self.distance / 10 > 0:
            print('lets drive')
        else:
            print('Need more fuel, please, fill more!')

car = Car("Mazda", "rx", "2016", 0)
car.drive(800)

# car.__add_distance()
# car.__subtract_fuel()
