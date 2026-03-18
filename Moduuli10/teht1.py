class Elevator:
    def __init__(self, min_floor, max_floor):
        self.current_floor = min_floor
        self.min_floor = min_floor
        self.max_floor = max_floor
    
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