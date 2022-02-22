class Vehicle:

    def drive(self):
        print("Regular mode driving speed")

    def wheels(self):
        print("4 wheels")

class BMW(Vehicle):

    def drive(self):
        print("Super speed driving mode")

class Maruti(Vehicle):
    pass

bmw = BMW()
bmw.drive()
bmw.wheels()

maruti = Maruti()
maruti.drive()
maruti.wheels()