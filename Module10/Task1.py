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


elevator = Elevator(1, 5)

elevator.go_to_floor(4)
