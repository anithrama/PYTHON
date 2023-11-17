class Car:
    def start_engine(self):
        print("engine started")
class ElectricCar(Car):
    def start_engine(self):
        super().start_engine()
class gasolineCar(Car):
    def start_engine(self):
        super().start_engine()
ev=ElectricCar()
gas=gasolineCar()
ev.start_engine()
gas.start_engine()