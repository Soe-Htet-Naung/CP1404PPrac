"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("{}, {}, {}".format(my_car.name, my_car.fuel, my_car.odometer))
    print("{self.name} {self.fuel}, {self.odometer}".format(self=my_car))
    """Limo"""
    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print("Fuel Amount In Limo:", limo.fuel)
    limo.drive(115)
    print("Odo of Limo:", limo.odometer)
    print(limo)


main()
