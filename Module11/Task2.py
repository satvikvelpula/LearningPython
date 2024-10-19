import random

class Car:
    def __init__(self, regnumber, maxspeed):
        self.regnumber = regnumber
        self.maxspeed = maxspeed
        self.currentspeed = 0
        self.traveldistance = 0


    def accelerate(self): # Acceleration (speed) of the car every hour
        speed_change = random.randint(-10, 15)
        self.currentspeed += speed_change
        if self.currentspeed < 0:
            self.currentspeed = 0
        elif self.currentspeed > self.maxspeed:
            self.currentspeed = self.maxspeed

    def drive(self, hours):
        self.traveldistance += hours * self.currentspeed # Calculating the travel distance of the car for every hour

    def choose_speed(self, chosen_speed):
        pass


class ElectricCar(Car):
    def __init__(self, regnumber, maxspeed, electric_capacity):
        super().__init__(regnumber, maxspeed)
        self.electric_capacity = electric_capacity # Battery (electric) kWh/h

    def choose_speed(self, chosen_speed):
        if chosen_speed > self.maxspeed:
            print(f"Your chosen speed of {chosen_speed} is invalid. Maximum speed is {self.maxspeed}")
        elif chosen_speed < 0:
            print(f"Your chosen speed of {chosen_speed} is invalid. Minimum speed should be greater than 0. ")
        else:
            self.currentspeed = chosen_speed
            print(f"Your chosen speed is {self.currentspeed}km")

    def drive(self, hours):
        super().drive(hours)
        print(f"After driving for {hours} hours, your travel distance is now {self.traveldistance}km")

class GasolineCar(Car):
    def __init__(self, regnumber, maxspeed, gas_capacity):
        super().__init__(regnumber, maxspeed)
        self.gas_capacity = gas_capacity # Gas litres (l)

    def choose_speed(self, chosen_speed):
        if chosen_speed > self.maxspeed:
            print(f"Your chosen speed of {chosen_speed} is invalid. Maximum speed is {self.maxspeed}")
        elif chosen_speed < 0:
            print(f"Your chosen speed of {chosen_speed} is invalid. Minimum speed should be greater than 0. ")
        else:
            self.currentspeed = chosen_speed
            print(f"Your chosen speed is {self.currentspeed}km")

    def drive(self, hours):
        super().drive(hours)
        print(f"After driving for {hours} hours, your travel distance is now {self.traveldistance}km")


class Race:
    def __init__(self, race_name, distance, amount_of_cars):
        self.race_name = race_name # The name of the race
        self.distance = distance # The amount of distance a race has
        self.amount_of_cars = amount_of_cars # The amount of cars in a race
        self.cars = [] # The list to store the amount of cars
        self.race_finished = False
        self.hours_of_race = 0

    def create_car(self):
        for i in range(self.amount_of_cars):
            car = Car(f"ABC-{i + 1}", random.randint(100, 200))
            self.cars.append(car)

    def hours_passes(self):
        for car in self.cars:
            car.accelerate()
            car.drive(1)
            print(f"Registration Number: {car.regnumber} | Speed: {car.currentspeed}km/h | Travel Distance: {car.traveldistance}km")

    def print_status(self):
        print(f"{'Registration Number':<20} {'Speed (km/h)':<15} {'Travel Distance (km)':<20}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.regnumber:<20} {car.currentspeed:<15} {car.traveldistance:<20}")

    def complete_checker(self):
        for car in self.cars:
            if car.traveldistance >= race.distance:
                print("\n")
                print(f"{car.regnumber} has won the race, by reaching {car.traveldistance}km.")
                self.race_finished = True
                break

    def start_race(self):
        while not self.race_finished:
            self.hours_of_race += 1
            if self.hours_of_race % 10 == 0:
                print(f"--- Hour {self.hours_of_race} of the race! --- ")
                self.hours_passes()
                self.complete_checker()

        print("\n")
        print("Result Status:")
        self.print_status()



# --------------------- | Main Program

race = Race("Grand Demolition Derby", 8000, 10)

race.create_car()

race.start_race()

electric_car = ElectricCar("IPK-448", 180, 52.5)
gasoline_car = GasolineCar("GHJ-777", 165, 32.3)

electric_car.choose_speed(20)
gasoline_car.choose_speed(30)

electric_car.drive(3)
gasoline_car.drive(3)