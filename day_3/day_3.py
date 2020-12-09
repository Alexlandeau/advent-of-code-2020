# -*- coding: utf-8 -*-

# Read input data
with open("day_3/input.txt", "r") as f:
    grid = f.read().split("\n")


class TobogganTrajectory:
    """
    Class to compute Toboggan trajectory on a map
    """

    DEFAULT_INITIAL_POSITION = (0, 0)

    def __init__(self, map, initial_position=DEFAULT_INITIAL_POSITION):
        self.map = map
        self.map_height = len(self.map)
        self.map_width = len(map[0])
        self.map_dimensions = (self.map_height, self.map_width)
        self.initial_position = initial_position
        self.current_position = self.initial_position
        self.finish = False

    def move(self, slope):
        horizontal_movement = slope[0]
        vertical_movement = slope[1]
        self.current_position = (
            (self.current_position[0] + horizontal_movement) % self.map_width,
            (self.current_position[1] + vertical_movement),
        )
        if self.current_position[1] >= self.map_height:
            self.finish = True

    def check_position(self, obstacle):
        if not self.finish:
            position_value = self.map[self.current_position[1]][self.current_position[0]]
            obstacle_flag = position_value == obstacle
            return obstacle_flag
        else:
            return False

    def generate_trajectory(self, slope):
        while not self.finish:
            self.move(slope)
            yield self.current_position

    def count_obstacles(self, obstacle, slope):
        self.obstacle_counter = 0
        for position in self.generate_trajectory(slope):
            self.obstacle_counter += self.check_position(obstacle)
        return self.obstacle_counter

    def reset(self):
        self.current_position = self.initial_position
        self.obstacle_counter = 0
        self.finish = False


# Part 1
toboggan = TobogganTrajectory(grid)
slope = (3, 1)
tree_count_1 = toboggan.count_obstacles("#", slope)
print(f"Part 1: encountered {tree_count_1} trees")

# Part 2

toboggan.reset()
slope = (1, 1)
tree_count_2 = toboggan.count_obstacles("#", slope)

toboggan.reset()
slope = (5, 1)
tree_count_3 = toboggan.count_obstacles("#", slope)

toboggan.reset()
slope = (7, 1)
tree_count_4 = toboggan.count_obstacles("#", slope)

toboggan.reset()
slope = (1, 2)
tree_count_5 = toboggan.count_obstacles("#", slope)

print(f"Part 2: product is {tree_count_1 * tree_count_2 * tree_count_3 * tree_count_4 * tree_count_5}")
