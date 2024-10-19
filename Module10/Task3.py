class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Going up! | Current floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Going down! | Current floor: {self.current_floor}")


    def go_to_floor(self, target_floor):
        if target_floor > self.top_floor:
            print("Please enter a valid floor number. ")
        elif target_floor < self.bottom_floor:
            print("Please enter a valid floor number. ")
        else:
            while target_floor > self.current_floor:
                self.floor_up()
            while target_floor < self.current_floor:
                self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators
        self.elevators = []

        for i in range(self.number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, number_of_elevator, target_floor):
        if number_of_elevator < 0:
            print("Please enter a valid number of elevators. ")

        if number_of_elevator >= len(self.elevators):
            print("Index is invalid, please enter a valid number. ")

        selected_elevator = self.elevators[number_of_elevator]
        print(f"Running the elevator {number_of_elevator}. ")
        selected_elevator.go_to_floor(target_floor)

    def fire_alarm(self):
        print("Fire alarm! Fire alarm! All elevators to the first floor! ")
        for index, elevator in enumerate(self.elevators):
            elevator.go_to_floor(self.bottom_floor)
            print(f"Elevator {index + 1} is now at floor {elevator.current_floor}!")

building = Building(1, 5, 4)

# building.run_elevator(2, 4)

building.fire_alarm()






