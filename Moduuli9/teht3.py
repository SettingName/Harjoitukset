class Car:
    def __init__(self, license_plate, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
    
    def accelerate(self, speedChange: int):
        self.current_speed = min(max((self.current_speed + speedChange), 0), self.maximum_speed)

    def drive(self, time):
        self.travelled_distance += (self.current_speed * time)