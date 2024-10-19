class Car:
    def __init__(self, regnumber, maxspeed):
        self.regnumber = regnumber
        self.maxspeed = maxspeed
        self.currentspeed = 0  # Initial speed is 0
        self.traveldistance = 0  # Initial travelled distance is 0

    # Method to change the speed
    def accelerate(self, speed_change):
        # Update the current speed by the speed change
        self.currentspeed += speed_change

        # Ensure that the speed doesn't go below 0
        if self.currentspeed < 0:
            self.currentspeed = 0

# Main program
car = Car("ABC-123", 142)  # Create a new car instance

# Display initial state
print(f"Registration number: {car.regnumber}")
print(f"Maximum speed: {car.maxspeed} km/h")
print(f"Current speed: {car.currentspeed} km/h")
print(f"Travelled distance: {car.traveldistance} km")

# Test the accelerate method
car.accelerate(30)  # Accelerate by 30 km/h
print(f"After 30 km/h of acceleration, the car's current speed is {car.currentspeed} km/h")

car.accelerate(70)
print(f"After 70 km/h of more acceleration, the car's current speed is {car.currentspeed} km/h")

car.accelerate(50)
print(f"After 50 km/h of more acceleration, the car's current speed is {car.currentspeed} km/h")

car.accelerate(-200)
print(f"After -200 km/h of deceleration, the car's current speed is {car.currentspeed} km/h")
