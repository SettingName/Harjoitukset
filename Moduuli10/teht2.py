class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
    
    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1
      
    def go_to_floor(self, floorNum: int):
        if self.current_floor < floorNum:
            for number in range(floorNum - self.current_floor):
                self.floor_up()
                print(self.current_floor)

        elif self.current_floor > floorNum:
            for num in range(self.current_floor - floorNum):
                self.floor_down()
                print(self.current_floor)
        else:
            print(self.current_floor)

class Building:
    def __init__(self, bottom_floor, top_floor, elevator_amount):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_amount  =  elevator_amount
        self.elevators = []
        
        for each in range(self.elevator_amount):
            self.elevators.append(Elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self, elevatorNum, floor):
        self.elevators[elevatorNum].go_to_floor(floor)