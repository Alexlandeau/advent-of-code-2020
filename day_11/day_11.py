# -*- coding: utf-8 -*-

# Load necessary modules
import itertools
from functools import lru_cache


TEST = False
INPUT_FILE = "day_11/input.txt"
TEST_FILE = "day_11/test.txt"

if TEST:
    INPUT_FILE = TEST_FILE


# Read input data
with open(INPUT_FILE, "r") as f:
    seat_layout = f.read().split("\n")


class SeatGrid:
    def __init__(self, seat_layout):
        self.grid_size = (len(seat_layout), len(seat_layout[0]))
        self.seats = {}
        self.floor_positions = set()

        for i, line in enumerate(seat_layout):
            for j, seat in enumerate(line):
                if seat != ".":
                    self.seats[(i, j)] = seat
                else:
                    self.floor_positions.add((i, j))

    @lru_cache(maxsize=None)
    def get_adjacent_seats_part2(self, position):
        x, y = position
        i = 1
        seats_in_view = dict.fromkeys(
            {
                "top",
                "top_right_diag",
                "right",
                "bottom_right_diag",
                "bottom",
                "bottom_left_diag",
                "left",
                "top_left_diag",
            }
        )
        while i <= max(x, self.grid_size[0] - x, y, self.grid_size[1] - y):
            if (not seats_in_view.get("top")) and self.seats.get((x - i, y)):
                seats_in_view["top"] = (x - i, y)
            if (not seats_in_view.get("top_right_diag")) and self.seats.get((x - i, y + i)):
                seats_in_view["top_right_diag"] = (x - i, y + i)
            if (not seats_in_view.get("right")) and self.seats.get((x, y + i)):
                seats_in_view["right"] = (x, y + i)
            if (not seats_in_view.get("bottom_right_diag")) and self.seats.get((x + i, y + i)):
                seats_in_view["bottom_right_diag"] = (x + i, y + i)
            if (not seats_in_view.get("bottom")) and self.seats.get((x + i, y)):
                seats_in_view["bottom"] = (x + i, y)
            if (not seats_in_view.get("bottom_left_diag")) and self.seats.get((x + i, y - i)):
                seats_in_view["bottom_left_diag"] = (x + i, y - i)
            if (not seats_in_view.get("left")) and self.seats.get((x, y - i)):
                seats_in_view["left"] = (x, y - i)
            if (not seats_in_view.get("top_left_diag")) and self.seats.get((x - i, y - i)):
                seats_in_view["top_left_diag"] = (x - i, y - i)
            i += 1

        adjacent_positions = [x for x in seats_in_view.values() if x]
        return adjacent_positions

    def get_adjacent_seats(self, position):
        x, y = position

        adjacent_positions = set([(i, j) for i, j in itertools.product(range(x - 1, x + 2), range(y - 1, y + 2))])
        adjacent_positions.remove((x, y))
        adjacent_positions = adjacent_positions - self.floor_positions
        return adjacent_positions

    def get_value_mapping(self, seat_value, adjacent_seats):
        if seat_value == "L" and adjacent_seats.count("#") == 0:
            return "#"
        elif seat_value == "#" and adjacent_seats.count("#") >= 4:
            return "L"
        else:
            return seat_value

    def get_value_mapping_part2(self, seat_value, adjacent_seats):
        if seat_value == "L" and adjacent_seats.count("#") == 0:
            return "#"
        elif seat_value == "#" and adjacent_seats.count("#") >= 5:
            return "L"
        else:
            return seat_value

    def update_grid(self, adjacent_seats_function, value_mapping_function):
        new_seats = {}
        for seat_position, seat_value in self.seats.items():
            adjacent_seats = [self.seats.get(position) for position in adjacent_seats_function(seat_position)]
            new_seats[seat_position] = value_mapping_function(seat_value, adjacent_seats)

        return new_seats

    def update(self, adjacent_seats_function, value_mapping_function):
        i = 0
        stop = False
        while not stop:
            i += 1
            new_seats = self.update_grid(adjacent_seats_function, value_mapping_function)
            if new_seats == self.seats:
                stop = True
                self.rounds_to_converge = i - 1
            else:
                self.seats = new_seats

    def render_seats(self, seats):
        output = []
        for i in range(self.grid_size[0]):
            output.append([])
            for j in range(self.grid_size[1]):
                output[i].append(seats.get((i, j), "."))
            output[i] = "".join(output[i])
        return output


# Part 1

seat_grid = SeatGrid(seat_layout)
seat_grid.update(seat_grid.get_adjacent_seats, seat_grid.get_value_mapping)
available_seats = sum(value == "#" for value in seat_grid.seats.values())
print(f"Part 1: number of occupied seats is {available_seats}")

# Part 2

seat_grid = SeatGrid(seat_layout)
seat_grid.update(seat_grid.get_adjacent_seats_part2, seat_grid.get_value_mapping_part2)
available_seats = sum(value == "#" for value in seat_grid.seats.values())
print(f"Part 2: number of occupied seats is {available_seats}")
