import random

class Car:
    def __init__(self, regnumber, maxspeed):
        self.regnumber = regnumber
        self.maxspeed = maxspeed
        self.currentspeed = 0
        self.traveldistance = 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        self.currentspeed += speed_change
        if self.currentspeed < 0:
            self.currentspeed = 0
        elif self.currentspeed > self.maxspeed:
            self.currentspeed = self.maxspeed

    def drive(self, hours):
        self.traveldistance += hours * self.currentspeed

# Main program
cars = []

for i in range(10):
    car = Car(f"ABC-{i + 1}", random.randint(100, 200))
    cars.append(car)

race_finished = False
hours_of_race = 0

while not race_finished:
    hours_of_race += 1
    print(f"--- Hour {hours_of_race} of the race! --- ")

    for car in cars:
        car.accelerate()
        car.drive(1)
        print(f"Registration number: {car.regnumber}, speed: {car.currentspeed}km/h, travel distance: {car.traveldistance}km")

        if car.traveldistance >= 10000:
            print(f"{car.regnumber} has won the race, by reaching {car.traveldistance} km.")
            race_finished = True
            break

print("Race is finished!")

for car in cars:
    print(f"Registration number: {car.regnumber}, final distance: {car.traveldistance}km")






