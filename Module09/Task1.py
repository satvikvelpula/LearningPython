class Car:
    def __init__(self, regnumber, maxspeed, currentspeed=0, traveldistance=0):
        self.regnumber = regnumber
        self.maxspeed = maxspeed
        self.currentspeed = 0
        self.traveldistance = 0

car = Car("GHJ-777", 202)

print(f"Registration number of the car: {car.regnumber}")
print(f"Max speed of the car: {car.maxspeed}km/h")
print(f"Current speed of the car: {car.currentspeed}km/h")
print(f"Travel distance of the car: {car.traveldistance}km")