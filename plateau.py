from typing import List


class Rover:
    x: int
    y: int
    direction: str

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def rotate(self, instruction):
        if self.direction == "N":
            if instruction == "L":
                self.direction = "W"
            if instruction == "R":
                self.direction = "E"
        elif self.direction == "S":
            if instruction == "L":
                self.direction = "E"
            if instruction == "R":
                self.direction = "W"
        elif self.direction == "E":
            if instruction == "L":
                self.direction = "N"
            if instruction == "R":
                self.direction = "S"
        elif self.direction == "W":
            if instruction == "L":
                self.direction = "S"
            if instruction == "R":
                self.direction = "N"

    def move(self):
        if self.direction == "N":
            self.y += 1
        if self.direction == "S":
            self.y -= 1
        if self.direction == "E":
            self.x += 1
        if self.direction == "W":
            self.x -= 1


class Plateau:
    dimensions: List[int]
    rovers = []

    def __init__(self, dimensions: List[int]):
        self.dimensions = dimensions

    def add_rover(self, x, y, direction):
        self.rovers.append(Rover(x, y, direction))

    def move_current_rover(self, instructions):
        current_rover = self.rovers[len(self.rovers) - 1]
        for instruction in instructions:
            if instruction == "L" or instruction == "R":
                current_rover.rotate(instruction)
            if instruction == "M":
                if current_rover.direction == "N":
                    if current_rover.y + 1 > self.dimensions[1]:
                        print("This move would overflow the plateau's dimensions.")
                        exit()
                if current_rover.direction == "S":
                    if current_rover.y - 1 < 0:
                        print("This move would overflow the plateau's dimensions.")
                        exit()
                if current_rover.direction == "E":
                    if current_rover.x + 1 > self.dimensions[0]:
                        print("This move would overflow the plateau's dimensions.")
                        exit()
                if current_rover.direction == "W":
                    if current_rover.x - 1 < 0:
                        print("This move would overflow the plateau's dimensions.")
                        exit()
                current_rover.move()

    def print_rover_positions(self):
        for rover in self.rovers:
            print(str(rover.x) + " " + str(rover.y) + " " + rover.direction)
