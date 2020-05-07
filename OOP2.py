class Car:
    def __init__(self, make, model, year, odometer=0,fuel=70):
            self.make = make
            self.model = model
            self.year = year
            self.odometer = odometer
            self.fuel = fuel

    def distance(self):
        distance1 = self.fuel * 10
        print(distance1)

    def __add_distance(self):
        new_distance =  self.odometer + distance1

    def drive(self):
        distance2 = self.odometer // 10
        print(distance2)   

    def subtract_fuel(self):
        if distance1 - distance2 > 0:
            print('lets drive')
        else:
            print('Need more fuel, please, fill more!')

car=Car("Mazda", "rx", "2016",6000)
car.distance()
car.drive()
car.subtract_fuel()
