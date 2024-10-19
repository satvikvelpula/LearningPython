class Car:
    def __init__(self, regnumber, maxspeed, currentspeed, traveldistance):
        self.regnumber = regnumber
        self.maxspeed = maxspeed
        self.currentspeed = currentspeed  # Initial speed is 0
        self.traveldistance = traveldistance  # Initial travelled distance is 0

    # Method to change the speed
    def accelerate(self, speed_change):
        # Update the current speed by the speed change
        self.currentspeed += speed_change

        # Ensure that the speed doesn't go below 0
        if self.currentspeed < 0:
            self.currentspeed = 0

    def drive(self, hours):
        self.traveldistance += hours * self.currentspeed

# Main program
car = Car("ABC-123", 142, 60, 2000)  # Create a new car instance

# Display initial state
print(f"Registration number: {car.regnumber}")
print(f"Maximum speed: {car.maxspeed} km/h")
print(f"Current speed: {car.currentspeed} km/h")
print(f"Travelled distance: {car.traveldistance} km")

car.drive(1.5)
print(f"The car's travelling distance is now {car.traveldistance} km")

