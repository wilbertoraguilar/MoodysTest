import typer
from plateau import Plateau


def delete_newline(s: str):
    return s.replace("\n", "")


def main(file: str):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    lines = [delete_newline(i) for i in lines]
    dimensions = [int(i) for i in lines[0].split(" ")]
    plateau = Plateau(dimensions)
    for idx, rover_line in enumerate(lines[1:]):
        if idx % 2 == 0:
            rover_position = rover_line.split(" ")
            try:
                plateau.add_rover(
                    int(rover_position[0]), int(rover_position[1]), rover_position[2]
                )
            except Exception as exp:
                print("Malformed file data: " + str(exp))
                exit()
        else:
            instructions = rover_line.split(" ")
            plateau.move_current_rover(instructions)
    plateau.print_rover_positions()


if __name__ == "__main__":
    typer.run(main)
